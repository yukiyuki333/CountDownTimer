# countDownTimer

打包：pyinstaller -F CountDownTimer.py -p Timer_UI.py -p HintWindow.py -p playMusicCtrl.py --noconsole --icon=icon.ico

若要使用音樂播放功能：將某個 mp3 放在和 .py 相同的資料夾即可，無法播放可能是 mp3 編碼問題。
倒數到 0 會自動從頭放音樂(相當於鬧鐘)

套件：pyqt5、pyinstaller
