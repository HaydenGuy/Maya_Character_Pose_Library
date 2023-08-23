import sys
import json
import maya.cmds as cmds
import maya.OpenMaya as om

'''
    Calls the path to the root directory so Maya can access files in the directory
    Replace this with your own directory path
'''
sys.path.append('/mnt/32346261-2a77-4ea4-ad97-df46c23e0f72/Maya_Scripts/Character_Pose_Library')

from PySide2.QtWidgets import QMainWindow, QApplication, QFileDialog
from PySide2.QtCore import QStringListModel
import UI.Ui_Character_Pose_Library  # Import the entire module

class LibraryWindow(QMainWindow, UI.Ui_Character_Pose_Library.Ui_library_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # Initalize a dictionary of poses
        self.poses = {}

        # Creates a current file variable to monitor the currently open file
        self.current_file = 'new'

        # Creates the list model that allows the list data to be displayed and manipulated
        self.list_model = QStringListModel()
        self.listView.setModel(self.list_model)

        # The signals for the UI buttons
        self.pb_save.clicked.connect(self.pose_save)
        self.pb_recall.clicked.connect(self.pose_recall)
        self.pb_delete.clicked.connect(self.pose_delete)

        # The signals for the File menu bar items
        self.actionNew.triggered.connect(self.new_file)
        self.actionOpen.triggered.connect(self.open_file)
        self.actionSave.triggered.connect(self.save_file)
        self.actionSave_As.triggered.connect(self.save_as_file)
        self.actionQuit.triggered.connect(self.quit_file)

    # Gets the transforms of the root object and returns the transforms dictionary
    def get_object_transforms(self, root_object):
        transforms = {}

        # Adds the children of root objects transforms to the transforms dictionary
        def recursive_get_transforms(obj):
            # Get translation, rotation, and scale attributes of the object
            translation = cmds.getAttr(f'{obj}.translate')[0]
            rotation = cmds.getAttr(f'{obj}.rotate')[0]
            scale = cmds.getAttr(f'{obj}.scale')[0]
            
            # Store the transformation data in the transforms dictionary
            transforms[obj] = {'Translate': translation, 'Rotation': rotation, 'Scale': scale}

            # Get children of the current object
            children = cmds.listRelatives(obj, children=True, type='transform') or []
            for child in children:
                # Recursively call the function for each child
                recursive_get_transforms(child)

        recursive_get_transforms(root_object)
        return transforms
    
    # Saves the pose name and data when the button is pressed
    def pose_save(self):
        # Sets the pose name to the text in the line edit
        pose_name = self.pose_name_input.text()

        # Raises a warning if trying to save without a name
        if pose_name == '':
            om.MGlobal.displayWarning('Please enter a name')
            return

        # Raises a warning if the pose name already exists
        if pose_name in self.poses:
            om.MGlobal.displayWarning('Pose name already exists')
            return

        # Get the currently selected object
        selected_object = cmds.ls(selection=True, type='transform')

        if selected_object:
            # Take the first selected object as the root object
            root_object = selected_object[0]

            # Call the method to get transforms of the entire hierarchy under the root object
            object_transforms = self.get_object_transforms(root_object)

            # Store the rig transforms in the poses dictionary
            self.poses[pose_name] = object_transforms

        # Update the list model
        list_items = self.list_model.stringList()
        list_items.append(pose_name)
        self.list_model.setStringList(list_items)

    # Recalls the pose data of the selected list pose
    def pose_recall(self):
        # Get the indexes of the selected items in the list view
        selected_list_indexes = self.listView.selectedIndexes()
        # Get the pose name (data) of the first selected item
        selected_list_item = selected_list_indexes[0].data()

        # Check if the selected pose name is present in the 'poses' dictionary
        if selected_list_item in self.poses:
            # Get the pose data (transforms) for the selected pose name
            pose_data = self.poses[selected_list_item]

            # Loop through each object's data in the pose data
            for object_name, object_data in pose_data.items():
                # Check if the object still exists in the scene and retrieve transform data
                if cmds.objExists(object_name):
                    translation = object_data['Translate']
                    rotation = object_data['Rotation']
                    scale = object_data['Scale']

                    # Check if translation attributes are locked and set if not
                    if not cmds.getAttr(f'{object_name}.translateX', lock=True):
                        cmds.setAttr(f'{object_name}.translateX', translation[0])
                    if not cmds.getAttr(f'{object_name}.translateY', lock=True):
                        cmds.setAttr(f'{object_name}.translateY', translation[1])
                    if not cmds.getAttr(f'{object_name}.translateZ', lock=True):
                        cmds.setAttr(f'{object_name}.translateZ', translation[2])
                    
                    # Check if rotation attributes are locked and set if not
                    if not cmds.getAttr(f'{object_name}.rotateX', lock=True):
                        cmds.setAttr(f'{object_name}.rotateX', rotation[0])
                    if not cmds.getAttr(f'{object_name}.rotateY', lock=True):
                        cmds.setAttr(f'{object_name}.rotateY', rotation[1])
                    if not cmds.getAttr(f'{object_name}.rotateZ', lock=True):
                        cmds.setAttr(f'{object_name}.rotateZ', rotation[2])

                    # Check if scale attributes are not locked and not connected, then set
                    if not cmds.getAttr(f'{object_name}.scaleX', lock=True) and not cmds.listConnections(f'{object_name}.scaleX'):
                        cmds.setAttr(f'{object_name}.scaleX', scale[0])
                    if not cmds.getAttr(f'{object_name}.scaleY', lock=True) and not cmds.listConnections(f'{object_name}.scaleY'):
                        cmds.setAttr(f'{object_name}.scaleY', scale[1])
                    if not cmds.getAttr(f'{object_name}.scaleZ', lock=True) and not cmds.listConnections(f'{object_name}.scaleZ'):
                        cmds.setAttr(f'{object_name}.scaleZ', scale[2])

    # Deletes the selected pose from the list
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
        self.current_file = 'new'
        self.setWindowTitle('Character Pose Library - new')
        self.pose_name_input.clear()
        self.poses = {}
        self.list_model.setStringList([])

    # Opens an existing file
    def open_file(self):
        # Uses QFileDialog to open a save dialog box
        file_path, _ = QFileDialog.getOpenFileName(self, 'Open file', '')

        '''
            If a file path is given (i.e. open a file)
            Clear all the UI data stored so its not adding on top of existing
            Call the get file name function
            with: manages file state, ensures it closes correctly
            open() the file indicated by file path in 'r' read mode
            as f: giving the opened file the nickname f
            Assign self.poses dictionary the data from the loaded file
        '''
        if file_path:
            self.pose_name_input.clear()
            self.poses = {}
            self.list_model.setStringList([])
            self.get_file_name(file_path)

            with open(file_path, 'r') as f:
                self.poses = json.load(f)

                # Updates the list view by looping an append over each item in the poses dict
                list_items = self.list_model.stringList()
                for pose_name in self.poses:
                    list_items.append(pose_name)
                self.list_model.setStringList(list_items)

    # Saves the current file, runs save as if the current file is 'new'
    def save_file(self):
        if self.current_file == 'new':
            self.save_as_file()
        else:
            '''
            with: manages file state, ensures it closes correctly
            open() the file indicated by file path in 'w' write mode
            as f: giving the opened file the nickname f
            json.dump(): taking the data from self.poses and coverts into readable file
            '''
            with open(self.current_file, 'w') as f:
                json.dump(self.poses, f)
        
    # Saves the file to a new file
    def save_as_file(self):
        # Uses QFileDialog to open a save dialog box
        file_path, _ = QFileDialog.getSaveFileName(self, 'Save Pose As', '')

        '''
            If a file path is given (i.e. a save happens)
            Call the get file name function 
            with: manages file state, ensures it closes correctly
            open() the file indicated by file path in 'w' write mode
            as f: giving the opened file the nickname f
            json.dump(): taking the data from self.poses and coverts into readable file
        '''
        if file_path:
            self.get_file_name(file_path)

            with open(file_path, 'w') as f:
                json.dump(self.poses, f)

    # Gets the file name of the open/saved file by passing a file path
    def get_file_name(self, file_path):
        '''
            Extract the file name from file path
            If the file path contains a / it splits it and extracts the last part (the file name)
            If no / it assigns the file name as the file path
            Updates the window title to be the name of the newly named file
            Updates the current file variable to be the file name
        '''
        file_name = file_path.split('/')[-1] if '/' in file_path else file_path
        self.setWindowTitle(f'Character Pose Library - {file_name}')
        self.current_file = file_name

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
