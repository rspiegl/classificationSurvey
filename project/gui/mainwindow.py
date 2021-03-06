# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/masterGUI/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1170)
        MainWindow.setStyleSheet("background-color: rgb(186, 189, 182);")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.listPicturesFalse = QtWidgets.QListWidget(self.centralWidget)
        self.listPicturesFalse.setMaximumSize(QtCore.QSize(800, 532))
        self.listPicturesFalse.setStyleSheet("background-color: rgb(186, 189, 182);\n"
"gridline-color: rgb(0, 0, 0);")
        self.listPicturesFalse.setFrameShape(QtWidgets.QFrame.Box)
        self.listPicturesFalse.setFrameShadow(QtWidgets.QFrame.Plain)
        self.listPicturesFalse.setLineWidth(2)
        self.listPicturesFalse.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listPicturesFalse.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.listPicturesFalse.setIconSize(QtCore.QSize(256, 256))
        self.listPicturesFalse.setViewMode(QtWidgets.QListView.IconMode)
        self.listPicturesFalse.setObjectName("listPicturesFalse")
        self.gridLayout.addWidget(self.listPicturesFalse, 1, 1, 1, 1)
        self.listPicturesTrue = QtWidgets.QListWidget(self.centralWidget)
        self.listPicturesTrue.setMaximumSize(QtCore.QSize(800, 532))
        self.listPicturesTrue.setStyleSheet("gridline-color: rgb(0, 0, 0);\n"
"background-color: rgb(186, 189, 182);")
        self.listPicturesTrue.setFrameShape(QtWidgets.QFrame.Box)
        self.listPicturesTrue.setFrameShadow(QtWidgets.QFrame.Plain)
        self.listPicturesTrue.setLineWidth(2)
        self.listPicturesTrue.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listPicturesTrue.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.listPicturesTrue.setIconSize(QtCore.QSize(256, 256))
        self.listPicturesTrue.setViewMode(QtWidgets.QListView.IconMode)
        self.listPicturesTrue.setObjectName("listPicturesTrue")
        self.gridLayout.addWidget(self.listPicturesTrue, 1, 0, 1, 1)
        self.widgetPic = QtWidgets.QWidget(self.centralWidget)
        self.widgetPic.setMinimumSize(QtCore.QSize(0, 360))
        self.widgetPic.setObjectName("widgetPic")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widgetPic)
        self.horizontalLayout_2.setContentsMargins(11, 0, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.picLeft = QtWidgets.QLabel(self.widgetPic)
        self.picLeft.setMaximumSize(QtCore.QSize(512, 512))
        self.picLeft.setAlignment(QtCore.Qt.AlignCenter)
        self.picLeft.setObjectName("picLeft")
        self.horizontalLayout_2.addWidget(self.picLeft)
        self.picShow = QtWidgets.QLabel(self.widgetPic)
        self.picShow.setMinimumSize(QtCore.QSize(512, 512))
        self.picShow.setMaximumSize(QtCore.QSize(512, 512))
        self.picShow.setFrameShape(QtWidgets.QFrame.Panel)
        self.picShow.setFrameShadow(QtWidgets.QFrame.Plain)
        self.picShow.setScaledContents(True)
        self.picShow.setAlignment(QtCore.Qt.AlignCenter)
        self.picShow.setObjectName("picShow")
        self.horizontalLayout_2.addWidget(self.picShow)
        self.picRight = QtWidgets.QLabel(self.widgetPic)
        self.picRight.setMinimumSize(QtCore.QSize(512, 512))
        self.picRight.setMaximumSize(QtCore.QSize(512, 512))
        self.picRight.setAlignment(QtCore.Qt.AlignCenter)
        self.picRight.setObjectName("picRight")
        self.horizontalLayout_2.addWidget(self.picRight)
        self.gridLayout.addWidget(self.widgetPic, 0, 0, 1, 2)
        self.widgetButtons = QtWidgets.QWidget(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetButtons.sizePolicy().hasHeightForWidth())
        self.widgetButtons.setSizePolicy(sizePolicy)
        self.widgetButtons.setMinimumSize(QtCore.QSize(0, 45))
        self.widgetButtons.setObjectName("widgetButtons")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widgetButtons)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonTrue = QtWidgets.QPushButton(self.widgetButtons)
        self.pushButtonTrue.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButtonTrue.setObjectName("pushButtonTrue")
        self.horizontalLayout.addWidget(self.pushButtonTrue)
        self.descriptionLabel = QtWidgets.QLabel(self.widgetButtons)
        self.descriptionLabel.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.descriptionLabel.sizePolicy().hasHeightForWidth())
        self.descriptionLabel.setSizePolicy(sizePolicy)
        self.descriptionLabel.setMaximumSize(QtCore.QSize(360, 16777215))
        self.descriptionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.descriptionLabel.setObjectName("descriptionLabel")
        self.horizontalLayout.addWidget(self.descriptionLabel)
        self.pushButtonFalse = QtWidgets.QPushButton(self.widgetButtons)
        self.pushButtonFalse.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButtonFalse.setObjectName("pushButtonFalse")
        self.horizontalLayout.addWidget(self.pushButtonFalse)
        self.gridLayout.addWidget(self.widgetButtons, 2, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1920, 24))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuDatasets = QtWidgets.QMenu(self.menuBar)
        self.menuDatasets.setObjectName("menuDatasets")
        self.menuCamera_Rotation = QtWidgets.QMenu(self.menuDatasets)
        self.menuCamera_Rotation.setObjectName("menuCamera_Rotation")
        self.menuRandom_Board_Images = QtWidgets.QMenu(self.menuDatasets)
        self.menuRandom_Board_Images.setObjectName("menuRandom_Board_Images")
        self.menuRotated_Images = QtWidgets.QMenu(self.menuDatasets)
        self.menuRotated_Images.setObjectName("menuRotated_Images")
        self.menuSVRT = QtWidgets.QMenu(self.menuBar)
        self.menuSVRT.setObjectName("menuSVRT")
        self.menuPSVRT = QtWidgets.QMenu(self.menuBar)
        self.menuPSVRT.setObjectName("menuPSVRT")
        MainWindow.setMenuBar(self.menuBar)
        self.actionSelectDirectory = QtWidgets.QAction(MainWindow)
        self.actionSelectDirectory.setObjectName("actionSelectDirectory")
        self.actionReset = QtWidgets.QAction(MainWindow)
        self.actionReset.setObjectName("actionReset")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionCamRot_1 = QtWidgets.QAction(MainWindow)
        self.actionCamRot_1.setObjectName("actionCamRot_1")
        self.actionCamRot_5 = QtWidgets.QAction(MainWindow)
        self.actionCamRot_5.setObjectName("actionCamRot_5")
        self.actionRanBoa_1 = QtWidgets.QAction(MainWindow)
        self.actionRanBoa_1.setObjectName("actionRanBoa_1")
        self.actionRanBoa_5 = QtWidgets.QAction(MainWindow)
        self.actionRanBoa_5.setObjectName("actionRanBoa_5")
        self.actionRotIm_1 = QtWidgets.QAction(MainWindow)
        self.actionRotIm_1.setObjectName("actionRotIm_1")
        self.actionRotIm_5 = QtWidgets.QAction(MainWindow)
        self.actionRotIm_5.setObjectName("actionRotIm_5")
        self.actionSVRT_1 = QtWidgets.QAction(MainWindow)
        self.actionSVRT_1.setObjectName("actionSVRT_1")
        self.actionSVRT_19 = QtWidgets.QAction(MainWindow)
        self.actionSVRT_19.setObjectName("actionSVRT_19")
        self.actionSVRT_20 = QtWidgets.QAction(MainWindow)
        self.actionSVRT_20.setObjectName("actionSVRT_20")
        self.actionSVRT_21 = QtWidgets.QAction(MainWindow)
        self.actionSVRT_21.setObjectName("actionSVRT_21")
        self.actionPSVRT_SD = QtWidgets.QAction(MainWindow)
        self.actionPSVRT_SD.setObjectName("actionPSVRT_SD")
        self.actionPSVRT_SR = QtWidgets.QAction(MainWindow)
        self.actionPSVRT_SR.setObjectName("actionPSVRT_SR")
        self.actionRestart = QtWidgets.QAction(MainWindow)
        self.actionRestart.setObjectName("actionRestart")
        self.actionConnect_EyeTracker = QtWidgets.QAction(MainWindow)
        self.actionConnect_EyeTracker.setObjectName("actionConnect_EyeTracker")
        self.menuFile.addAction(self.actionSelectDirectory)
        self.menuFile.addAction(self.actionConnect_EyeTracker)
        self.menuFile.addAction(self.actionReset)
        self.menuFile.addAction(self.actionRestart)
        self.menuFile.addAction(self.actionExit)
        self.menuCamera_Rotation.addAction(self.actionCamRot_5)
        self.menuCamera_Rotation.addAction(self.actionCamRot_1)
        self.menuRandom_Board_Images.addAction(self.actionRanBoa_5)
        self.menuRandom_Board_Images.addAction(self.actionRanBoa_1)
        self.menuRotated_Images.addAction(self.actionRotIm_5)
        self.menuRotated_Images.addAction(self.actionRotIm_1)
        self.menuDatasets.addAction(self.menuRandom_Board_Images.menuAction())
        self.menuDatasets.addAction(self.menuCamera_Rotation.menuAction())
        self.menuDatasets.addAction(self.menuRotated_Images.menuAction())
        self.menuSVRT.addAction(self.actionSVRT_1)
        self.menuSVRT.addAction(self.actionSVRT_19)
        self.menuSVRT.addAction(self.actionSVRT_20)
        self.menuSVRT.addAction(self.actionSVRT_21)
        self.menuPSVRT.addAction(self.actionPSVRT_SR)
        self.menuPSVRT.addAction(self.actionPSVRT_SD)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuPSVRT.menuAction())
        self.menuBar.addAction(self.menuSVRT.menuAction())
        self.menuBar.addAction(self.menuDatasets.menuAction())

        self.retranslateUi(MainWindow)
        self.actionReset.triggered.connect(MainWindow.reset)
        self.actionSelectDirectory.triggered.connect(MainWindow.selectDirectory)
        self.actionExit.triggered.connect(MainWindow.close)
        self.pushButtonFalse.clicked.connect(MainWindow.categoryFalse)
        self.pushButtonTrue.clicked.connect(MainWindow.categoryTrue)
        self.actionCamRot_1.triggered.connect(MainWindow.menuCamRot_1)
        self.actionCamRot_5.triggered.connect(MainWindow.menuCamRot_5)
        self.actionRanBoa_1.triggered.connect(MainWindow.menuRanBoa_1)
        self.actionRanBoa_5.triggered.connect(MainWindow.menuRanBoa_5)
        self.actionRotIm_1.triggered.connect(MainWindow.menuRotIma_1)
        self.actionRotIm_5.triggered.connect(MainWindow.menuRotIma_5)
        self.actionSVRT_1.triggered.connect(MainWindow.menuSVRT_1)
        self.actionSVRT_19.triggered.connect(MainWindow.menuSVRT_19)
        self.actionSVRT_20.triggered.connect(MainWindow.menuSVRT_20)
        self.actionSVRT_21.triggered.connect(MainWindow.menuSVRT_21)
        self.actionPSVRT_SD.triggered.connect(MainWindow.menuPSVRT_SD)
        self.actionPSVRT_SR.triggered.connect(MainWindow.menuPSVRT_SR)
        self.actionRestart.triggered.connect(MainWindow.restart)
        self.actionConnect_EyeTracker.triggered.connect(MainWindow.connectEyeTracker)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Humans vs CNNs"))
        self.picShow.setText(_translate("MainWindow", "ImageLabel"))
        self.pushButtonTrue.setToolTip(_translate("MainWindow", "Shortcut: Left Arrow"))
        self.pushButtonTrue.setText(_translate("MainWindow", "Category 1"))
        self.pushButtonTrue.setShortcut(_translate("MainWindow", "Left"))
        self.descriptionLabel.setText(_translate("MainWindow", "Welcome!"))
        self.pushButtonFalse.setToolTip(_translate("MainWindow", "Shortcut: Right Arrow"))
        self.pushButtonFalse.setText(_translate("MainWindow", "Category 2"))
        self.pushButtonFalse.setShortcut(_translate("MainWindow", "Right"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuDatasets.setTitle(_translate("MainWindow", "Chessboard"))
        self.menuCamera_Rotation.setTitle(_translate("MainWindow", "Camrot"))
        self.menuRandom_Board_Images.setTitle(_translate("MainWindow", "Ranboaima"))
        self.menuRotated_Images.setTitle(_translate("MainWindow", "Rotima"))
        self.menuSVRT.setTitle(_translate("MainWindow", "SVRT"))
        self.menuPSVRT.setTitle(_translate("MainWindow", "PSVRT"))
        self.actionSelectDirectory.setText(_translate("MainWindow", "Select Dataset"))
        self.actionReset.setText(_translate("MainWindow", "Reset"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionCamRot_1.setText(_translate("MainWindow", "1"))
        self.actionCamRot_5.setText(_translate("MainWindow", "5"))
        self.actionRanBoa_1.setText(_translate("MainWindow", "1"))
        self.actionRanBoa_5.setText(_translate("MainWindow", "5"))
        self.actionRotIm_1.setText(_translate("MainWindow", "1"))
        self.actionRotIm_5.setText(_translate("MainWindow", "5"))
        self.actionSVRT_1.setText(_translate("MainWindow", "1"))
        self.actionSVRT_19.setText(_translate("MainWindow", "19"))
        self.actionSVRT_20.setText(_translate("MainWindow", "20"))
        self.actionSVRT_21.setText(_translate("MainWindow", "21"))
        self.actionPSVRT_SD.setText(_translate("MainWindow", "SD"))
        self.actionPSVRT_SR.setText(_translate("MainWindow", "SR"))
        self.actionRestart.setText(_translate("MainWindow", "Restart"))
        self.actionConnect_EyeTracker.setText(_translate("MainWindow", "Connect EyeTracker"))


