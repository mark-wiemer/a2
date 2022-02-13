/*
Library for getting info from a specific Explorer window.Length
If window handle not specified, the currently active window will be used.
Works with the desktop. Does not currently work with save dialogs and such.

examples:
	path := explorer_get_path()
	all := explorer_get_all()
	sel := explorer_get_selected()

Joshua A. Kinnison
2011-04-27, 16:12
*/

explorer_get_selected(hwnd="") {
    ; Get array of paths of selected items via Explorer window handle.
    return explorer_get(hwnd, true)
}

explorer_get_path(hwnd="") {
    ; Get path of target window's folder.
    if !(window := explorer_get_window(hwnd))
        return ErrorLevel := "ERROR"
    if (window="desktop")
        return A_Desktop
    pth := RegExReplace(window.LocationURL, "ftp://.*@", "ftp://")
    pth := StrReplace(pth, "file:///", "")
    pth := StrReplace(pth, "/", "\")
    ; thanks to polyethene
    Loop
    {
        ; What the hell?!? This is to replace percentage notation, right?
        If RegExMatch(pth, "i)(?<=%)[\da-f]{1,2}", hex)
            StringReplace, pth, pth, `%%hex%, % Chr("0x" . hex), All
        Else
            Break
    }
    return pth
}

explorer_get_all(hwnd="") {
    ; Get array of paths of ALL items via Explorer window handle.
    return explorer_get(hwnd)
}

explorer_get_window(hwnd="") {
    ; Get Explorer window COM object from handle.
    ; thanks to jethrow for some pointers here
    WinGet, proc, processName, % "ahk_id" hwnd := hwnd? hwnd:WinExist("A")
    if (proc != "explorer.exe")
        return

    WinGetClass clss, ahk_id %hwnd%
    if (clss ~= "(Cabinet|Explore)WClass") {
        for window in ComObjCreate("Shell.Application").Windows
            Try if (window.hwnd==hwnd)
            return window
    }
    else if (clss ~= "Progman|WorkerW")
        return "desktop" ; desktop found
    else if (clss == "Shell_TrayWnd")
        return
}

explorer_get(hwnd="",selection=false) {
    ; Get items from an Explorer window via handle.
    if !(window := explorer_get_window(hwnd))
        return ErrorLevel := "ERROR"

    result := []
    if (window="desktop")
    {
        ControlGet, hwWindow, HWND,, SysListView321, ahk_class Progman
        if !hwWindow ; #D mode
            ControlGet, hwWindow, HWND,, SysListView321, A
        ControlGet, files, List, % ( selection ? "Selected":"") "Col1",,ahk_id %hwWindow%
        base := SubStr(A_Desktop,0,1)=="\" ? SubStr(A_Desktop,1,-1) : A_Desktop
        Loop, Parse, files, `n, `r
        {
            pth := base "\" A_LoopField
            IfExist %pth% ; ignore special icons like Computer (at least for now)
                result.Push(pth)
        }
    }
    else
    {
        if selection
            collection := window.document.SelectedItems
        else
            collection := window.document.Folder.Items

        for item in collection
            result.Push(item.path)
    }
    return result
}

explorer_select(basename) {
    ; Selects a file with the given basename
    if !(window := explorer_get_window(""))
        return ErrorLevel := "ERROR"
    file_found := 0
    for item in window.document.Folder.Items
    {
        if (item.name == basename)
        {
            window.document.SelectItem(item, 1)
            file_found := 1
        } else {
            window.document.SelectItem(item, 0)
        }
    }
    return file_found
}

explorer_show(pth) {
    ; Open an Explorer with the given directory or file selected.
    pth := StrReplace(pth, "\\", "\")
    pth := StrReplace(pth, "/", "\")

    explorer_path := path_join(A_WinDir, "explorer.exe")
    if path_is_file(pth)
        cmd := """" explorer_path """ /select, """ pth """"
    else if path_is_dir(pth)
        cmd := """" explorer_path """ """ pth """"
    else if (pth == "") {
        cmd := """" explorer_path """"
    }
    else
        MsgBox, No such path to explorer to!`n %pth%

    Run, %cmd%
}

; Ask for file name as long that name exists in given directory or user cancels. Return `true` if name is available and accepted and `false` if canceled.
explorer_create_file_dialog(ByRef file_name, dir_path, extension, file_label, title, subtitle := "", w := 420, h:= 140)
{
    if (!dir_path) {
        MsgBox, No dir_path given!
        Return
    }

    extension := Trim(string_prefix(extension, "."))
    StringLower, extension, extension

    msg := "Please enter a name for the new " file_label ":`n"
    InputBox, file_name, %title%, %msg%%subtitle%,, 420, 140,,,,, %file_name%
    if ErrorLevel {
        Return false
    }

    file_path := __create_dialog_build_path(dir_path, file_name, extension)
    while (Trim(file_name) == "" OR FileExist(file_path)) {
        if FileExist(file_path)
            msg := "This file name already exists! Please pick another " file_label " name!`n"
        else
            msg := "Please enter NON-EMPTY name for the new " file_label ":`n"

        InputBox, file_name, %title%, %msg%%subtitle%,, 420, 140,,,,, %file_name%
        if ErrorLevel {
            Return false
        }

        file_path := __create_dialog_build_path(dir_path, file_name, extension)
    }
    Return true
}

__create_dialog_build_path(dir_path, file_name, extension)
{
    this_ext := path_split_ext(file_name)[2]
    if this_ext
    {
        StringLower, this_ext, this_ext
        this_ext := Trim(string_prefix(this_ext, "."))

        if (this_ext == extension) {
            Return path_join(dir_path, file_name)
        }
    }
    Return path_join(dir_path, file_name extension)
}
