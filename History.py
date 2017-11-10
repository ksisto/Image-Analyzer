import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from History_GUI import *

class HistoryList(QWidget):
    button_delete = pyqtSignal()
    button_move = pyqtSignal()

    def __init__(self, parent=None):
        QWidget.__init__(self,parent)
        self.HistoryItem = Ui_History_Item()
        self.HistoryItem.setupUi(self)
        self.setUpWidgetUiFunction()


    def setUpWidgetUiFunction(self):
        self.HistoryItem.Button_Delete.clicked.connect(self.deleteButtonPushed)
        self.HistoryItem.Button_Move.clicked.connect(self.moveButtonPushed)

    def setXpoint(self,X):
        self.HistoryItem.txt_XChange.setText(X)

    def setYpoint(self,Y):
        self.HistoryItem.txt_YChange.setText(Y)
    def setHistoryName(self,Name):
        self.HistoryItem.txt_point.setText(Name)
    def deleteButtonPushed(self):
        self.button_delete.emit()
    def moveButtonPushed(self):
        self.button_move.emit()
        #import pdb; pdb.set_trace()


#This site has something that can help
#https://stackoverflow.com/questions/30916787/deleting-an-item-from-a-scene
    # def setUpProjectName(self,ProjectName):
    #     self.CustomUi.text_Project_Name_Change.setText(ProjectName)
    #
    # def setUpMainName(self,Name):
    #     self.CustomUi.text_Name_Change.setText(Name)
    #
    # def setUpMainNumber(self,Number):
    #     self.CustomUi.text_PhoneNumber_CHANGE.setText(Number)
    #
    # def setupDate(self,Date):
    #     self.CustomUi.text_Date_CHANGE.setText(Date)
    #
    # def setupNextDate(self,Date):
    #     self.CustomUi.text_NextDeliverible_CHANGE.setText(Date)
    #
    # def setupProjectFoler(self,ProjectFolder):
    #     self.CustomUi.text_ProjectFolder_CHANGE.setText(ProjectFolder)
    #     self.CustomUi.text_ProjectFolder_CHANGE.setOpenExternalLinks(True)
