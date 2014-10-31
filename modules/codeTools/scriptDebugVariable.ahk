scriptDebugVariable() {
	selection := getSelection()

	if (selection = "")	{
		tt("nothing selected!",1)
		return
	}

	code := ""
	IfWinActive, ahk_class Notepad++
	{
		; get the type of script --------------------
		; get window id
		WinGet, notepad_id, ID, A
		; get text from the statusline
		ControlGetText, statusText, msctls_statusbar321, ahk_id %notepad_id%
		if statusText =
			ControlGetText, statusText, msctls_statusbar322, ahk_id %notepad_id%

		if InStr(statusText,"AHK")
			scriptType = ahk
		else if InStr(statusText,"Python")
			scriptType = py
		else if InStr(statusText,"mel")
			scriptType = mel
		else
			msgBox statusText is: "%statusText%"`nWhat does it mean!?
		
		If (scriptType = "ahk") { ; the Autohotkey case
			code = MsgBox %selection%: `%%selection%`%
			paste( code )
		}
		Else If (scriptType = "mel") ; the MEL case
			pasteMel( selection )
		Else If (scriptType = "py") ; the python case
			pastePy( selection )
	}
	Else IfWinActive, Script Editor ahk_class AfxFrameOrView80
		pasteMel( selection )
	Else IfWinActive, Script Editor ahk_class QWidget
		pastePy( selection )
}

; var = ['sadfas','DFGSDF'] # from 'var' selected this makes:
; print( 'var: ' + str(var) ) # and prints:
; var: ['sadfas', 'DFGSDF']
pastePy( byref text ) {
	code = print( '%text%: ' + str(%text%) + '\n'),
	paste( code )
}

pasteMel( byref text ) {
	code = print( "%text%: \"" + %text% + "\"\n");
	paste( code )
}