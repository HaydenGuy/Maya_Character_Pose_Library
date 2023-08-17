import sys
import importlib
import maya.cmds as cmds

'''
    Calls the path to the root directory so Maya can access files in the directory
    Replace this with your own directory path
'''
sys.path.append('/mnt/185EB3E65EB3BAB8/Maya_Scripts/Virtual_Environment/Character_Pose_Library')

from PySide2.QtWidgets import QMainWindow, QApplication
import UI.Ui_Character_Pose_Library  # Import the entire module

def reload_module(module_name):
    # Reloads a module if it's already in sys.modules
    if module_name in sys.modules:
        importlib.reload(sys.modules[module_name])

# Reload the UI module before anything else
module_name = 'UI.Ui_Character_Pose_Library'    
reload_module(module_name)


class LibraryWindow(QMainWindow, UI.Ui_Character_Pose_Library.Ui_library_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # Connect button clicks to functions
        self.pb_save.clicked.connect(self.pose_save)
        self.pb_recall.clicked.connect(self.pose_recall)

    def pose_save(self):
        # Get the first selected object's name
        object_name = cmds.ls(selection=True)[0]
        
        # Get translation, rotation, and scale attributes of the object
        self.translation = cmds.getAttr(f'{object_name}.translate')[0]
        self.rotation = cmds.getAttr(f'{object_name}.rotate')[0]
        self.scale = cmds.getAttr(f'{object_name}.scale')[0]

        return self.translation, self.rotation, self.scale
    
    def pose_recall(self):
        # Get the first selected object's name
        object_name = cmds.ls(selection=True)[0]
        
        # Set translation, rotation, and scale attributes of the object       
        cmds.setAttr(f'{object_name}.translate', self.translation[0], self.translation[1], self.translation[2], type='double3')
        cmds.setAttr(f'{object_name}.rotate', self.rotation[0], self.rotation[1], self.rotation[2], type='double3')
        cmds.setAttr(f'{object_name}.scale', self.scale[0], self.scale[1], self.scale[2], type='double3')


if __name__ == '__main__':
    # Create a Qt application instance or use the existing one
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    
    # Create and show the UI window
    window = LibraryWindow()    
    window.show()
