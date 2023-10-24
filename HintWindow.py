from PyQt5 import QtWidgets
import sys

class HintWindow(QtWidgets.QWidget):
    def __init__(self,hintText):
        super().__init__()
        self.setWindowTitle('Hint')
        self.hintText=hintText
        self.resize(500, 200)
        self.ui()

    def ui(self):
        self.contest = QtWidgets.QLabel(self)
        self.contest.setText(self.hintText)
        self.contest.setStyleSheet('font-size:26px;')
        self.contest.setGeometry(40,60,350,40)


