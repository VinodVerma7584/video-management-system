# -*- coding: utf-8 -*-
"""
@author: GitHub@Oscarshu0719
"""

from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_MainWindow(QtCore.QObject):
    """ Class:
    Main window.
    """
    
    # Main window size.
    WIN_SIZE = [800, 600]
    # Path used to save the log.
    SAVE_LOG_PATH = r"save\results.log"
    # Main window icon path.
    WIN_ICON_PATH = r"conf\video_128px_1223561_easyicon.net.ico"
    # Messagebox icon path
    MSG_BOX_ICON_PATH = r"conf\database_128px_1229683.ico"
    # Self-defined signal which is used to drop the database.
    signal_drop_database = QtCore.pyqtSignal()
    
    def setupUi(self, MainWindow):
        """ Function:
        Setup user interface of main window.
        """
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(Ui_MainWindow.WIN_SIZE[0], Ui_MainWindow.WIN_SIZE[1])
        MainWindow.setWindowIcon(QtGui.QIcon(Ui_MainWindow.WIN_ICON_PATH))
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 781, 32))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.label_video_number = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_video_number.setObjectName("label_video_number")
        self.horizontalLayout.addWidget(self.label_video_number)
        self.text_video_number = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.text_video_number.setObjectName("text_video_number")
        self.horizontalLayout.addWidget(self.text_video_number)
        self.label_video_name = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_video_name.setObjectName("label_video_name")
        self.horizontalLayout.addWidget(self.label_video_name)
        self.text_video_name = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.text_video_name.setObjectName("text_video_name")
        self.horizontalLayout.addWidget(self.text_video_name)
        self.label_actress_name = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_actress_name.setObjectName("label_actress_name")
        self.horizontalLayout.addWidget(self.label_actress_name)
        self.text_actress_name = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.text_actress_name.setObjectName("text_actress_name")
        self.horizontalLayout.addWidget(self.text_actress_name)
        self.label_type = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_type.setObjectName("label_type")
        self.horizontalLayout.addWidget(self.label_type)
        self.text_type = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.text_type.setObjectName("text_type")
        self.horizontalLayout.addWidget(self.text_type)
        self.label_quality = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_quality.setObjectName("label_quality")
        self.horizontalLayout.addWidget(self.label_quality)
        self.checkbox_quality = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkbox_quality.setText("")
        self.checkbox_quality.setObjectName("checkbox_quality")
        self.horizontalLayout.addWidget(self.checkbox_quality)
        self.combobox_quality = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.combobox_quality.setObjectName("combobox_quality")
        self.combobox_quality.addItem("")
        self.combobox_quality.addItem("")
        self.combobox_quality.addItem("")
        self.combobox_quality.addItem("")
        self.horizontalLayout.addWidget(self.combobox_quality)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.result_display = QtWidgets.QListWidget(self.centralwidget)
        self.result_display.setGeometry(QtCore.QRect(10, 50, 781, 451))
        self.result_display.setObjectName("result_display")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(9, 510, 501, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        
        self.button_show_number = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.button_show_number.setObjectName("button_show_number")
        self.horizontalLayout_3.addWidget(self.button_show_number)
        self.button_show_actresses = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.button_show_actresses.setObjectName("button_show_actresses")
        self.horizontalLayout_3.addWidget(self.button_show_actresses)
        self.button_show_types = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.button_show_types.setObjectName("button_show_types")
        self.horizontalLayout_3.addWidget(self.button_show_types)
        self.button_show_favorite = QtWidgets.QPushButton(self.centralwidget)
        self.button_show_favorite.setGeometry(QtCore.QRect(520, 510, 271, 28))
        self.button_show_favorite.setObjectName("button_show_favorite")
        self.horizontalLayoutWidget.raise_()
        self.result_display.raise_()
        self.horizontalLayoutWidget_2.raise_()
        self.button_show_favorite.raise_()
        self.button_show_favorite.raise_()
        self.result_display.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.result_display.customContextMenuRequested.connect(self.right_click_menu)
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuitem_menu = QtWidgets.QMenu(self.menubar)
        self.menuitem_menu.setObjectName("menuitem_menu")
        self.menu_save_log = QtWidgets.QMenu(self.menuitem_menu)
        self.menu_save_log.setObjectName("menu_save_log")
        self.menu_import = QtWidgets.QMenu(self.menuitem_menu)
        self.menu_import.setObjectName("menu_import")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_batch_import = QtWidgets.QAction(MainWindow)
        self.action_batch_import.setObjectName("action_batch_import")
        self.action_batch_import.setStatusTip("Batch import data.")
        self.action_manual_import = QtWidgets.QAction(MainWindow)
        self.action_manual_import.setObjectName("action_manual_import")
        self.action_manual_import.setStatusTip("Manually import data.")
        self.menu_import.addAction(self.action_batch_import)
        self.menu_import.addAction(self.action_manual_import)
        self.action_show_all = QtWidgets.QAction(MainWindow)
        self.action_show_all.setObjectName("action_show_all")
        self.action_show_all.setStatusTip("Show all videos.")
        self.menuitem_menu.addAction(self.action_show_all)
        self.action_append = QtWidgets.QAction(MainWindow)
        self.action_append.setObjectName("action_append")
        self.action_append.setStatusTip("Save old and new results in {}.".format(
                Ui_MainWindow.SAVE_LOG_PATH))
        self.action_new = QtWidgets.QAction(MainWindow)
        self.action_new.setObjectName("action_new")
        self.action_new.setStatusTip("Only save new results from selected file.")
        self.menu_save_log.addAction(self.action_append)
        self.menu_save_log.addAction(self.action_new)
        self.action_clear_log = QtWidgets.QAction(MainWindow)
        self.action_clear_log.setObjectName("action_clear_log")
        self.action_clear_log.setStatusTip("Clear the searching results.")
        self.action_sort = QtWidgets.QAction(MainWindow)
        self.action_sort.setObjectName("action_sort")
        self.action_sort.setStatusTip("Sort the results in ascending order.")
        self.action_drop_database = QtWidgets.QAction(MainWindow)
        self.action_drop_database.setObjectName("action_drop_database")
        self.action_drop_database.setStatusTip("Drop database.")
        self.menuitem_menu.addAction(self.menu_import.menuAction())
        self.menuitem_menu.addAction(self.menu_save_log.menuAction())
        self.menuitem_menu.addAction(self.action_clear_log)
        self.menuitem_menu.addAction(self.action_sort)
        self.menuitem_menu.addAction(self.action_drop_database)
        self.menubar.addAction(self.menuitem_menu.menuAction())
        self.menubar.triggered[QtWidgets.QAction].connect(self.menubar_action)
        self.right_menu = QtWidgets.QMenu()
        self.action_copy = self.right_menu.addAction(u"Copy")
        self.action_add_to_favorite = self.right_menu.addAction(u"Add to Favorite")
        self.action_remove_from_favorite = self.right_menu.addAction(u"Remove from Favorite")
        
        self.retranslateUi(MainWindow)
        
        # Connect to slot functions.
        self.button_show_number.clicked.connect(lambda: MainWindow.show_all(1))
        self.button_show_actresses.clicked.connect(lambda: MainWindow.show_all(2))
        self.button_show_types.clicked.connect(lambda: MainWindow.show_all(3))
        self.button_show_favorite.clicked.connect(lambda: MainWindow.show_all(4))
        self.text_video_number.returnPressed.connect(MainWindow.search_videos)
        self.text_video_name.returnPressed.connect(MainWindow.search_videos)
        self.text_actress_name.returnPressed.connect(MainWindow.search_videos)
        self.text_type.returnPressed.connect(MainWindow.search_videos)
        self.result_display.itemDoubleClicked.connect(MainWindow.item_double_clicked)
        self.action_add_to_favorite.triggered.connect(
                lambda: MainWindow.setup_favorite(self.result_display.selectedItems()[0].text(), 0))
        self.action_remove_from_favorite.triggered.connect(
                lambda: MainWindow.setup_favorite(self.result_display.selectedItems()[0].text(), 1))
        self.action_batch_import.triggered.connect(lambda: MainWindow.import_data(1))
        self.action_manual_import.triggered.connect(lambda: MainWindow.import_data(0))
        self.signal_drop_database.connect(MainWindow.drop_database)
        self.action_show_all.triggered.connect(MainWindow.show_all_videos)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def right_click_menu(self, pos):
        """ Slot function:
        The right click menu with operation 'Copy'. 
        'Copy' is used to copy the selected item to the clipboard.
        """
        
        action = self.right_menu.exec_(QtGui.QCursor.pos())
        if action == self.action_copy:
            """ Case:
            Operation 'Copy'.
            """
            
            clipboard = QtWidgets.QApplication.clipboard()
            clipboard.setText(self.result_display.selectedItems()[0].text())
            event = QtCore.QEvent(QtCore.QEvent.Clipboard)
            QtWidgets.QApplication.sendEvent(clipboard, event)
                    
    def menubar_action(self, menu_item):
        """ Slot function:
        The menubar has 'Append', 'New', 'Clear', 'Sort', and 'Drop', 
        totally four operations. 
        The 'Append' operation is saving the log from the start of the 
        destination file, and 'New' is similar, but it saves the log from the 
        end of the file. 
        The 'Clear' operation is used to clear the shown items. 
        The 'Sort' operation is used to sort the shown items.
        The 'Drop' operation is used to drop the database.
        """
        
        if menu_item.text() == "Append":
            """ Case:
            Operation 'Append'.
            """
            
            # Check if the folder 'save' is created.
            if not os.path.isdir("save"):
                os.mkdir("save")
                
            with open(Ui_MainWindow.SAVE_LOG_PATH, 'a', encoding='utf8') as output_file:
                for i in range(self.result_display.count()):
                    output_file.write(self.result_display.item(i).text() + '\n')
            self.statusbar.showMessage("Info: 'Append' successfully ...")
        elif menu_item.text() == "New":
            """ Case:
            Operation 'New'.
            """
            
            options = QtWidgets.QFileDialog.Options()
            options |= QtWidgets.QFileDialog.DontUseNativeDialog
            filename, _ = QtWidgets.QFileDialog.getOpenFileName(
                    QtWidgets.QMainWindow(), "QFileDialog.getOpenFileName()", 
                    "", "All Files (*);;Text Files (*.txt)", options=options)
            
            if filename:
                with open(filename, 'w', encoding='utf8') as output_file:
                    for i in range(self.result_display.count()):
                        output_file.write(self.result_display.item(i).text() + '\n')
                self.statusbar.showMessage("Info: 'New' successfully ...")
        elif menu_item.text() == "Clear":
            """ Case:
            Operation 'Clear'.
            """
            
            self.result_display.clear()
            self.statusbar.showMessage("Info: 'Clear' successfully ...")
        elif menu_item.text() == "Sort":
            """ Case:
            Oepration 'Sort'.
            """
            
            self.result_display.sortItems()
            self.statusbar.showMessage("Info: 'Sort' successfully ...")
        elif menu_item.text() == "Drop":
            """ Case:
            Operation 'Drop'.
            """
            
            # Use message box to double-check if the user wanna drop the 
            # database.
            reply = self.question_messagebox()
            if reply == QtWidgets.QMessageBox.Yes:
                    self.statusbar.showMessage(
                            "Info: Start dropping the database ...")
                    self.signal_drop_database.emit()
            else:
                    self.statusbar.showMessage(
                            "Info: Operation 'Drop' is cancelled ...")
                    
    def question_messagebox(self):
        """ Function:
        Messagebox window.
        """
        
        message_box = QtWidgets.QMessageBox()
        message_box.setWindowTitle("Drop database")
        message_box.setWindowIcon(QtGui.QIcon(Ui_MainWindow.MSG_BOX_ICON_PATH))
        message_box.setIcon(QtWidgets.QMessageBox.Warning)
        message_box.setText("Are you sure to drop the database?")
        message_box.setStandardButtons(QtWidgets.QMessageBox.Yes
                                       | QtWidgets.QMessageBox.No)

        reply = message_box.exec_()
        
        return reply
    
    def retranslateUi(self, MainWindow):
        """ Function:
        Dynamically translate.
        """
        
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Main window"))
        self.label_video_number.setText(_translate("MainWindow", "Video No."))
        self.label_video_name.setText(_translate("MainWindow", "Video name"))
        self.label_actress_name.setText(_translate("MainWindow", "Actress name"))
        self.label_type.setText(_translate("MainWindow", "Type"))
        self.label_quality.setText(_translate("MainWindow", "Quality"))
        self.combobox_quality.setItemText(0, _translate("MainWindow", "360p"))
        self.combobox_quality.setItemText(1, _translate("MainWindow", "480p"))
        self.combobox_quality.setItemText(2, _translate("MainWindow", "720p"))
        self.combobox_quality.setItemText(3, _translate("MainWindow", "1080p"))
        self.button_show_number.setText(_translate("MainWindow", "Show No."))
        self.button_show_actresses.setText(_translate("MainWindow", "Show actresses"))
        self.button_show_types.setText(_translate("MainWindow", "Show types"))
        self.button_show_favorite.setText(_translate("MainWindow", "Show favorites"))
        self.menuitem_menu.setTitle(_translate("MainWindow", "Menu"))
        self.menu_save_log.setTitle(_translate("MainWindow", "Save log"))
        self.menu_import.setTitle(_translate("MainWindow", "Import"))
        self.action_clear_log.setText(_translate("MainWindow", "Clear"))
        self.action_clear_log.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.action_sort.setText(_translate("MainWindow", "Sort"))
        self.action_sort.setShortcut(_translate("MainWindow", "Ctrl+T"))
        self.action_drop_database.setText(_translate("MainWindow", "Drop"))
        self.action_drop_database.setShortcut(_translate("MainWindow", "Ctrl+D"))
        self.action_batch_import.setText(_translate("MainWindow", "Batch"))
        self.action_batch_import.setShortcut(_translate("MainWindow", "Ctrl+B"))
        self.action_manual_import.setText(_translate("MainWindow", "Manual"))
        self.action_manual_import.setShortcut(_translate("MainWindow", "Ctrl+M"))
        self.action_show_all.setText(_translate("MainWindow", "Show all"))
        self.action_show_all.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.action_append.setText(_translate("MainWindow", "Append"))
        self.action_append.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.action_new.setText(_translate("MainWindow", "New"))
        self.action_new.setShortcut(_translate("MainWindow", "Ctrl+N"))
