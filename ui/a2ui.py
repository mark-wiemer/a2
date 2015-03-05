# a2ui
from PySide import QtGui, QtCore
import os
from os.path import exists, join
from functools import partial
import sys
import logging
import a2dblib
import a2design_ui
import json
logging.basicConfig()
log = logging.getLogger('a2ui')
log.setLevel(logging.DEBUG)


class A2Window(QtGui.QMainWindow):
    def __init__(self):
        super(A2Window, self).__init__()

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("_dump/a2logo 16.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        self.initPaths()
        self.dbfile = join(self.a2setdir, 'a2.db')
        # create db connection: use test\a2dbtest.py to test it
        self.db = a2dblib.A2db(self.dbfile)

        self.enabledMods = self.db.get('enabled', 'a2')
        log.info('enabledMods: %s' % self.enabledMods)

        self.fetchModules()

        self.ui = a2design_ui.Ui_a2Widget()
        self.ui.setupUi(self.ui)

        self.maintab = self.ui.scrollAreaContents
        
        self.mainlayout = self.ui.verticalLayout_4
        self.currtab = self.maintab
        
        # create a spacer to arrange the layout
        # NOTE that a spacer is added via addItem! not widget
        self.ui.spacer = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum,
                                           QtGui.QSizePolicy.Expanding)
        self.mainlayout.addItem(self.ui.spacer)

        self.ui.modList.insertItems(0, list(self.modules.keys()))
        self.ui.modList.itemSelectionChanged.connect(self.modSelect)
        self.selectedMod = None

        self.setCentralWidget(self.ui)
        self.setWindowTitle("a2")
        #TODO: remember size and window position
        self.setGeometry(QtCore.QRect(250, 250, 1268, 786))

        log.info('a2ui initialised!')

    def modSelect(self, force=False):
        """
        updates the mod view to the right of the UI when something different is
        selected in the module list 
        """
        name = self.ui.modList.selectedItems()[0].text()
        if name == self.selectedMod and force is False:
            return
        
        log.debug('sel: %s' % name)
        
        self.selectedMod = name
        mod = self.modules[name]
        
        self.drawMod(mod)
        
    def drawUI(self, controls):
        """
        takes list of controls and arranges them in the scroll layout
        
        1. I tried to just create layouts for each module unhook them from the
        scroll layout on demand and hook up another one but Qt is spart so it
        deletes the invisible layout which cannot be hooked up again.
        2. I tried to brute force delete everything and building it over again each
        time something else is seleceted in the left list but Qt refuses to
        delete anything visually with destroy() or removeWidget()
        3. We probably need an actual tab layout to do this but I can't find how to
        make the tabs invisible...
        4. I'll try to create an all new layout,
            fill it and switch away from the old one:
        """
        # to refill the scoll layout:
        # take away the spacer from 'mainLayout'
        self.mainlayout.removeItem(self.ui.spacer)
        # create widget to host the module's new layout 
        newLayout = QtGui.QWidget()
        # create new columnLayout for the module controls
        newInner = QtGui.QVBoxLayout(newLayout)
        
        ### create the contols
        ##self.drawUI(mod)
        
        # make the new inner layout the mainLayout
        self.mainlayout = newInner
        # add the controls to it
        for ctrl in controls:
            self.mainlayout.addWidget(ctrl)
        # amend the spacer
        self.mainlayout.addItem(self.ui.spacer)
        # turn scroll layout content to new host widget
        self.ui.scrollArea.setWidget(newLayout)
    
    def drawMod(self, mod):
        """
        from the modules config creates the usual display controls and
        fills them with the saved settings from the database.
        On change they trigger writing to the db, collect all include info
        and restart a2.
        """
        log.debug('drawing: %s' % mod.name)
        controls = []
        if exists(mod.configFile):
            try:
                with open(mod.configFile) as fObj:
                    mod.config = json.load(fObj)
            except:
                mod.config = {}
                controls.append(QtGui.QLabel('config.json currently empty. imagine placeholder layout here ...'))
            
            log.debug('config: >%s<' % mod.config)
            buttonText = 'Edit'
        else:
            mod.config = {}
            controls.append(QtGui.QLabel('"%s" has no configuration file yet!\n'
                                         'Would you like to set one up?' % mod.name))
            buttonText = 'Create'
        
        log.debug('creating display controls here...')
        
        # add temp edit button. This will goto the menu bar in the future or to a hotkey Ctrl+E?
        editButton = QtGui.QPushButton(buttonText)
        editButton.pressed.connect(partial(self.editMod, mod))
        controls.append(editButton)
        
        self.drawUI(controls)
        
    def editMod(self, mod):
        """
        From the modules config creates controls to edit the config itself.
        If a header is not found one will be added to the in-edit config.
        On OK the config data is collected from the UI and written back to the json.
        On Cancel the in-edit config is discarded and the standard drawMod called
        to show the UI without change.
        """
        log.debug('editing: %s' % mod.name)
        controls = []
        
        s = "Because none existed before this temporary description was created for %s. "\
            "Change it to describe what it does with a couple of words." % mod.name
        config = dict(mod.config)
        if 'nfo' not in config:
            config['nfo'] = {'description': s,
                             'display name': '%s' % mod.name,
                             'author': 'your name',
                             'version': '0.1',
                             'date': '2015'}
        
        ctrlDict = {}
        
        # create header edit controls
        def editctrl(nfoDict, keyName, typ, parent, editCtrls):
            label = QtGui.QLabel('%s:' % keyName)
            parent.addWidget(label)
            if typ == 'text':
                inputctrl = QtGui.QPlainTextEdit()
                inputctrl.setPlainText(nfoDict.get(keyName) or '')
            else: 
                inputctrl = QtGui.QLineEdit()
                inputctrl.setText(nfoDict.get(keyName) or '')
            parent.addWidget(inputctrl)
            editCtrls[keyName] = inputctrl
            
        nfo = config.get('nfo')
        nfoCtrls = {}
        nfoBox = QtGui.QGroupBox()
        nfoBox.setTitle('module information:')
        nfoBoxLayout = QtGui.QVBoxLayout(nfoBox)
        
        editctrl(nfo, 'display name', 'line', nfoBoxLayout, nfoCtrls)
        editctrl(nfo, 'description', 'text', nfoBoxLayout, nfoCtrls)
        editctrl(nfo, 'author', 'line', nfoBoxLayout, nfoCtrls)
        editctrl(nfo, 'version', 'line', nfoBoxLayout, nfoCtrls)
        editctrl(nfo, 'date', 'line', nfoBoxLayout, nfoCtrls)
        
        controls.append(nfoBox)
        log.debug('creating EDIT controls here...')
        
        ctrlDict['nfo'] = nfoCtrls
        
        # amend OK, Cancel buttons at the end
        editFooter = QtGui.QWidget()
        editFooterLayout = QtGui.QHBoxLayout(editFooter)
        okButton = QtGui.QPushButton('OK')
        okButton.pressed.connect(partial(self.editSubmit, ctrlDict))
        cancelBtn = QtGui.QPushButton('Cancel')
        cancelBtn.pressed.connect(partial(self.drawMod, mod))
        editFooterLayout.addWidget(okButton)
        editFooterLayout.addWidget(cancelBtn)
        controls.append(editFooter)
        
        self.drawUI(controls)
    
    def editSubmit(self, ctrlDict):
        log.debug('editSubmit...')
        for nme, ctrl in ctrlDict['nfo'].items():
            if isinstance(ctrl, QtGui.QPlainTextEdit):
                text = ctrl.toPlainText()
            else:
                text = ctrl.text()
            log.debug('%s: %s' % (nme, text))

    def editCancel(self):
        log.debug('editCancel...')
    
    def settingsChanged(self, mod):
        print('mod: ' + str(self.modules[mod]))
    
    def fetchModules(self):
        self.modules = {}
        for mod in os.listdir(self.a2moddir):
            self.modules[mod] = Mod(mod, self.a2moddir, self.db)

    def initPaths(self):
        """ makes sure all necessary paths and their variables are available """
        # if run on its own sys.path[0] will be the script dir
        self.a2uidir = sys.path[0]
        if not self.a2uidir:
            #self.a2uidir = 'C:/My Files/code/a2/ui'
            cwd = os.getcwd()
            if exists(join(cwd, 'a2ui.py')):
                self.a2uidir = cwd
                log.info('fetched a2ui dir from cwd... %s' % cwd)
            else:
                raise Exception('a2ui start interrupted! '
                                'Could not get main Ui dir!')

        self.a2dir = os.path.dirname(self.a2uidir)
        self.a2libdir = self.a2dir + '/' + 'lib/'
        self.a2exe = self.a2dir + '/a2Starter.exe'
        self.a2ahk = self.a2dir + '/a2.ahk'
        self.a2setdir = self.getSettingsDir()
        self.a2moddir = self.a2dir + '/' + 'modules/'
        # test if all necessary directories are present:
        mainItems = [self.a2ahk, self.a2exe, self.a2libdir, self.a2moddir,
                     self.a2setdir, self.a2uidir]
        missing = [p for p in mainItems if not exists(p)]
        if missing:
            raise Exception('a2ui start interrupted! %s not found in main dir!'
                            % missing)
        if not os.access(self.a2setdir, os.W_OK):
            raise Exception('a2ui start interrupted! %s inaccessable!'
                            % self.a2setdir)

    def getSettingsDir(self):
        """ TODO: temporary under a2dir!! has to be VARIABLE! """
        return join(self.a2dir, 'settings')


class Mod(object):
    """
    WIP! A ui wrapper for an a2 module
    The ui creates such a Mod instance when dealing with it
    from this it gets all information that it displays (hotkey interface,
    buttons, sliders, checkboxes, text, and the language for that)

    also holds the requirements of the module such as local (in the module folder)
    or global (in the a2/libs folder) libs.
    stores the available parts of the module that can be enabled in the ui.
    also the according variables, hotkeys, defaults, inits
    encapsulates the background functions for enabling/disabling a part
    
    config is None at first and filled as soon as the mod is selected in the UI.
    If there is no configFile yet it will be emptied instead of None.
    """
    def __init__(self, modname, a2moddir, db):
        # gather files from module path in local list
        self.name = modname
        self.dir = join(a2moddir, modname)
        self.config = None
        self.configFile = join(self.dir, 'config.json')
        self.db = db
        self.ui = None

    @property
    def files(self):
        return self.getFiles()

    def enable(self, part):
        """
        # enlist filename to settings/includes.ahk
        # kickoff a2reload
        # write a2db mod/part list
        """
        pass

    def disable(self, part):
        """
        # takes filename from settings/includes.ahk
        # kickoff a2reload
        # write a2db mod/part list
        """
        pass

    def getFiles(self):
        """
        browses the modules folder for files that belong to a module part
        # script file - the filename to be enlisted to the includes
        # defaults file - variable defaults and hotkey suggestions
        # language file - for ui and runtime
        """
        return os.listdir(self.dir)

    def createConfig(self, main=None):
        log.debug('%s config exists: %s' % (self.name, exists(self.configFile)))
        with open(self.configFile, 'w') as fileObj:
            fileObj.write('')
        log.debug('%s config exists: %s' % (self.name, exists(self.configFile)))
        if main:
            main.modSelect(True)
        

class A2Obj(object):
    """
    WIP!: this doesn't really work well... somhow I'd like a console
    that can talk to the running ui window. Gotta learn more Qt...
    """
    def __init__(self):
        self.app = QtGui.QApplication([])
        self.ui = A2Window()
        self.ui.show()
        log.info('aaaand its gone!')
        #exit(self.app.exec_())


if __name__ == '__main__':
    # if in main thread, run the ui directly
    app = QtGui.QApplication(sys.argv)
    a2ui = A2Window()
    a2ui.show()
    exit(app.exec_())
else:
    # otherwise offer a scripting interface
    log.error('__name__ != "__main__": %s' % __name__)
    log.info('fetch an A2Obj e.g.:\n\ta2 = a2ui.A2Obj()\n')


def a2reload():
    # engages the a2.ahk runtime to shutdown and restart
    # preferably in another thread?
    pass


def r():
    # debug wrapper to reload a2ui in py env
    __import__(sys.modules['a2ui'])
    __import__(sys.modules['a2dblib'])
    return A2Window()