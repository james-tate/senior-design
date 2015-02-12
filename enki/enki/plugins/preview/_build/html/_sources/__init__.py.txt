
**********************************************************
__init__.py - The HTML, Markdown, and reST preview package
**********************************************************
The Preview plugin provides an HTML-based rendering of the
file currently being edited. This file implements the
Plugin interface; other modules are given below.

::

 # wokifvzohtdlm
 
 import sys
 import os.path
 from PyQt4.QtCore import QObject, Qt, pyqtSlot
 from PyQt4.QtGui import QAction, QIcon, QKeySequence, QWidget, QFileDialog, QPalette
 from PyQt4 import uic
 
 from enki.core.core import core
 from enki.core.uisettings import CheckableOption, TextOption, ChoiseOption
 from enki.lib.get_console_output import get_console_output
 
 # wokifvzohtdlm

Import CodeChat if possible; otherwise, indicate it wasn't available.

::

 # wokifvzohtdlm
 try:
     import CodeChat
     import CodeChat.LanguageSpecificOptions as LSO
 except ImportError:
     CodeChat = None
 
 def isHtmlFile(document):
     return document is not None and  \
            document.qutepart.language() is not None and \
            'html' in document.qutepart.language().lower()  and \
            (not 'php' in document.qutepart.language().lower())  # Django HTML template but not HTML (PHP)
 
 def _getSphinxVersion(path):
     """Return the Sphinx version as a list of integer items.
 
     Raise OSError if not found, or
           ValueError if failed to parse.
     """
     stdout, stderr = get_console_output(path)
     for line in stderr.split('\n'):
         if line.startswith("Sphinx"):
 # wokifvzohtdlm

..

 ..

  ..

   ..

    ..

     ..

      ..

       ..

        ..

         ..

          ..

           ..

            Typical line we're looking for, taking from running
            ``sphinx-build`` on the command line: ``Sphinx v1.2.3``.
            Therefore, ``line.split()[1][1:] == '1.2.3'``.

::

 # wokifvzohtdlm
             version = line.split()[1][1:]
 # wokifvzohtdlm

..

 ..

  ..

   ..

    ..

     ..

      ..

       ..

        ..

         ..

          ..

           ..

            Split on periods and convert to an int, returning the version as a
            tuple.

::

 # wokifvzohtdlm
             return [int(num) for num in version.split('.')]
     raise ValueError
 
 class SettingsWidget(QWidget):
     """Insert the preview plugin as a page of the UISettings dialog.
     """
     def __init__(self, *args):
 # wokifvzohtdlm

..

 ..

  ..

   ..

    ..

     ..

      ..

       ..

        Initialize the dialog, loading in the literate programming settings GUI.

::

 # wokifvzohtdlm
         QWidget.__init__(self, *args)
         uic.loadUi(os.path.join(os.path.dirname(__file__), 'Settings.ui'), self)
 
 # wokifvzohtdlm

..

 ..

  ..

   ..

    ..

     ..

      ..

       ..

        Make links gray when they are disabled

::

 # wokifvzohtdlm
         palette = self.palette()
         palette.setColor(QPalette.Disabled,
                          QPalette.Link,
                          palette.color(QPalette.Disabled, QPalette.Text))
         self.lbSphinxReference.setPalette(palette)
 
         palette = self.palette()
         palette.setColor(QPalette.Active,
                          QPalette.WindowText,
                          palette.color(QPalette.Normal, QPalette.Link))
         self.lbSphinxEnableAdvMode.setPalette(palette)
 
         self.labelCodeChatIntro.setEnabled(1)
         if CodeChat is None:
 # wokifvzohtdlm

..

 ..

  ..

   ..

    ..

     ..

      ..

       ..

        ..

         ..

          ..

           ..

            If the CodeChat module can't be loaded, then disable the
            associated checkbox and show the "not installed" message.

::

 # wokifvzohtdlm
             self.cbCodeChat.setEnabled(False)
             self.labelCodeChatNotInstalled.setVisible(True)
             self.labelCodeChatNotInstalled.setEnabled(True)
         else:
 # wokifvzohtdlm

..

 ..

  ..

   ..

    ..

     ..

      ..

       ..

        ..

         ..

          ..

           ..

            Hide the "not installed" message.

::

 # wokifvzohtdlm
             self.labelCodeChatNotInstalled.setVisible(False)
 
 # wokifvzohtdlm

..

 ..

  ..

   ..

    ..

     ..

      ..

       ..

        Clicking on advanced mode label triggers either advanced mode or
        normal mode.

::

 # wokifvzohtdlm
         self.lbSphinxEnableAdvMode.mousePressEvent = self.on_ToggleSphinxSettingModeClicked
 
 # wokifvzohtdlm

..

 ..

  ..

   ..

    ..

     ..

      ..

       ..

        Update misc pieces of the GUI that can't be stored in the .ui file.

::

 # wokifvzohtdlm
         self._updateSphinxSettingMode()
 
     def _updateleValidateSphinxExecutable(self):
         """ Check if Sphinx is installed. Sphinx version is not important
 
         Update leValidateSphinxExecutable based on Sphinx status.
         """
         path = self.leSphinxExecutable.text()
         try:
             _getSphinxVersion(path)
         except OSError as ex:
             self.leValidateSphinxExecutable.setText('Failed to execute {}: {}'.format(path, ex))
         except ValueError:
             self.leValidateSphinxExecutable.setText('Failed to parse {} version. Does sphinx work?'.format(path))
         else:
             self.leValidateSphinxExecutable.setText('Sphinx is found!')
 
     @pyqtSlot()
     def on_pbSphinxProjectPath_clicked(self):
         """Provide a directory chooser for the user to select a project path.
         """
         path = QFileDialog.getExistingDirectory(core.mainWindow(),
             'Project path', self.leSphinxProjectPath.text())
         if path:
             self.leSphinxProjectPath.setText(path)
 # wokifvzohtdlm

..

 ..

  ..

   ..

    ..

     ..

      ..

       ..

        ..

         ..

          ..

           ..

            Automatically set the builder output path to '_build\\html' under
            builder root path.
            
            Since relative paths are supported, we will only set
            leSphinxOutputPath if the path was none or was absolute (and
            therefore presumabely wrong). If it's a relative path such as
            ``_build\html``, then it's probably OK without changing.

::

 # wokifvzohtdlm
             if (not self.leSphinxOutputPath.text()
                 or os.path.isabs(self.leSphinxOutputPath.text())):
                 self.leSphinxOutputPath.setText(os.path.join(path, '_build', 'html'))
 
     @pyqtSlot()
     def on_pbSphinxOutputPath_clicked(self):
         """Proivde a directory chooser for the user to select an output path.
         """
         path = QFileDialog.getExistingDirectory(core.mainWindow(), 'Output path')
         if path:
             self.leSphinxOutputPath.setText(path)
 
 # wokifvzohtdlm

..

 ..

  ..

   ..

    The Sphinx executable can be selected by the user. A filter is needed
    such that non-executable files will not be selected by the user.

::

 # wokifvzohtdlm
     @pyqtSlot()
     def on_pbSphinxExecutable_clicked(self):
         fltr = "sphinx-build" + (".exe" if sys.platform.startswith("win") else "") \
                + ";; All files (*)"
         path = QFileDialog.getOpenFileName(self,
                                            "Select Sphinx executable",
                                            filter=fltr)
         if path:
             self.leSphinxExecutable.setText(path)
             self._updateleValidateSphinxExecutable()
 
     def on_ToggleSphinxSettingModeClicked(self, *args):
         core.config()['Sphinx']['AdvancedMode'] = not core.config()['Sphinx']['AdvancedMode']
         core.config().flush()
         self._updateSphinxSettingMode()
 
 # wokifvzohtdlm

..

 ..

  ..

   ..

    The project path and Sphinx executable directory must be absolute;
    the output path may be relative to the project path or absolute.
    Use abspath or normpath as appropriate to guarantee this is true.

::

 # wokifvzohtdlm
     def on_leSphinxProjectPath_editingFinished(self):
         self.leSphinxProjectPath.setText(os.path.abspath(self.leSphinxProjectPath.text()))
 
     def on_leSphinxOutputPath_editingFinished(self):
         self.leSphinxOutputPath.setText(os.path.normpath(self.leSphinxOutputPath.text()))
 
     def on_leSphinxExecutable_editingFinished(self):
         self._updateleValidateSphinxExecutable()
 
     def _updateSphinxSettingMode(self):
         """Update the Sphinx settings mode by hiding/revealing the appropriate
         controls.
         """
         if core.config()['Sphinx']['AdvancedMode']:
 # wokifvzohtdlm

..

 ..

  ..

   ..

    ..

     ..

      ..

       ..

        ..

         ..

          ..

           ..

            Switch to advanced setting mode:
            hide all path setting line edit boxes and buttons.

::

 # wokifvzohtdlm
             for i in range(self.gridLtNotAdvancedSettings.count()):
                 if self.gridLtNotAdvancedSettings.itemAt(i):
                     self.gridLtNotAdvancedSettings.itemAt(i).widget().setVisible(False)
 # wokifvzohtdlm

..

 ..

  ..

   ..

    ..

     ..

      ..

       ..

        ..

         ..

          ..

           ..

            Enable advanced setting mode items

::

 # wokifvzohtdlm
             self.lbSphinxEnableAdvMode.setText('<html><head/><body><p>' +
             '<span style="text-decoration: underline;">Switch to Normal Mode' +
             '</span></p></body></html>')
             self.lbSphinxCmdline.setVisible(True)
             self.leSphinxCmdline.setVisible(True)
             self.lbSphinxReference.setVisible(True)
         else:
 # wokifvzohtdlm

..

 ..

  ..

   ..

    ..

     ..

      ..

       ..

        ..

         ..

          ..

           ..

            Reenable all path setting line edit boxes and buttons

::

 # wokifvzohtdlm
             for i in range(self.gridLtNotAdvancedSettings.count()):
                 if self.gridLtNotAdvancedSettings.itemAt(i):
                     self.gridLtNotAdvancedSettings.itemAt(i).widget().setVisible(True)
 # wokifvzohtdlm

..

 ..

  ..

   ..

    ..

     ..

      ..

       ..

        ..

         ..

          ..

           ..

            Hide all advanced mode entries.

::

 # wokifvzohtdlm
             self.lbSphinxEnableAdvMode.setText('<html><head/><body><p>' +
               '<span style="text-decoration: underline;">Switch to Advanced Mode' +
               '</span></p></body></html>')
             self.lbSphinxCmdline.setVisible(False)
             self.leSphinxCmdline.setVisible(False)
             self.lbSphinxReference.setVisible(False)
 
 
 class Plugin(QObject):
     """Plugin interface implementation
     """
     def __init__(self):
         """Create and install the plugin
         """
         QObject.__init__(self)
 
         self._dock = None
         self._saveAction = None
         self._dockInstalled = False
         core.workspace().currentDocumentChanged.connect(self._onDocumentChanged)
         core.workspace().languageChanged.connect(self._onDocumentChanged)
 
 # wokifvzohtdlm

..

 ..

  ..

   ..

    ..

     ..

      ..

       ..

        Install our CodeChat page into the settings dialog.

::

 # wokifvzohtdlm
         core.uiSettingsManager().aboutToExecute.connect(self._onSettingsDialogAboutToExecute)
 # wokifvzohtdlm

..

 ..

  ..

   ..

    ..

     ..

      ..

       ..

        Update preview dock when the settings dialog (which contains the CodeChat
        enable checkbox) is changed.

::

 # wokifvzohtdlm
         core.uiSettingsManager().dialogAccepted.connect(self._onDocumentChanged)
 
 # wokifvzohtdlm

..

 ..

  ..

   ..

    ..

     ..

      ..

       ..

        If user's config .json file lacks it, populate CodeChat's default
        config key and Sphinx's default config key.

::

 # wokifvzohtdlm
         if not 'CodeChat' in core.config():
             core.config()['CodeChat'] = {}
             core.config()['CodeChat']['Enabled'] = False
             core.config().flush()
         if not 'Sphinx' in core.config():
             core.config()['Sphinx'] = {}
             core.config()['Sphinx']['Enabled'] = False
             core.config()['Sphinx']['Executable'] = u'sphinx-build'
             core.config()['Sphinx']['ProjectPath'] = u''
             core.config()['Sphinx']['BuildOnSave'] = False
             core.config()['Sphinx']['OutputPath'] = os.path.join('_build', 'html')
             core.config()['Sphinx']['AdvancedMode'] = False
             core.config()['Sphinx']['Cmdline'] = u'sphinx-build -d ' + os.path.join('_build','doctrees')  \
                                                  + ' . ' + os.path.join('_build','html')
             core.config().flush()
 
     def del_(self):
         """Uninstall the plugin
         """
         if self._dockInstalled:
             self._removeDock()
 
         if self._dock is not None:
             self._dock.del_()
 
     def _onDocumentChanged(self):
         """Document or Language changed.
         Create dock, if necessary
         """
         if self._canPreview(core.workspace().currentDocument()):
             if not self._dockInstalled:
                 self._createDock()
         else:
             if self._dockInstalled:
                 self._removeDock()
 
     def _canPreview(self, document):
         """Check if the given document can be shown in the Preview dock.
         """
         if document is None:
             return False
 
         if document.qutepart.language() in ('Markdown', 'Restructured Text') or \
            isHtmlFile(document):
             return True
 
 # wokifvzohtdlm

..

 ..

  ..

   ..

    ..

     ..

      ..

       ..

        CodeChat can preview a file if it's enabled and if that file's
        extension is supported. Since enki needs to check file extension,
        file path cannot be none.

::

 # wokifvzohtdlm
         if ( CodeChat is not None and core.config()['CodeChat']['Enabled']
              and document.filePath()):
             lso = LSO.LanguageSpecificOptions()
             fileExtension = os.path.splitext(document.filePath())[1]
             if fileExtension in lso.extension_to_options.keys():
                 return True
 # wokifvzohtdlm

..

 ..

  ..

   ..

    ..

     ..

      ..

       ..

        TODO: When to really show the preview dock with Sphinx? That is, how
        can we tell if Sphinx will produce a .html file based on the currently
        open file in the editor? Just checking for a .html file doesn't work;
        perhaps Sphinx hasn't been run or the output files were removed, but
        a run of Sphinx will generate them. Or perhaps Sphinx won't process
        this file (it's excluded, wrong extension, etc.)

::

 # wokifvzohtdlm
         if core.config()['Sphinx']['Enabled'] and document.filePath():
             return True
 
         return False
 
     def _createDock(self):
         """Install dock
         """
 # wokifvzohtdlm

..

 ..

  ..

   ..

    ..

     ..

      ..

       ..

        create dock

::

 # wokifvzohtdlm
         if self._dock is None:
             from enki.plugins.preview.preview import PreviewDock
             self._dock = PreviewDock()
             self._dock.closed.connect(self._onDockClosed)
             self._dock.shown.connect(self._onDockShown)
             self._saveAction = QAction(QIcon(':enkiicons/save.png'), 'Save Preview as HTML', self._dock)
             self._saveAction.setShortcut(QKeySequence("Alt+Shift+P"))
             self._saveAction.triggered.connect(self._dock.onPreviewSave)
 
         core.mainWindow().addDockWidget(Qt.RightDockWidgetArea, self._dock)
 
         core.actionManager().addAction("mView/aPreview", self._dock.showAction())
         core.actionManager().addAction("mFile/aSavePreview", self._saveAction)
         self._dockInstalled = True
         if core.config()['Preview']['Enabled']:
             self._dock.show()
 
     def _onDockClosed(self):
         """Dock has been closed by user. Change Enabled option
         """
         if core.config()['Preview']['Enabled']:
             core.config()['Preview']['Enabled'] = False
             core.config().flush()
 
     def _onDockShown(self):
         """Dock has been shown by user. Change Enabled option
         """
         if not core.config()['Preview']['Enabled']:
             core.config()['Preview']['Enabled'] = True
             core.config().flush()
 
     def _removeDock(self):
         """Remove dock from GUI
         """
         core.actionManager().removeAction("mView/aPreview")
         core.actionManager().removeAction("mFile/aSavePreview")
         core.mainWindow().removeDockWidget(self._dock)
         self._dockInstalled = False
 
     def _onSettingsDialogAboutToExecute(self, dialog):
         """The UI settings dialog is about to execute. Install CodeChat-related
            settings."""
 # wokifvzohtdlm

..

 ..

  ..

   ..

    ..

     ..

      ..

       ..

        First, append the CodeChat settings page to the settings dialog.

::

 # wokifvzohtdlm
         widget = SettingsWidget(dialog)
         dialog.appendPage(u"Literate programming", widget)
 # wokifvzohtdlm

..

 ..

  ..

   ..

    ..

     ..

      ..

       ..

        Next, have the setting UI auto-update the corresponding CodeChat and
        config entries.

::

 # wokifvzohtdlm
         dialog.appendOption(CheckableOption(dialog, core.config(),
                                             "CodeChat/Enabled",
                                             widget.cbCodeChat))
         dialog.appendOption(CheckableOption(dialog, core.config(),
                                             "Sphinx/Enabled",
                                             widget.gbSphinxProject))
         dialog.appendOption(ChoiseOption(dialog, core.config(), "Sphinx/BuildOnSave",
                                          {widget.rbBuildOnlyOnSave: True,
                                           widget.rbBuildOnFileChange: False}))
         dialog.appendOption(TextOption(dialog, core.config(),
                                        "Sphinx/ProjectPath",
                                        widget.leSphinxProjectPath))
         dialog.appendOption(TextOption(dialog, core.config(),
                                        "Sphinx/OutputPath",
                                        widget.leSphinxOutputPath))
         dialog.appendOption(TextOption(dialog, core.config(),
                                        "Sphinx/Executable",
                                        widget.leSphinxExecutable))
         dialog.appendOption(TextOption(dialog, core.config(),
                                        "Sphinx/Cmdline",
                                        widget.leSphinxCmdline))
 
 # wokifvzohtdlm

..

 ..

  ..

   ..

    ..

     ..

      ..

       ..

        Run this after the appendOption calls, since these fields must be set
        up before _updateleValidateSphinxExecutable can run.

::

 # wokifvzohtdlm
         widget._updateleValidateSphinxExecutable()
