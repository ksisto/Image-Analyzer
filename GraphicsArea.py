import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from GraphicsArea_GUI import *
from QGraphicsView import *
import Constents


class LogObject(QObject):
    MousePixmapSignal = pyqtSignal(QPoint, QColor)
    pointDraw = pyqtSignal(QPoint)

class PictureItem(QGraphicsPixmapItem):

    def __init__(self, log,*args, **kwargs):
        QGraphicsPixmapItem.__init__(self,*args, **kwargs)
        self.setAcceptHoverEvents(True)
        self.log = log


    def hoverMoveEvent(self, event):
        point = event.pos().toPoint()
        color = QColor(self.pixmap().toImage().pixel(point.x(), point.y()))
        self.log.MousePixmapSignal.emit(point, color)
        QGraphicsPixmapItem.hoverMoveEvent(self, event)

    def hoverEnterEvent(self, event):
        QApplication.setOverrideCursor(Qt.CrossCursor)
        QGraphicsPixmapItem.hoverMoveEvent(self, event)

    def hoverLeaveEvent(self, event):
        QApplication.setOverrideCursor(Qt.ArrowCursor)
        QGraphicsPixmapItem.hoverLeaveEvent(self, event)

    def mousePressEvent(self,event):
        point = event.pos().toPoint()
        self.log.pointDraw.emit(point)
        QGraphicsPixmapItem.mousePressEvent(self, event)




class LoadPicture(QWidget, Ui_GraphicsArea):
    def __init__(self, pixmap, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.pixmap = pixmap
        self.log = LogObject(self)
        self.scene = self.PictureArea.setScene(QGraphicsScene())
        self.item = PictureItem(self.log,pixmap)
        self.PictureArea.scene().addItem(self.item)
        self.resize(pixmap.size())
        self.log.pointDraw.connect(self.drawCircle)




    def drawCircle(self,pos):
        pen = QPen(QColor(Qt.red))
        ellipse = QGraphicsEllipseItem(-5,5,10,-10)
        #ellipse.setObjectName("Ellipse_"+ self.variables.analysisCount)
        ellipse.setPen(pen)
        self.PictureArea.scene().addItem(ellipse)
        ellipse.setPos(pos.x(),pos.y())
        Constents.analysisDetails[str(Constents.analysisCount)]=[pos.x(),pos.y()]


    def findAndRemoveAnalysisPoint(self,posX,posY):
        ellipseFound = self.PictureArea.itemAt(posX,posY)
        self.PictureArea.scene().removeItem(ellipseFound)
        #return ellipseFound
