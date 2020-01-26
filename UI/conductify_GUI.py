# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\gladi\Desktop\conductify-ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1168, 863)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(260, 770, 291, 91))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(680, 770, 291, 91))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 1161, 541))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.otherBar = QtWidgets.QProgressBar(self.horizontalLayoutWidget)
        self.otherBar.setProperty("value", 24)
        self.otherBar.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.otherBar.setTextVisible(False)
        self.otherBar.setOrientation(QtCore.Qt.Vertical)
        self.otherBar.setObjectName("otherBar")
        self.horizontalLayout.addWidget(self.otherBar)
        self.drumsBar = QtWidgets.QProgressBar(self.horizontalLayoutWidget)
        self.drumsBar.setProperty("value", 24)
        self.drumsBar.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.drumsBar.setTextVisible(False)
        self.drumsBar.setOrientation(QtCore.Qt.Vertical)
        self.drumsBar.setObjectName("drumsBar")
        self.horizontalLayout.addWidget(self.drumsBar)
        self.pianoBar = QtWidgets.QProgressBar(self.horizontalLayoutWidget)
        self.pianoBar.setProperty("value", 24)
        self.pianoBar.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.pianoBar.setTextVisible(False)
        self.pianoBar.setOrientation(QtCore.Qt.Vertical)
        self.pianoBar.setObjectName("pianoBar")
        self.horizontalLayout.addWidget(self.pianoBar)
        self.bassBar = QtWidgets.QProgressBar(self.horizontalLayoutWidget)
        self.bassBar.setProperty("value", 24)
        self.bassBar.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.bassBar.setTextVisible(False)
        self.bassBar.setOrientation(QtCore.Qt.Vertical)
        self.bassBar.setObjectName("bassBar")
        self.horizontalLayout.addWidget(self.bassBar)
        self.vocalsBar = QtWidgets.QProgressBar(self.horizontalLayoutWidget)
        self.vocalsBar.setProperty("value", 24)
        self.vocalsBar.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.vocalsBar.setTextVisible(False)
        self.vocalsBar.setOrientation(QtCore.Qt.Vertical)
        self.vocalsBar.setObjectName("vocalsBar")
        self.horizontalLayout.addWidget(self.vocalsBar)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 560, 1161, 171))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        pixOther = QPixmap('other.png')
        pixDrums = QPixmap('drums.png')
        pixBass = QPixmap('bass.png')
        pixPiano = QPixmap("piano.png")
        pixVocals = QPixmap("vocals.png")

        self.label.setPixmap(pixOther)
        self.label_2.setPixmap(pixDrums)
        self.label_3.setPixmap(pixBass)
        self.label_4.setPixmap(pixVocals)
        self.label_5.setPixmap(pixPiano)




    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Play"))
        self.pushButton_2.setText(_translate("Form", "Pause"))
        self.label.setText(_translate("Form", "otherLabel"))
        self.label_5.setText(_translate("Form", "drumsLabel"))
        self.label_4.setText(_translate("Form", "pianoLabel"))
        self.label_3.setText(_translate("Form", "bassLabel"))
        self.label_2.setText(_translate("Form", "vocalsLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
