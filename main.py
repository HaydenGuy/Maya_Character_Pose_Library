import sys
import importlib
import json
import maya.cmds as cmds

'''
    Calls the path to the root directory so Maya can access files in the directory
    Replace this with your own directory path
'''
sys.path.append('/mnt/185EB3E65EB3BAB8/Maya_Scripts/Virtual_Environment/Character_Pose_Library')

from PySide2.QtWidgets import QMainWindow, QApplication, QFileDialog
from PySide2.QtCore import QStringListModel
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
        
        # Initalize a dictionary of poses
        self.poses = {}

        # Creates the list model that allows the list data to be displayed and manipulated
        self.list_model = QStringListModel()
        self.listView.setModel(self.list_model)

        # The signals for the UI buttons
        self.pb_save.clicked.connect(self.pose_save)
        self.pb_recall.clicked.connect(self.pose_recall)
        self.pb_delete.clicked.connect(self.pose_delete)

        # The signals for the File menu bar items
        self.actionNew.triggered.connect(self.new_file)
        # self.actionOpen.triggered.connect(self.open_file)
        # self.actionSave.triggered.connect(self.save_file)
        self.actionSave_As.triggered.connect(self.save_as_file)
        self.actionQuit.triggered.connect(self.quit_file)

    def pose_save(self):
        # Sets the pose name to the text in the line edit
        pose_name = self.pose_name_input.text()

        # Get the first selected object's name
        object_name = cmds.ls(selection=True)[0]
        
        # Get translation, rotation, and scale attributes of the object
        translation = cmds.getAttr(f'{object_name}.translate')[0]
        rotation = cmds.getAttr(f'{object_name}.rotate')[0]
        scale = cmds.getAttr(f'{object_name}.scale')[0]

        '''
            If the pose name isn't in the poses dictionary
            Creates a new entry to the dictionary key=pose_name, value=pose_data
            Adds the pose_name to the list_model in the listView
        '''
        if pose_name not in self.poses:
            pose_data = {'Translate': translation,
                        'Rotation': rotation,
                        'Scale': scale
                        }
            self.poses[pose_name] = pose_data

            list_items = self.list_model.stringList()
            list_items.append(pose_name)
            self.list_model.setStringList(list_items)
    
    def pose_recall(self):
        # Retrieves data about the currently selected item in the list
        selected_list_indexes = self.listView.selectedIndexes()
        selected_list_item = selected_list_indexes[0].data()

        # Get the first selected object's name
        object_name = cmds.ls(selection=True)[0]

        # Extracts the translation, rotation, and scale data from the poses dictionary based on the list item selected
        translation = self.poses[selected_list_item]['Translate']
        rotation = self.poses[selected_list_item]['Rotation']
        scale = self.poses[selected_list_item]['Scale']

        # Set translation, rotation, and scale attributes of the selected object by calling the poses dictionary values
        cmds.setAttr(f'{object_name}.translate', translation[0], translation[1], translation[2], type='double3')
        cmds.setAttr(f'{object_name}.rotate', rotation[0], rotation[1], rotation[2], type='double3')
        cmds.setAttr(f'{object_name}.scale', scale[0], scale[1], scale[2], type='double3')

    def pose_delete(self):
        # Retrieves data about the currently selected item in the list
        selected_list_indexes = self.listView.selectedIndexes()
        selected_list_item = selected_list_indexes[0].data()

        # Remove the pose data from the dictionary and update the list model
        if selected_list_item in self.poses:
            del self.poses[selected_list_item]
            list_items = self.list_model.stringList()
            list_items.remove(selected_list_item)
            self.list_model.setStringList(list_items)
        
    # Resets the UI by clearing all the stored data
    def new_file(self):
        self.pose_name_input.clear()
        self.poses = {}
        self.list_model.setStringList([])

    # Saves the file to a new file
    def save_as_file(self):
        # Uses QFileDialog to open a save dialog box
        file_path, _ = QFileDialog.getSaveFileName(self, 'Save Pose As', '', 'Text File (*.txt)')
        
        '''
            If a file path exists
            with: manages file state, ensures it closes correctly
            open() the file indicated by file path in 'w' write mode
            as f: giving the opened file the nickname f
            json.dump(): taking the data from self.poses and coverts into readable file
        '''
        if file_path:
            with open(file_path, 'w') as f:
                json.dump(self.poses, f)

    # Closes the Character Pose Library window
    def quit_file(self):
        self.close()

if __name__ == '__main__':
    # Create a Qt application instance or use the existing one
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    
    # Create and show the UI window
    window = LibraryWindow()    
    window.show()
