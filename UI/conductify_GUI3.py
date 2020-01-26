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
        Form.resize(1128, 863)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(120, 760, 291, 91))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(720, 760, 291, 91))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 20, 1081, 541))
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
        self.otherLabel = QtWidgets.QLabel(Form)
        self.otherLabel.setGeometry(QtCore.QRect(140, 590, 101, 141))
        self.otherLabel.setText("")
        self.otherLabel.setObjectName("otherLabel")
        self.drumLabel = QtWidgets.QLabel(Form)
        self.drumLabel.setGeometry(QtCore.QRect(330, 590, 101, 141))
        self.drumLabel.setObjectName("drumLabel")
        self.pianoLabel = QtWidgets.QLabel(Form)
        self.pianoLabel.setGeometry(QtCore.QRect(530, 590, 91, 141))
        self.pianoLabel.setObjectName("pianoLabel")
        self.bassLabel = QtWidgets.QLabel(Form)
        self.bassLabel.setGeometry(QtCore.QRect(710, 590, 91, 141))
        self.bassLabel.setObjectName("bassLabel")
        self.vocalsLabel = QtWidgets.QLabel(Form)
        self.vocalsLabel.setGeometry(QtCore.QRect(900, 590, 91, 141))
        self.vocalsLabel.setObjectName("vocalsLabel")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        pixOther = QPixmap('other.png')
        pixOther = pixOther.scaled(self.otherLabel.width(), self.otherLabel.height(), QtCore.Qt.KeepAspectRatio)

        pixDrums = QPixmap('drums.png')
        pixDrums = pixDrums.scaled(self.drumLabel.width(), self.drumLabel.height(), QtCore.Qt.KeepAspectRatio)

        pixBass = QPixmap('bass.png')
        pixBass = pixBass.scaled(self.bassLabel.width(), self.bassLabel.height(), QtCore.Qt.KeepAspectRatio)

        pixPiano = QPixmap("piano.png")
        pixPiano = pixPiano.scaled(self.pianoLabel.width(), self.pianoLabel.height(), QtCore.Qt.KeepAspectRatio)

        pixVocals = QPixmap("vocals.png")
        pixVocals = pixVocals.scaled(self.vocalsLabel.width(), self.vocalsLabel.height(), QtCore.Qt.KeepAspectRatio)

        self.otherLabel.setPixmap(pixOther)
        self.otherLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.drumLabel.setPixmap(pixDrums)
        self.drumLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.bassLabel.setPixmap(pixBass)
        self.bassLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.vocalsLabel.setPixmap(pixVocals)
        self.vocalsLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.pianoLabel.setPixmap(pixPiano)
        self.pianoLabel.setAlignment(QtCore.Qt.AlignCenter)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Play"))
        self.pushButton_2.setText(_translate("Form", "Pause"))
        self.drumLabel.setText(_translate("Form", "piano"))
        self.pianoLabel.setText(_translate("Form", "drums"))
        self.bassLabel.setText(_translate("Form", "bass"))
        self.vocalsLabel.setText(_translate("Form", "vocals"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
