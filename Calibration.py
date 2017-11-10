import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Calibration_GUI import *
import Constents


class Calibration_window(QWidget):
    #signal = pyqtSignal()

    def __init__(self, parent=None):
        QWidget.__init__(self,parent)
        self.Calibration = Ui_Calibration()
        self.Calibration.setupUi(self)

        self.setUpMainUiFunction()

    def setUpMainUiFunction(self):
        self.Calibration.Button_ok.hide()
        self.Calibration.Button_Cancel.clicked.connect(self.cancelButton)

    def cancelButton(self):
        self.close()
