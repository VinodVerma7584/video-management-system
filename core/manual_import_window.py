# -*- coding: utf-8 -*-
"""
@author: GitHub@Oscarshu0719
"""

from PyQt5 import QtCore, QtGui, QtWidgets

class ManualImportWindow(object):
    """ Class:
    Manual import window.
    """
    
    # Manual import window icon.
    WIN_ICON_PATH = r"conf\import.ico"
    # Button 'Enter' icon.
    BUTTON_ICON_PATH = r"conf\folder.ico"
    
    def setupUi(self, MainWindow):
        """ Function.
        Setup user interface of Manual import window.
        """
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 450)
        MainWindow.setWindowIcon(QtGui.QIcon(ManualImportWindow.WIN_ICON_PATH))
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 3, 581, 351))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        
        self.text_type = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.text_type.setObjectName("text_type")
        self.gridLayout.addWidget(self.text_type, 4, 1, 1, 1)
        self.label_number = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_number.setObjectName("label_number")
        self.gridLayout.addWidget(self.label_number, 0, 0, 1, 1)
        self.label_quality = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_quality.setObjectName("label_quality")
        self.gridLayout.addWidget(self.label_quality, 5, 0, 1, 1)
        self.button_location = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_location.setObjectName("button_location")
        self.button_location.setIcon(
                QtGui.QIcon(ManualImportWindow.BUTTON_ICON_PATH))
        self.gridLayout.addWidget(self.button_location, 6, 0, 1, 1)
        self.text_number = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.text_number.setObjectName("text_number")
        self.gridLayout.addWidget(self.text_number, 0, 1, 1, 1)
        self.checkbox_favorite = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkbox_favorite.setText("")
        self.checkbox_favorite.setObjectName("checkbox_favorite")
        self.gridLayout.addWidget(self.checkbox_favorite, 3, 1, 1, 1)
        self.label_favorite = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_favorite.setObjectName("label_favorite")
        self.gridLayout.addWidget(self.label_favorite, 3, 0, 1, 1)
        self.label_type = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_type.setObjectName("label_type")
        self.gridLayout.addWidget(self.label_type, 4, 0, 1, 1)
        self.label_actress_name = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_actress_name.setObjectName("label_actress_name")
        self.gridLayout.addWidget(self.label_actress_name, 2, 0, 1, 1)
        self.combobox_quality = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.combobox_quality.setObjectName("combobox_quality")
        self.combobox_quality.addItem("")
        self.combobox_quality.addItem("")
        self.combobox_quality.addItem("")
        self.combobox_quality.addItem("")
        self.gridLayout.addWidget(self.combobox_quality, 5, 1, 1, 1)
        self.text_actress_name = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.text_actress_name.setObjectName("text_actress_name")
        self.gridLayout.addWidget(self.text_actress_name, 2, 1, 1, 1)
        self.text_video_name = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.text_video_name.setObjectName("text_video_name")
        self.gridLayout.addWidget(self.text_video_name, 1, 1, 1, 1)
        self.text_location = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.text_location.setObjectName("text_location")
        self.gridLayout.addWidget(self.text_location, 6, 1, 1, 1)
        self.label_video_name = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_video_name.setObjectName("label_video_name")
        self.gridLayout.addWidget(self.label_video_name, 1, 0, 1, 1)
        self.button_enter = QtWidgets.QPushButton(self.centralwidget)
        self.button_enter.setGeometry(QtCore.QRect(10, 360, 581, 31))
        self.button_enter.setObjectName("button_enter")
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        
        self.retranslateUi(MainWindow)

        # Connect to slot functions.
        self.button_location.clicked.connect(self.select_video)
        self.button_enter.clicked.connect(MainWindow.import_video)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def select_video(self):
        """ Slot funtion:
        Select a video and set the textbox with the path of selected video.
        """
        
        video_name, _ = QtWidgets.QFileDialog.getOpenFileName(
                QtWidgets.QMainWindow(), "Select video", QtCore.QDir.homePath())
        
        if video_name != '':
            self.text_location.setText(video_name)

    def retranslateUi(self, MainWindow):
        """ Function:
        Dynamically translate.
        """
        
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Manually import window"))
        self.label_number.setText(_translate("MainWindow", "No."))
        self.label_quality.setText(_translate("MainWindow", "Quality"))
        self.button_location.setText(_translate("MainWindow", "Location"))
        self.label_favorite.setText(_translate("MainWindow", "Favorite"))
        self.label_type.setText(_translate("MainWindow", "Type"))
        self.label_actress_name.setText(_translate("MainWindow", "Actress name"))
        self.combobox_quality.setItemText(0, _translate("MainWindow", "360p"))
        self.combobox_quality.setItemText(1, _translate("MainWindow", "480p"))
        self.combobox_quality.setItemText(2, _translate("MainWindow", "720p"))
        self.combobox_quality.setItemText(3, _translate("MainWindow", "1080p"))
        self.label_video_name.setText(_translate("MainWindow", "Video name"))
        self.button_enter.setText(_translate("MainWindow", "Enter"))
    
            