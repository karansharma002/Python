from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtWidgets import QMessageBox,QFileDialog
from mutagen.id3 import ID3
from mutagen.mp3 import MP3
from pygame import mixer
import os
import time
import configdata

#Global Vars
songs_list = []
real_list = []
song_index = 0
mixer.init()

total_sec = 0
#Global Vars

class MyThread(QThread):
    
    change_value = pyqtSignal(int)
    
    def run(self):
        global songs_list
        global song_index
        audio = MP3(songs_list[song_index])
        length = audio.info.length
        numlength = length 
        total_sec = int(numlength)
        val = 0
        while val < total_sec:
            val +=1
            self.change_value.emit(val)
            time.sleep(1)

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(240, 370)
        MainWindow.setFixedSize(MainWindow.size())
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Images/Icons/Logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-image: url(:/Images/Icons/background.png);")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Fixed Text Widget
        self.FixedNPTEXT = QtWidgets.QLabel(self.centralwidget)
        self.FixedNPTEXT.setGeometry(QtCore.QRect(70, 50, 111, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.FixedNPTEXT.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.FixedNPTEXT.setFont(font)
        self.FixedNPTEXT.setAutoFillBackground(False)
        self.FixedNPTEXT.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.FixedNPTEXT.setObjectName("FixedNPTEXT")

        # SONG PROGRESS BAR 


        #########################################################
        self.ProgressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.ProgressBar.setGeometry(QtCore.QRect(10, 120, 211, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.ProgressBar.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ProgressBar.setFont(font)
        self.ProgressBar.setAutoFillBackground(False)
        self.ProgressBar.setTextVisible(False)
        self.ProgressBar.setOrientation(QtCore.Qt.Horizontal)
        self.ProgressBar.setInvertedAppearance(False)
        self.ProgressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.ProgressBar.setObjectName("ProgressBar")
        #self.ProgressBar.set
        

        #lCD WIDGET
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(80, 20, 81, 23))
        self.lcdNumber.setObjectName("lcdNumber")
        
        # VOLUME WHEEL
        self.Volume = QtWidgets.QDial(self.centralwidget)
        self.Volume.setGeometry(QtCore.QRect(180, 210, 51, 61))
        self.Volume.setAutoFillBackground(False)
        self.Volume.setStyleSheet("background-color: rgb(120, 120, 120));")
        self.Volume.setMaximum(10)
        self.Volume.setSingleStep(1)
        self.Volume.setPageStep(1)
        self.Volume.setWrapping(False)
        self.Volume.setNotchesVisible(True)
        self.Volume.setObjectName("Volume")
        self.Volume.valueChanged.connect(self.set_volume)

        # SONG NAME LABEL
        self.SongName = QtWidgets.QLabel(self.centralwidget)
        self.SongName.setGeometry(QtCore.QRect(10, 90, 221, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.SongName.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.SongName.setFont(font)
        self.SongName.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.SongName.setFrameShadow(QtWidgets.QFrame.Plain)
        self.SongName.setObjectName("SongName")

        # PREVIOUS TRACK 
        self.Previous = QtWidgets.QToolButton(self.centralwidget)
        self.Previous.setGeometry(QtCore.QRect(50, 150, 31, 21))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Images/Icons/Previous.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Previous.setIcon(icon1)
        self.Previous.setObjectName("Previous")
        self.Previous.clicked.connect(self.previous_music)

        # Play
        self.Play = QtWidgets.QToolButton(self.centralwidget)
        self.Play.setGeometry(QtCore.QRect(130, 150, 31, 21))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/Images/Icons/Play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Play.setIcon(icon4)
        self.Play.setObjectName("Stop")
        self.Play.clicked.connect(self.play_music)

        # PAUSE/PLAY 
        self.PausePlay = QtWidgets.QToolButton(self.centralwidget)
        self.PausePlay.setGeometry(QtCore.QRect(90, 150, 31, 21))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Images/Icons/Pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PausePlay.setIcon(icon2)
        self.PausePlay.setObjectName("PausePlay")
        #self.PausePlay.clicked.connect(self.pause_music)
        self.PausePlay.clicked.connect(self.pause_music)
        # SEARCH BAR
        self.Searchbar = QtWidgets.QLineEdit(self.centralwidget)
        self.Searchbar.setGeometry(QtCore.QRect(30, 300, 191, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setBold(True)
        font.setWeight(75)
        self.Searchbar.setFont(font)
        self.Searchbar.setAutoFillBackground(False)
        self.Searchbar.setClearButtonEnabled(True)
        self.Searchbar.setObjectName("Searchbar")
        

        # NEXT MUSIC
        self.Next = QtWidgets.QToolButton(self.centralwidget)
        self.Next.setGeometry(QtCore.QRect(170, 150, 31, 21))
        icon3 = QtGui.QIcon()

        icon3.addPixmap(QtGui.QPixmap(":/Images/Icons/Next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Next.setIcon(icon3)
        self.Next.setObjectName("Next")
        self.Next.clicked.connect(self.next_music)
        
        # CLEAR MUSIC LIST
        self.Clear= QtWidgets.QToolButton(self.centralwidget)
        self.Clear.setGeometry(QtCore.QRect(90, 180, 71, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Clear.setPalette(palette)   
        self.Clear.setFont(font)
        self.Clear.setObjectName("Clear List")
        self.Clear.clicked.connect(self.clear_list)

        # LIST OF SONGS
        self.ShowList = QtWidgets.QToolButton(self.centralwidget)
        self.ShowList.setGeometry(QtCore.QRect(90, 210, 71, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ShowList.setPalette(palette)   
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ShowList.setFont(font)
        self.ShowList.setObjectName("ShowList")
        self.ShowList.clicked.connect(self.list_page)

        # REPEAT THE SONG
        self.Repeat = QtWidgets.QToolButton(self.centralwidget)
        self.Repeat.setGeometry(QtCore.QRect(90, 240, 71, 19))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Repeat.setPalette(palette)   
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Repeat.setFont(font)
        self.Repeat.setObjectName("Repeat")
        self.Repeat.clicked.connect(self.repeat_music)

        # SHUFFLE THE SONG
        self.Shuffle = QtWidgets.QToolButton(self.centralwidget)
        self.Shuffle.setGeometry(QtCore.QRect(90, 270, 71, 19))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Shuffle.setFont(font)
        self.Shuffle.setObjectName("Shuffle")
        self.Shuffle.setPalette(palette)   



        # MAIN WINDOW

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 240, 21))
        self.menubar.setAutoFillBackground(False)
        self.menubar.setStyleSheet("")
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setStyleSheet("")
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuPreferences = QtWidgets.QMenu(self.menuSettings)
        self.menuPreferences.setObjectName("menuPreferences")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpen.triggered.connect(self.song_directory)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.triggered.connect(self.exit_app)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionUpdates = QtWidgets.QAction(MainWindow)
        self.actionUpdates.setObjectName("actionUpdates")
        self.actionEqualizer = QtWidgets.QAction(MainWindow)
        self.actionEqualizer.setObjectName("actionEqualizer")
        self.actionSongs_List = QtWidgets.QAction(MainWindow)
        self.actionSongs_List.setObjectName("actionSongs_List")
        self.actionThemes = QtWidgets.QAction(MainWindow)
        self.actionThemes.setObjectName("actionThemes")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.actionAbout.triggered.connect(self.about_page)
        self.menuHelp.addAction(self.actionUpdates)
        self.actionUpdates.triggered.connect(self.update_page)
        self.menuPreferences.addAction(self.actionThemes)
        self.menuSettings.addAction(self.actionEqualizer)
        self.menuSettings.addAction(self.menuPreferences.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Media Hub"))
        self.FixedNPTEXT.setText(_translate("MainWindow", "NOW PLAYING"))
        self.SongName.setText(_translate("MainWindow","..."))
        self.Previous.setText(_translate("MainWindow", "..."))
        self.Play.setText(_translate("MainWindow", "..."))
        self.PausePlay.setText(_translate("MainWindow", "..."))
        self.Searchbar.setPlaceholderText(_translate("MainWindow","..."))
        self.Next.setText(_translate("MainWindow", "..."))
        self.Clear.setText(_translate("MainWindow", "Clear List"))
        self.ShowList.setText(_translate("MainWindow", "Show List"))
        self.Repeat.setText(_translate("MainWindow", "Repeat"))
        self.Shuffle.setText(_translate("MainWindow", "Shuffle"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuPreferences.setTitle(_translate("MainWindow", "Preferences"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionUpdates.setText(_translate("MainWindow", "Updates"))
        self.actionEqualizer.setText(_translate("MainWindow", "Equalizer"))
        self.actionSongs_List.setText(_translate("MainWindow", "Songs List"))
        self.actionThemes.setText(_translate("MainWindow", "Themes"))

    def song_directory(self):
        global song_index
        global songs_list
        global real_list
        directory_choose = QFileDialog.getOpenFileNames()
        path = directory_choose[0]

        for filename in path:
            audioname = ID3(filename)
            real_list.append(audioname['TIT2'].text[0])
            songs_list.append(filename)
        
        mixer.music.load(songs_list[song_index])
        self.test_variable()
        mixer.music.play()
        self.start_progress_bar()
        self.SongName.setText(real_list[song_index])
    
    def clear_list(self):
        global songs_list
        global song_index
        songs_list = []
        song_index = 0
        return songs_list, song_index

    def play_music(self):
        mixer.music.play()
        self.start_progress_bar()
        self.SongName.setText(real_list[song_index])

    def pause_music(self):
        mixer.music.pause()
        self.SongName.setText(" ------ Paused ----- ")
    
    
    def next_music(self):
        global song_index
        global real_list
        self.stop_progress_bar()
        try:
            song_index +=1
            mixer.music.load(songs_list[song_index])
            self.test_variable()
            mixer.music.play()
            self.start_progress_bar()
            self.SongName.setText(real_list[song_index])  
            return song_index
        except Exception:
            song_index = 0
            return song_index
    
    def previous_music(self):
        global song_index
        global real_list
        self.stop_progress_bar()
        try:
            song_index -= 1
            mixer.music.load(songs_list[song_index])
            self.test_variable()
            mixer.music.play()
            self.start_progress_bar()
            self.SongName.setText(real_list[song_index])
            return song_index
        except Exception:
            song_index = 0
            return song_index

    
    def repeat_music(self):
        pass

    def set_volume(self):
        a_volume = self.Volume.value()
        mixer.music.set_volume(a_volume)

    def search_bar(self):
        pass

    def shuffle_music(self):
        pass
        
    def audio_list(self):
        pass

    def about_page(self):
        show_label = QMessageBox()
        show_label.setWindowTitle("Media Hub ")
        show_label.setIcon(QMessageBox.Information)
        show_label.setText(" Version: V1.0.0 \n Version Date: 02/02/2020 \n Developed By Sofia \n 2020-21")
        show_label.exec_()
    
    def update_page(self):
        show_label = QMessageBox()
        show_label.setWindowTitle("Media Hub")
        show_label.setIcon(QMessageBox.Warning)
        show_label.setText(" --- | Coming Very Soon | ----")
        show_label.exec_()
    
    def list_page(self):
        global real_list
        show_label = QMessageBox()
        show_label.setWindowTitle("Media Hub [List of Songs]")
        show_label.setIcon(QMessageBox.Information)
        show_label.setText(" Not Available! Check Readme for More information! ")
        show_label.exec()
        
    def progress_value(self,val):
        self.ProgressBar.setValue(val)
        self.lcdNumber.display(val)
    
    def stop_progress_bar(self):
        self.thread = MyThread()
        self.thread.exit()
        self.lcdNumber.display(0)

    def start_progress_bar(self):
        self.thread = MyThread()
        self.thread.change_value.connect(self.progress_value)
        self.thread.start()

    def exit_app(self):
        sys.exit(app.exec_())
       
    def test_variable(self):
        global songs_list
        global song_index
        song_var = MP3(songs_list[song_index])
        song_length = song_var.info.length
        length_to_int = int(song_length)
        return self.ProgressBar.setMaximum(length_to_int)

    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    #Thread(target = audio_num).start()
    #Thread(target = MainWindow.show()).start()
    MainWindow.show()
    sys.exit(app.exec_())
