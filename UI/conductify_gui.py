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
        Form.resize(1128, 1000)
        Form.setStyleSheet("background-color: #6898a4;")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(250, 900, 601, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.searchInput = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget)
        self.searchInput.setObjectName("searchInput")
        self.searchInput.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.horizontalLayout.addWidget(self.searchInput)
        self.search = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.search.setStyleSheet("""
            QPushButton {
                background-color: rgb(125, 125, 125);
                border-style: outset;
                border-width: 2px;
                border-radius: 10px;
                border-color: beige;
                font: bold 20px;
                min-width: 10em;
                padding: 6px;
            }
            QPushButton:pressed {
                background-color: rgb(150, 150, 150);
                border-style: inset;
        }""")
        self.search.setObjectName("search")
        self.horizontalLayout.addWidget(self.search)
        self.horizontalLayoutWidget.raise_()
        self.searchInput.raise_()
        self.searchInput.raise_()

        self.start_pushButton = QtWidgets.QPushButton(Form)
        self.start_pushButton.setGeometry(QtCore.QRect(120, 760, 291, 91))
        self.start_pushButton.setObjectName("start_pushButton")
        self.start_pushButton.setStyleSheet("""
            QPushButton {
                background-color: green;
                border-style: outset;
                border-width: 2px;
                border-radius: 10px;
                border-color: beige;
                font: bold 30px;
                min-width: 10em;
                padding: 6px;
                }
            QPushButton:pressed {
                background-color: rgb(0, 250, 0);
                border-style: inset;
        }""")
        self.stop_pushButton = QtWidgets.QPushButton(Form)
        self.stop_pushButton.setGeometry(QtCore.QRect(720, 760, 291, 91))
        self.stop_pushButton.setObjectName("stop_pushButton")
        self.stop_pushButton.setStyleSheet("""
            QPushButton {
                background-color: rgb(125, 0, 0);
                border-style: outset;
                border-width: 2px;
                border-radius: 10px;
                border-color: beige;
                font: bold 30px;
                min-width: 10em;
                padding: 6px;
            }
            QPushButton:pressed {
                background-color: rgb(250, 0, 0);
                border-style: inset;
        }""")

        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 20, 1081, 541))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.otherBar = QtWidgets.QProgressBar(self.horizontalLayoutWidget)
        self.otherBar.setProperty("value", 100)
        self.otherBar.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.otherBar.setTextVisible(False)
        self.otherBar.setOrientation(QtCore.Qt.Vertical)
        self.otherBar.setObjectName("otherBar")
        self.otherBar.setStyleSheet("""
                                QProgressBar {
                                    border: 6px solid grey;
                                    border-radius: 7px;

                                }
                                QProgressBar::chunk {
                                    background-color: #0064c8
                                }
        """)
        self.horizontalLayout.addWidget(self.otherBar)
        self.drumsBar = QtWidgets.QProgressBar(self.horizontalLayoutWidget)
        self.drumsBar.setProperty("value", 100)
        self.drumsBar.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.drumsBar.setTextVisible(False)
        self.drumsBar.setOrientation(QtCore.Qt.Vertical)
        self.drumsBar.setObjectName("drumsBar")
        self.drumsBar.setStyleSheet("""
                                QProgressBar {
                                    border: 6px solid grey;
                                    border-radius: 7px;

                                }
                                QProgressBar::chunk {
                                    background-color: #0064c8
                                }
        """)

        self.horizontalLayout.addWidget(self.drumsBar)
        self.pianoBar = QtWidgets.QProgressBar(self.horizontalLayoutWidget)
        self.pianoBar.setProperty("value", 100)
        self.pianoBar.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.pianoBar.setTextVisible(False)
        self.pianoBar.setOrientation(QtCore.Qt.Vertical)
        self.pianoBar.setObjectName("pianoBar")
        self.pianoBar.setStyleSheet("""
                                QProgressBar {
                                    border: 6px solid grey;
                                    border-radius: 7px;

                                }
                                QProgressBar::chunk {
                                    background-color: #0064c8
                                }
        """)
        self.horizontalLayout.addWidget(self.pianoBar)
        self.bassBar = QtWidgets.QProgressBar(self.horizontalLayoutWidget)
        self.bassBar.setProperty("value", 100)
        self.bassBar.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.bassBar.setTextVisible(False)
        self.bassBar.setOrientation(QtCore.Qt.Vertical)
        self.bassBar.setObjectName("bassBar")
        self.bassBar.setStyleSheet("""
                                QProgressBar {
                                    border: 6px solid grey;
                                    border-radius: 7px;

                                }
                                QProgressBar::chunk {
                                    background-color: #0064c8
                                }
        """)

        self.horizontalLayout.addWidget(self.bassBar)
        self.vocalsBar = QtWidgets.QProgressBar(self.horizontalLayoutWidget)
        self.vocalsBar.setProperty("value", 100)
        self.vocalsBar.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.vocalsBar.setTextVisible(False)
        self.vocalsBar.setOrientation(QtCore.Qt.Vertical)
        self.vocalsBar.setObjectName("vocalsBar")
        self.vocalsBar.setStyleSheet("""
                                QProgressBar {
                                    border: 6px solid grey;
                                    border-radius: 7px;

                                }
                                QProgressBar::chunk {
                                    background-color: #0064c8
                                }
        """)

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

        pixOther = QPixmap('UI/other.png')
        pixOther = pixOther.scaled(self.otherLabel.width(), self.otherLabel.height(), QtCore.Qt.KeepAspectRatio)

        pixDrums = QPixmap('UI/drums.png')
        pixDrums = pixDrums.scaled(self.drumLabel.width(), self.drumLabel.height(), QtCore.Qt.KeepAspectRatio)

        pixBass = QPixmap('UI/bass.png')
        pixBass = pixBass.scaled(self.bassLabel.width(), self.bassLabel.height(), QtCore.Qt.KeepAspectRatio)

        pixPiano = QPixmap("UI/piano.png")
        pixPiano = pixPiano.scaled(self.pianoLabel.width(), self.pianoLabel.height(), QtCore.Qt.KeepAspectRatio)

        pixVocals = QPixmap("UI/vocals.png")
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
        self.start_pushButton.setText(_translate("Form", " PLAY"))
        self.stop_pushButton.setText(_translate("Form", "STOP"))
        self.drumLabel.setText(_translate("Form", "piano"))
        self.pianoLabel.setText(_translate("Form", "drums"))
        self.bassLabel.setText(_translate("Form", "bass"))
        self.vocalsLabel.setText(_translate("Form", "vocals"))
        self.search.setText(_translate("Form", "Search"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
