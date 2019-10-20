# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/widget.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(900, 600)
        Form.setMinimumSize(QtCore.QSize(900, 600))
        Form.setMaximumSize(QtCore.QSize(900, 600))
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setMaximumSize(QtCore.QSize(294, 16777215))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(500)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout_2.addWidget(self.spinBox, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.spinBox_2 = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_2.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.spinBox_2.setMinimum(10)
        self.spinBox_2.setMaximum(1000)
        self.spinBox_2.setProperty("value", 100)
        self.spinBox_2.setObjectName("spinBox_2")
        self.gridLayout_2.addWidget(self.spinBox_2, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 4, 0, 1, 1)
        self.listWidget = QtWidgets.QListWidget(self.groupBox_2)
        self.listWidget.setMinimumSize(QtCore.QSize(0, 300))
        self.listWidget.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_2.addWidget(self.listWidget, 5, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 397, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 6, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.gridLayout_2.addLayout(self.horizontalLayout, 7, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 2, 1, 1, 1)
        self.graphicsView = QtWidgets.QGraphicsView(Form)
        self.graphicsView.setMaximumSize(QtCore.QSize(588, 16777215))
        self.graphicsView.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 0, 0, 3, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Snake"))
        self.groupBox_2.setTitle(_translate("Form", "Game"))
        self.label.setText(_translate("Form", "Food items count"))
        self.label_2.setText(_translate("Form", "Update timeout (miliseconds)"))
        self.label_3.setText(_translate("Form", "Statistic"))
        self.pushButton.setText(_translate("Form", "Play"))
        self.pushButton_2.setText(_translate("Form", "Pause"))
