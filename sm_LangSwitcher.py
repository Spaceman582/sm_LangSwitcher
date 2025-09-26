try:
    from PySide2 import QtCore, QtWidgets
except:
    from PySide6 import QtCore, QtWidgets
import shiboken2
import ctypes
import os
import logging
import maya.OpenMayaMPx as OpenMayaMPx


lang_switcher = None
kPluginCmdName = "sm_LangSwitcher"

class LangSwitcherClass(OpenMayaMPx.MPxCommand):
    def __init__(self):
        OpenMayaMPx.MPxCommand.__init__(self)

    def doIt(self, args):
        global lang_switcher
        if lang_switcher == None:
            lang_switcher = LangSwitcher()
        lang_switcher.start()

def cmdCreator():
    return OpenMayaMPx.asMPxPtr(LangSwitcherClass())

def initializePlugin(mobject):
    global lang_switcher
    mplugin = OpenMayaMPx.MFnPlugin(mobject, "SpaceMan", "1.0", "Any")
    try:
        mplugin.registerCommand(kPluginCmdName, cmdCreator)
        lang_switcher = LangSwitcher()
        lang_switcher.start()
    except Exception as e:
        raise RuntimeError(f"Failed to register command {kPluginCmdName}: {e}")

def uninitializePlugin(mobject):
    global lang_switcher
    mplugin = OpenMayaMPx.MFnPlugin(mobject)
    try:
        mplugin.deregisterCommand(kPluginCmdName)
        if lang_switcher is not None:
            lang_switcher.pause()
            lang_switcher = None
    except Exception as e:
        raise RuntimeError(f"Failed to unregister command {kPluginCmdName}: {e}")


class LangSwitcher(QtCore.QObject):
    ENGLISH = 0x409  # LANG_ID en-US
    def __init__(self, parent=None):
        super(LangSwitcher, self).__init__(parent)
        #Logging
        self.logger = logging.getLogger("LangAutoSwitch")
        self.logger.setLevel(logging.INFO)
        self.logger.info("Initialized and started")
        #eventFilter setup
        self.install_app_filter()
        #OS API
        self.user32 = ctypes.WinDLL("user32", use_last_error=True)
        #self.kernel32 = ctypes.windll.kernel32 #Linux
        self.WM_INPUTLANGCHANGEREQUEST = 0x0050
        self.INPUTLANGCHANGE_FORWARD = 0x0002
        #Lang vars
        self.saved_layout = None
        self.enabled = True
        self.native_lang = self._get_current_layout()
        self.unfocused_lang = self.native_lang
        
     # === Controll ===
    def start(self):
        if not self.enabled:
            self.enabled = True
            self.logger.info("Started")
        else:
            self.logger.info("Already started")

    def pause(self):
        if self.enabled:
            self.enabled = False
            # return lang if changed
            if self.saved_layout:
                self._set_layout(self.saved_layout)
                self.saved_layout = None
            self.logger.info("Stopped")
    
    def debug(self):
        self.logger.setLevel(logging.DEBUG)
        self.logger.info("Debug logging started")
        
    def info():
        self.logger.setLevel(logging.INFO)
        self.logger.info("Returned to normal logging mode")        
        
    def __del__(self):
        self.enabled = False
        self.saved_layout = None
        self.logger.info("Deleted")
            
    # === Lang Switch ===
    def _get_current_layout(self):
        hkl = self.user32.GetKeyboardLayout(0)
        return hkl & 0xFFFF

    def _set_layout(self, lang_id):
        # Get foreground window
        hwnd = self.user32.GetForegroundWindow()
        if not hwnd:
            return False

        # Load lang layout
        layout_hex = f"{lang_id:08x}"
        hkl = self.user32.LoadKeyboardLayoutW(layout_hex, 1)
        if not hkl:
            raise ctypes.WinError(ctypes.get_last_error())

        # Send msg to active window
        res = self.user32.PostMessageW(hwnd, self.WM_INPUTLANGCHANGEREQUEST, self.INPUTLANGCHANGE_FORWARD, hkl)
        if not res:
            raise ctypes.WinError(ctypes.get_last_error())
        return True

    # === Window focus trigger ===
    def install_app_filter(self):
        self.app = QtWidgets.QApplication.instance()
        if self.app:
            self.app.installEventFilter(self)
            self.logger.debug("Event filter installed on QApplication")


    def eventFilter(self, obj, event):
        current_lang = self._get_current_layout()
        if obj == QtWidgets.QApplication.instance():
            if event.type() == QtCore.QEvent.ApplicationActivate:
                self.logger.debug("Maya window gained focus")
                self.unfocused_lang = self._get_current_layout()
                if current_lang != self.ENGLISH:
                    self.native_lang = self._get_current_layout()
                    self._set_layout(self.ENGLISH)
                    self.logger.debug("Focused - switched to EN")
            elif event.type() == QtCore.QEvent.ApplicationDeactivate:
                self.logger.debug("Maya window lost focus")
                if self.unfocused_lang != self.ENGLISH:
                    if self.native_lang != self.ENGLISH:
                        self._set_layout(self.native_lang)
                        self.logger.debug("Unfocused - restored previous layout")
                    
        return super(LangSwitcher, self).eventFilter(obj, event)

LangSwitcherClass()

