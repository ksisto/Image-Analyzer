import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Main_GUI import *
from GraphicsArea import *
from History import *
import Constents


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.setUpMainUiFunction()



    def setUpMainUiFunction(self):
        self.actionOpen.triggered.connect(self.OpenDialog)
        self.Button_LoadPhoto.clicked.connect(self.OpenDialog)

        open = QAction(QIcon("icons/open.bmp"), "open", self)
        save = QAction(QIcon("icons/save.bmp"), "save", self)
        NormalCursor = QAction(QIcon("icons/cursor-normal.png"), "NormalCursor", self)
        CrosshairCursor = QAction(QIcon("icons/crosshair.png"), "CrosshairCursor", self)

        self.TopToolBar.addAction(open)
        self.TopToolBar.addAction(save)
        self.LeftToolBar.addAction(NormalCursor)
        self.LeftToolBar.addAction(CrosshairCursor)


        # self.TopToolBar.actionTriggered[QAction].connect(self.toolbtnpressed)

    def OpenDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        #PicturePath = QStandardPaths.standardLocations(QStandardPaths.PicturesLocation)[0]
        #filenames, _ = QFileDialog.getOpenFileNames(self, "Open File", PicturePath, "JPEG File (*.jpeg)", options=options)
        filenames, _ = QFileDialog.getOpenFileNames(self, "Open File", "JPEG File (*.jpeg)", options=options)
        for filename in filenames:
            pixmap = QPixmap(filename)
            self.showPicture(pixmap)
            self.statusbar.showMessage("Successfully Loaded: {}".format(filename))

    def showPicture(self, picture):
        sub = QMdiSubWindow(self)
        self.loadPicture = LoadPicture(picture, sub)
        sub.setWidget(self.loadPicture)
        sub.setObjectName("Load_Picture_window")
        sub.setWindowTitle("New Photo")
        self.mdiArea.addSubWindow(sub)
        sub.show()

        if picture.size().height() > self.mdiArea.geometry().height():
             sub.resize(picture.size().width(),self.mdiArea.geometry().height())
        else:
            sub.resize(picture.size())

        self.loadPicture.log.MousePixmapSignal.connect(self.updatePixel)
        self.loadPicture.PictureArea.rectChanged.connect(self.UpdateStatueBar)
        self.loadPicture.log.pointDraw.connect(self.Add_History)

    def updatePixel(self, point, color):
        self.UserInput_PixelValue_X.setText("{}".format(point.x()))
        self.UserInput_PixelValue_Y.setText("{}".format(point.y()))

        self.UserInput_PixelValue_R.setText("{}".format(color.red()))
        self.UserInput_PixelValue_G.setText("{}".format(color.green()))
        self.UserInput_PixelValue_B.setText("{}".format(color.blue()))

    def UpdateStatueBar(self,r):

        topLeft = r.topLeft()
        bottomRight = r.bottomRight()
        self.statusbar.showMessage("Top Left X: " + str(topLeft.x()) + " Top Left Y: " + str(topLeft.y()) + " Bottom Right X: " + str(bottomRight.x()) + " Bottom Right Y: " + str(bottomRight.y()))


    def toolbtnpressed(self,a):
      print ("pressed tool button is",a.text())



    def Add_History(self,pos):
        self.HistoryWidget = HistoryList()
        self.HistoryWidget.setObjectName("HistoryWidget_"+ str(Constents.analysisCount))
        myQListWidgetItem = QListWidgetItem(self.History_List)
        myQListWidgetItem.setSizeHint(self.HistoryWidget.sizeHint())
        self.History_List.addItem(myQListWidgetItem)
        self.History_List.setItemWidget(myQListWidgetItem, self.HistoryWidget)
        self.HistoryWidget.buttonPushed.connect(self.deleteObject)
        self.HistoryWidget.setXpoint(str(pos.x()))
        self.HistoryWidget.setYpoint(str(pos.y()))
        self.HistoryWidget.setHistoryName("Point "+ str(Constents.analysisCount))
        Constents.analysisCount = Constents.analysisCount + 1


    def deleteObject(self):
        sender = self.sender() #var of object that sent the request
        row_number = sender.objectName().split("_")
        number = row_number[1]
        x,y = Constents.analysisDetails[str(number)]# getting xy for object
        self.loadPicture.findAndRemoveAnalysisPoint(x,y) #calling the class with the scense to delete it
        Constents.analysisDetails.pop(str(number)) # get rid of the object in the variables
        HistoryWidget = self.findChildren(HistoryList, "HistoryWidget_"+number)[0] #find the actual object

        HistoryWidget.deleteLater() #delete that object
        #Simport pdb; pdb.set_trace()
        #self.History_List.takeItem(HistoryWidget)

    def ToDoNext(self):
        pass

    # This guy has done alot of what I want to do. Refer to this later
    #https://stackoverflow.com/questions/32018223/pyqt4-qgraphicsitem-position-doesnt-map-into-scene-properly-after-drag
    #https://pythonhosted.org/guiqwt/index.html

    #https://github.com/marcel-goldschen-ohm/ImageViewerPyQt/blob/master/ImageViewerQt.py
    #Make a layers section kinda like photoshop or like bluebeam. where everything you add can be taken away or changed

if __name__ == "__main__":
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    pyqtRemoveInputHook()
    app = QtWidgets.QApplication(sys.argv)
    app.setAttribute(Qt.AA_EnableHighDpiScaling,True)
    screen_resolution = app.desktop().screenGeometry()
    width, height = screen_resolution.width()/1.5, screen_resolution.height()/1.2
    MainWindow = MainWindow()
    MainWindow.resize(width,height)
    MainWindow.setWindowTitle('Figure out name later')
    MainWindow.show()
    sys.exit(app.exec_())
