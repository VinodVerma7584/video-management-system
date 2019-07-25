# -*- coding: utf-8 -*-
"""
@author: GitHub@Oscarshu0719
"""

from PyQt5 import QtCore, QtWidgets
from core.main_window import Ui_MainWindow
from core.manual_import_window import ManualImportWindow
from core.model import Model
from core.video_player_window import VideoWindow
import os
import re
import sys

# TODO: Components scale up/down while the window zooms in/out.
# TODO: One actress may have many Actress names.
# TODO: arrow_up and arrow_down need to be completed.
# TODO: Video window cannot correctly show after reopen.

class MainForm(QtWidgets.QMainWindow):
    """ Class:
    Control the signals sent from module 'main_frame'.
    """
    
    def __init__(self, parent=None):
        super(MainForm, self).__init__(parent)
        
        # Main window instance.
        self.ui = Ui_MainWindow()
        # Initialize the main window user interface.
        self.ui.setupUi(self)
        
        # Model instance.
        self.mongodb_obj = Model()
        
        # Initialize in advance.
        for i in range(1, 5):
            self._init_all(i)
        
        # Video player instance.
        self.video_window = VideoWindow()

    def search_videos(self):
        """ Slot function: 
        After return is pressed, the text in the textboxes will be send to this 
        function and start searching in the database.
        """
        
        search_video_number = self.ui.text_video_number.text()
        search_video_name = self.ui.text_video_name.text()
        search_actress_name = self.ui.text_actress_name.text()
        search_type = self.ui.text_type.text()
        search_quality = self.ui.combobox_quality.currentText()
        search_quality_ckecked = self.ui.checkbox_quality.isChecked()
        input_text = [search_video_number, search_video_name, 
                      search_actress_name, search_type, 
                      search_quality]
        
        self.ui.statusbar.showMessage('Info: Start searching ...')
        
        search_results = self.mongodb_obj.query(input_text, 
                                                search_quality_ckecked)
        
        self.ui.result_display.clear()
        self._show_result(search_results)
            
        self.ui.statusbar.showMessage('Info: Finish searching ... (Total: ' 
                                      + str(len(search_results)) + ").")
        
    def _init_all(self, option):
        """ Function:
        Initialize the variables which are saved critical data, like list of 
        'No.', set of 'Actress name', set of 'Type', and list of 'Favorite'.
        """
        
        if option == 1:
            """ Case 1:
            No.
            """
            
            # Some video of has 'No' started with '.' or even None 'No', and 
            # both of above are omitted.
            all_result = [col['No'] for col_name in 
                      self.mongodb_obj.database.list_collection_names()
                      for col in self.mongodb_obj.database[col_name].find()
                      if col['No'] != '' and col['No'][0] != '.']
            
            self.all_number = all_result
        elif option == 2:
            """ Case 2:
            Actress name.
            """
            
            all_result = [col['Actress name'] for col_name in 
                      self.mongodb_obj.database.list_collection_names() 
                      for col in self.mongodb_obj.database[col_name].find()
                      if col['Actress name'] != '']
                
            show_result = set()
            for result in all_result:
                show_result.update(result)
            
            # Some of the videos has no 'Actress name', and while listing all
            # 'Actress name', None 'Actress name' is omitted.
            if '' in show_result:
                show_result.remove('')
            
            self.all_actress_name = show_result
        elif option == 3:
            """ Case 3:
            Type.
            """
            
            all_result = [col['Type'] for col_name in 
                      self.mongodb_obj.database.list_collection_names() 
                      for col in self.mongodb_obj.database[col_name].find()
                      if col['Type'] != '']
                
            show_result = set()
            for result in all_result:
                show_result.update(result)
            
            # Some of the videos has no 'Type', and while listing all 'Type', 
            # None 'Type' is omitted.
            if '' in show_result:
                show_result.remove('')
            
            self.all_type = show_result
        elif option == 4:
            """ Case 4:
            Favorite.
            """
            
            all_result = [col for col_name in 
                          self.mongodb_obj.database.list_collection_names() 
                          for col in self.mongodb_obj.database[col_name].find()
                          if col['Favorite']]
                
            self.all_favorite = all_result
        
    def show_all(self, option):
        """ Slot function:
        The three cases below are corresponding to the three buttons 'Show
        No.', 'Show actresses', 'Show types', and 'Show favorites'.
        """
        
        self._init_all(option)
        self.ui.result_display.clear()
        
        if option == 1:
            """ Case 1:
            No.
            """
            
            for result in self.all_number:
                self.ui.result_display.addItem(result)
            
            msg = "Info: Show all 'No.' (Total: " 
            msg += str(len(self.all_number)) + ")."
            self.ui.statusbar.showMessage(msg)
        elif option == 2:
            """ Case 2:
            Actress name.
            """
            
            for result in self.all_actress_name:
                self.ui.result_display.addItem(result)
                
            msg = "Info: Show all 'Actress name' (Total: "
            msg += str(len(self.all_actress_name)) + ")."
            self.ui.statusbar.showMessage(msg)
        elif option == 3:
            """ Case 3:
            Type.
            """
            
            for result in self.all_type:
                self.ui.result_display.addItem(result)
            
            msg = "Info: Show all 'Type' (Total: "
            msg += str(len(self.all_type)) + ")."
            self.ui.statusbar.showMessage(msg)
        elif option == 4:
            """ Case 4:
            Favorite.
            """
            
            self._show_result(self.all_favorite)
                
            msg = "Info: Show all 'Favorite' (Total: "
            msg += str(len(self.all_favorite))  + ")."
            self.ui.statusbar.showMessage(msg)
    
    def _show_result(self, search_results):
        """ Function:
        Output the full name of each item.
        """
        
        for result in search_results:
            text = result['No'] + '_' + result['Video name'] + '_'
            if len(result['Actress name']) > 1:
                text += ', '.join(result['Actress name'])
            elif len(result['Actress name']) == 1:
                text += result['Actress name'][0]
            text += '_'
            if len(result['Type']) > 1:
                text += ', '.join(result['Type'])
            elif len(result['Type']) == 1:
                text += result['Type'][0]
            text += ('_' + result['Quality'])
            
            self.ui.result_display.addItem(text)
            
    def item_double_clicked(self, selected_item):
        """ Slot function:
        The actions after double-clicked an item.
        If the action is to play a video, the hidden video player window will 
        show.
        After the user closing the video player window, it doesn't exactly 
        close, but just hide.
        """
        
        text = selected_item.text()
        if text in self.all_actress_name:
            """
            Actress name. 
            Show all videos about the clicked actress.
            """
            
            search_results = self.mongodb_obj.query(['', '', text, '', ''], 0)
            
            self.ui.result_display.clear()
            self._show_result(search_results)
            
            self.ui.statusbar.showMessage("Info: Videos about Actress '" 
                                          + text + "' ..." + 
                                          ' (Total: ' + str(len(search_results)) 
                                          + ").")
            
        elif text in self.all_type:
            """
            Type. 
            Show all videos about the clicked type.
            """
            
            search_results = self.mongodb_obj.query(['', '', '', text, ''], 0)
            
            self.ui.result_display.clear()
            self._show_result(search_results)
            
            self.ui.statusbar.showMessage("Info: Videos about Type '" 
                                          + text + "' ..." + 
                                          ' (Total: ' + str(len(search_results))
                                          + ").")
        else:
            """
            No. and Full name. 
            Play the video.
            """
            
            self.video_window.show()
            option = self._classifier(text)
            
            if option == 1:
                """
                No.
                """
                
                video = self.mongodb_obj.database[text].find_one()
            elif option != text:
                """
                Full name with common No..
                """
                
                video = self.mongodb_obj.database[option].find_one()
            else:
                """
                Full name with specific No. like '' and '.CD1'.
                """
                
                result = self.mongodb_obj.specific_query(text)
                video = self.mongodb_obj.database[result].find_one()
                
            self.video_window.double_clicked_play_video(video['Location'] + '/'
                                                        + video['_id'])

    def setup_favorite(self, selected_item, flag):
        """ Slot function:
        The slot function of 'Add to Favorite' and 'Remove from Favorite'.
        'Add to Favorite': Add the selected item to favorite.
        'Remove from Favorite': Remove the selected item from favorite.
        Notice that if the selected item is 'Actress name', all of the videos 
        that the 'Actress name' act will be added to or removed from favorite.
        """
        
        option = self._classifier(selected_item)
        
        if option == 1:
            """
            No.
            """
            
            self.mongodb_obj.add_to_remove_from_favorite(selected_item, 1, flag)
        elif selected_item in self.all_actress_name:
            """
            Actress name.
            """
            
            self.mongodb_obj.add_to_remove_from_favorite(selected_item, 2, flag)
        elif option != selected_item:
            """
            Full name with common No..
            """
            
            self.mongodb_obj.add_to_remove_from_favorite(option, 3, flag)
        else:
            """
            Full name with specific No. like '' and '.CD1'.
            """
            
            self.mongodb_obj.add_to_remove_from_favorite(selected_item, 4, flag)
            
    def _classifier(self, text):
        """ Function:
        Classify the selected item to continue to the next-step operation.
        If the selected item matches full name of a video, then check if the  
        'No.' of the video is common or specific, if the 'No.' is common,  
        return the 'No.', if the 'No.' is specific, return the text of selected 
        item.
        If the selected item matches 'No.', return 1.
        """
        
        pattern_full_name = re.compile(r'(.*)_(.*)_.*_.*_.*')
        pattern_number = re.compile(r'([a-zA-Z\d\-\.]+)')
        
        match_full_name = pattern_full_name.match(text)
        match_number = pattern_number.match(text)
        
        if match_full_name:
            if match_full_name.group(1) == '' or match_full_name.group(1)[0] == '.':
                return match_full_name.group(0)
            else:
                return match_full_name.group(1)
        elif match_number:
            return 1
        
    def import_data(self, option):
        """ Slot function:
        The slot function of 'Batch import' and 'Manual import'.
        'Batch import': Select a folder, and all videos under the folder will 
        be imported.
        'Manual import': Select a video, and the user can modify each data.
        Notice that the input data will NOT append, but overwrite the old data.
        """
        
        if option:
            folder = QtWidgets.QFileDialog.getExistingDirectory(
                    self, "Select folder", QtCore.QDir.homePath())
            if folder != '':
                if not os.path.isdir('data'):
                    os.mkdir('data')
                output_path = 'data\\' + folder[folder.rfind('/') + 1:] + '.log'
                
                with open(output_path, 'w', encoding='utf8') as output_file:
                    for dir_path, dir_name, filename in os.walk(folder):
                        for file in filename:
                            output_file.write(file + '\n')
                
                check_succeeded, check_failed = self.mongodb_obj.import_batch(folder)
                
                if not check_failed:
                    self.ui.statusbar.showMessage(
                            'Info: Import successfully (Total: {}).'.format(check_succeeded))
                else:
                    self.ui.statusbar.showMessage(
                            'Error: Import failed (Successful: {}, Failed: {}).'.format(check_succeeded, check_failed))
        else:
            manual_import_window.show()
            
    def show_all_videos(self):
        """ Slot function.
        The slot function of 'Show all'.
        'Show all': Show all videos in the database.
        """
        search_results = self.mongodb_obj.show_all_videos()
        
        self.ui.result_display.clear()
        self._show_result(search_results)
            
        self.ui.statusbar.showMessage('Info: Finish searching ... (Total: ' 
                                      + str(len(search_results)) + ").")
    
    def drop_database(self):
        """ Slot function.
        The slot function of 'Drop'.
        'Drop': Drop the database.
        """
        
        self.mongodb_obj.client.drop_database(self.mongodb_obj.DB_NAME)
        self.ui.statusbar.showMessage("Info: 'Drop' successfully.")
            
class ImportWindow(QtWidgets.QMainWindow):
    """ Class:
    Control the signal from module 'manual_import_window'.
    """
    
    def __init__(self, parent=None):
        super(ImportWindow, self).__init__(parent)
        
        # Manual import window instance.
        self.ui = ManualImportWindow()
        # Initialize manual import window.
        self.ui.setupUi(self)
        
        # Model instance.
        self.mongodb_obj = Model()
    
    def import_video(self):
        """ Slot function:
        The slot function of button 'Enter'.
        'Enter': Try to import the video to the database.
        """
        
        import_number = self.ui.text_number.text()
        import_video_name = self.ui.text_video_name.text()
        import_actress_name = self.ui.text_actress_name.toPlainText().split(', ')
        import_favorite = self.ui.checkbox_favorite.isChecked()
        import_type = self.ui.text_type.toPlainText().split(', ')
        import_quality = self.ui.combobox_quality.currentText()
        import_location = self.ui.text_location.toPlainText().split(';; ')

        success = 0
        failed = 0
        error_list = list()
        for loc in import_location:
            check_correct = self.mongodb_obj.import_manual([import_number, 
                import_video_name, import_actress_name, import_favorite, 
                import_type, import_quality, loc])
            
            if not check_correct:
                error = list()
                error.append(import_number)
                error.append(import_video_name)
                error.append(import_actress_name)
                error.append(import_favorite)
                error.append(import_type)
                error.append(import_quality)
                error.append(loc)
                error_list.append(error)
                failed += 1
            else:
                success += 1
                
        keys = ['No', 'Video name', 'Actress name', 'Favorite', 'Type', 
                'Quality', 'Location']
        with open(Model.IMPORT_ERROR_LOG_PATH, 'a', encoding='utf8') as error_output:
            for error_record in error_list:
                error_output.write('Warning: Failed to import: \n')
                error_output.write('--------------------------------------------------')
                error_output.write('--------------------------------------------------\n')
                for i in range(7):
                    error_output.write(keys[i] + ': ' + str(error_record[i]) + '\n')
                error_output.write('--------------------------------------------------')
                error_output.write('--------------------------------------------------\n')
            
        self.ui.statusbar.showMessage("Info: Import successfully (Total: {}, Successful: {}, Failed: {}).".format(
                success + failed, success, failed))
        self.ui.text_location.clear()

if __name__ == "__main__":
    """
    Program entrance.
    """
    
    """
    app = QApplication(sys.argv) will go wrong.
    """
    app = QtCore.QCoreApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)

    main_window = MainForm()
    main_window.show()
    
    manual_import_window = ImportWindow()
    
    """
    sys.exit(app.exec_()) will go wrong.
    """
    app.exec_()