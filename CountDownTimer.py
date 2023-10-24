import sys,os
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import*
from PyQt5 import QtGui
from Timer_UI import Ui_Form
from PyQt5.QtMultimedia import QMediaPlayer,QMediaContent
from time import perf_counter, sleep
import threading
from HintWindow import HintWindow


def create_thread(target):
    thread=threading.Thread(target=target)
    thread.daemon=True
    thread.start()


class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form() #新增剛剛拉的前端介面
        self.ui.setupUi(self)
        # variables
        self.endFlag, self.pauseFlag,self.timerIsRunningFlag= 0,0,0
        self.hour, self.min, self.sec = 0, 30, 1

        # music player setting
        self.musicIsPlayingFlag=0

        # call init function
        self.initTimer()

        # click start button
        self.ui.Start_button.clicked.connect(self.start_thread)

        # click set time button
        self.ui.setTimeButton.clicked.connect(self.setTime)

        # click end button
        self.ui.End_button.clicked.connect(self.setTimerEnd)

        # click pause button
        self.ui.tmp_button.clicked.connect(self.pauseCtrl)

        # click play music button
        self.ui.playMusicButton.clicked.connect(self.playMusic)

        # show
        self.show()

    # 初始化計時器
    def initTimer(self):
        self.hour, self.min, self.sec = 0, 30, 0
        font = QtGui.QFont()
        font.setPointSize(26)
        self.ui.second.setText("00")
        self.ui.second.setFont(font)
        self.ui.minute.setText("30")
        self.ui.minute.setFont(font)
        self.ui.hour.setText("00")
        self.ui.hour.setFont(font)

    # 錯誤操作時跳出提示
    def setHint(self,hintText):
        self.hw = HintWindow(hintText)  # 連接新視窗
        self.hw.show()

    # 按下開始按鈕
    def start_thread(self):
        if self.timerIsRunningFlag==0:
            create_thread(self.startTimer)
        else:
            self.setHint("Timer is running!")
    def startTimer(self):
        self.timerIsRunningFlag = 1
        self.endFlag = 0
        self.pauseFlag=0
        self.countDownTheTime()
    # 按下設置時間按鈕
    def setTime(self):
        if self.timerIsRunningFlag==0:
            input_hour=self.ui.inputHourBox.text()
            input_min=self.ui.inputMinuteBox.text()
            input_sec=self.ui.inputSecondBox.text()
            if input_hour:
                self.hour=int(input_hour)
            else:
                self.hour =0
            if input_min:
                self.min=int(input_min)
            else:
                self.min=0
            if input_sec:
                self.sec=int(input_sec)
            else:
                self.sec=0
            self.showTimerState()
        else:
            self.setHint("Timer is running!Can't set time")

    # 計時
    def countDownTheTime(self):
        while (True):
            sleep(0.9935)
            if self.sec!=0:
                self.sec-=1
            else:
                if self.min!=0:
                    self.min-=1
                    self.sec=59
                else:
                    if self.hour!=0:
                        self.hour-=1
                        self.min = 59
                        self.sec = 59
                    else:
                        self.endFlag = 1
            self.showTimerState()
            if self.endFlag == 1:
                self.timerIsRunningFlag=0
                break
            if self.pauseFlag == 1:
                break
    # 顯示當前計時器狀態
    def showTimerState(self):
        font = QtGui.QFont()
        font.setPointSize(26)
        if int(self.sec) < 10:
            self.ui.second.setText("0" + str(self.sec))
            self.ui.second.setFont(font)
        else:
            self.ui.second.setText(str(self.sec))
            self.ui.second.setFont(font)
        if int(self.min) < 10:
            self.ui.minute.setText("0" + str(self.min))
            self.ui.minute.setFont(font)
        else:
            self.ui.minute.setText(str(self.min))
            self.ui.minute.setFont(font)
        if int(self.hour) < 10:
            self.ui.hour.setText("0" + str(self.hour))
            self.ui.hour.setFont(font)
        else:
            self.ui.hour.setText(str(self.hour))
            self.ui.hour.setFont(font)
    # 停止計時器
    def setTimerEnd(self):
        self.endFlag = 1
        self.timerIsRunningFlag = 0
        self.pauseFlag=0
        self.initTimer()


    # 暫停計時器
    def pauseCtrl(self):
        if self.endFlag == 0 and self.timerIsRunningFlag == 1:
            if self.pauseFlag == 0:
                # 啟動暫停
                self.pauseFlag = 1
            else:
                # 啟動繼續
                self.pauseFlag = 0
                create_thread(self.countDownTheTime)
    # 播放音樂設置
    def playMusic(self):
        if self.musicIsPlayingFlag==0:
            #play music
            self.musicIsPlayingFlag=1
            self.ui.playMusicButton.setText("playMusic")
        else:
            #pause music
            self.musicIsPlayingFlag = 0
            self.ui.playMusicButton.setText("stopMusic")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = AppWindow()
    w.show()
    sys.exit(app.exec_())