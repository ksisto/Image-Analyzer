# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'History_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_History_Item(object):
    def setupUi(self, History_Item):
        History_Item.setObjectName("History_Item")
        History_Item.resize(176, 83)
        self.verticalLayout = QtWidgets.QVBoxLayout(History_Item)
        self.verticalLayout.setObjectName("verticalLayout")
        self.txt_point = QtWidgets.QLabel(History_Item)
        self.txt_point.setObjectName("txt_point")
        self.verticalLayout.addWidget(self.txt_point)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.txt_X = QtWidgets.QLabel(History_Item)
        self.txt_X.setObjectName("txt_X")
        self.horizontalLayout.addWidget(self.txt_X)
        self.txt_XChange = QtWidgets.QLabel(History_Item)
        self.txt_XChange.setObjectName("txt_XChange")
        self.horizontalLayout.addWidget(self.txt_XChange)
        self.txt_Y = QtWidgets.QLabel(History_Item)
        self.txt_Y.setObjectName("txt_Y")
        self.horizontalLayout.addWidget(self.txt_Y)
        self.txt_YChange = QtWidgets.QLabel(History_Item)
        self.txt_YChange.setObjectName("txt_YChange")
        self.horizontalLayout.addWidget(self.txt_YChange)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Button_Move = QtWidgets.QPushButton(History_Item)
        self.Button_Move.setObjectName("Button_Move")
        self.horizontalLayout_2.addWidget(self.Button_Move)
        self.Button_Delete = QtWidgets.QPushButton(History_Item)
        self.Button_Delete.setObjectName("Button_Delete")
        self.horizontalLayout_2.addWidget(self.Button_Delete)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(History_Item)
        QtCore.QMetaObject.connectSlotsByName(History_Item)

    def retranslateUi(self, History_Item):
        _translate = QtCore.QCoreApplication.translate
        History_Item.setWindowTitle(_translate("History_Item", "Form"))
        self.txt_point.setText(_translate("History_Item", "Point 1"))
        self.txt_X.setText(_translate("History_Item", "X:"))
        self.txt_XChange.setText(_translate("History_Item", "TextLabel"))
        self.txt_Y.setText(_translate("History_Item", "Y:"))
        self.txt_YChange.setText(_translate("History_Item", "TextLabel"))
        self.Button_Move.setText(_translate("History_Item", "Move"))
        self.Button_Delete.setText(_translate("History_Item", "Delete"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    History_Item = QtWidgets.QWidget()
    ui = Ui_History_Item()
    ui.setupUi(History_Item)
    History_Item.show()
    sys.exit(app.exec_())

