# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 250)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setIconSize(QtCore.QSize(0, 0))
        MainWindow.setAnimated(True)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.beginAtSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.beginAtSpinBox.setGeometry(QtCore.QRect(70, 10, 51, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.beginAtSpinBox.setFont(font)
        self.beginAtSpinBox.setMouseTracking(False)
        self.beginAtSpinBox.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.beginAtSpinBox.setAcceptDrops(False)
        self.beginAtSpinBox.setToolTip("")
        self.beginAtSpinBox.setMinimum(1)
        self.beginAtSpinBox.setMaximum(9999)
        self.beginAtSpinBox.setObjectName("beginAtSpinBox")
        self.endAtSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.endAtSpinBox.setGeometry(QtCore.QRect(70, 51, 40, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.endAtSpinBox.setFont(font)
        self.endAtSpinBox.setMouseTracking(False)
        self.endAtSpinBox.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.endAtSpinBox.setAcceptDrops(False)
        self.endAtSpinBox.setToolTip("")
        self.endAtSpinBox.setToolTipDuration(2)
        self.endAtSpinBox.setStatusTip("")
        self.endAtSpinBox.setMinimum(100)
        self.endAtSpinBox.setMaximum(9999)
        self.endAtSpinBox.setObjectName("endAtSpinBox")
        self.beginAtLabel = QtWidgets.QLabel(self.centralwidget)
        self.beginAtLabel.setGeometry(QtCore.QRect(16, 10, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.beginAtLabel.setFont(font)
        self.beginAtLabel.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.beginAtLabel.setToolTip("")
        self.beginAtLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.beginAtLabel.setObjectName("beginAtLabel")
        self.endAtLabel = QtWidgets.QLabel(self.centralwidget)
        self.endAtLabel.setGeometry(QtCore.QRect(20, 40, 47, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.endAtLabel.setFont(font)
        self.endAtLabel.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.endAtLabel.setToolTip("")
        self.endAtLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.endAtLabel.setScaledContents(False)
        self.endAtLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.endAtLabel.setObjectName("endAtLabel")
        self.helpLabel = QtWidgets.QLabel(self.centralwidget)
        self.helpLabel.setGeometry(QtCore.QRect(20, 110, 381, 111))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.helpLabel.setFont(font)
        self.helpLabel.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.helpLabel.setToolTip("")
        self.helpLabel.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.helpLabel.setWordWrap(True)
        self.helpLabel.setObjectName("helpLabel")
        self.modeComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.modeComboBox.setGeometry(QtCore.QRect(210, 10, 51, 20))
        self.modeComboBox.setEditable(False)
        self.modeComboBox.setCurrentText("JJ/GJ")
        self.modeComboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.modeComboBox.setMinimumContentsLength(1)
        self.modeComboBox.setFrame(True)
        self.modeComboBox.setObjectName("modeComboBox")
        self.modeComboBox.addItem("")
        self.modeComboBox.addItem("")
        self.modeComboBox.addItem("")
        self.modeComboBox.addItem("")
        self.jackTypeLabel = QtWidgets.QLabel(self.centralwidget)
        self.jackTypeLabel.setGeometry(QtCore.QRect(140, 10, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.jackTypeLabel.setFont(font)
        self.jackTypeLabel.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.jackTypeLabel.setToolTip("")
        self.jackTypeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.jackTypeLabel.setObjectName("jackTypeLabel")
        self.capitalizationComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.capitalizationComboBox.setGeometry(QtCore.QRect(210, 40, 51, 22))
        self.capitalizationComboBox.setObjectName("capitalizationComboBox")
        self.capitalizationComboBox.addItem("")
        self.capitalizationComboBox.addItem("")
        self.capitalizationComboBox.addItem("")
        self.capitalizationLabel = QtWidgets.QLabel(self.centralwidget)
        self.capitalizationLabel.setGeometry(QtCore.QRect(120, 40, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.capitalizationLabel.setFont(font)
        self.capitalizationLabel.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.capitalizationLabel.setToolTip("")
        self.capitalizationLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.capitalizationLabel.setObjectName("capitalizationLabel")
        self.punctuationLabel = QtWidgets.QLabel(self.centralwidget)
        self.punctuationLabel.setGeometry(QtCore.QRect(260, 10, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.punctuationLabel.setFont(font)
        self.punctuationLabel.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.punctuationLabel.setToolTip("")
        self.punctuationLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.punctuationLabel.setObjectName("punctuationLabel")
        self.punctuationTextBox = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.punctuationTextBox.setGeometry(QtCore.QRect(340, 10, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.punctuationTextBox.setFont(font)
        self.punctuationTextBox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.punctuationTextBox.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.punctuationTextBox.setUndoRedoEnabled(False)
        self.punctuationTextBox.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.punctuationTextBox.setPlainText("")
        self.punctuationTextBox.setOverwriteMode(False)
        self.punctuationTextBox.setCenterOnScroll(False)
        self.punctuationTextBox.setPlaceholderText("")
        self.punctuationTextBox.setObjectName("punctuationTextBox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(120, 70, 181, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.startStopLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.startStopLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.startStopLayout.setContentsMargins(0, 0, 0, 0)
        self.startStopLayout.setSpacing(0)
        self.startStopLayout.setObjectName("startStopLayout")
        self.startButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.startButton.setObjectName("startButton")
        self.startStopLayout.addWidget(self.startButton)
        self.stopButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.stopButton.setObjectName("stopButton")
        self.startStopLayout.addWidget(self.stopButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.modeComboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Bot"))
        self.beginAtLabel.setText(_translate("MainWindow", "Başlangıç:"))
        self.endAtLabel.setText(_translate("MainWindow", "Bitiş:"))
        self.helpLabel.setText(_translate("MainWindow", "Yadashi#1883 / waez0ne#9121"))
        self.modeComboBox.setItemText(0, _translate("MainWindow", "JJ/GJ"))
        self.modeComboBox.setItemText(1, _translate("MainWindow", "HJ"))
        self.modeComboBox.setItemText(2, _translate("MainWindow", "DJ"))
        self.modeComboBox.setItemText(3, _translate("MainWindow", "CJ"))
        self.jackTypeLabel.setText(_translate("MainWindow", "Jack Type:"))
        self.capitalizationComboBox.setItemText(0, _translate("MainWindow", "BİR"))
        self.capitalizationComboBox.setItemText(1, _translate("MainWindow", "İki"))
        self.capitalizationComboBox.setItemText(2, _translate("MainWindow", "üç"))
        self.capitalizationLabel.setText(_translate("MainWindow", "Capitalization:"))
        self.punctuationLabel.setText(_translate("MainWindow", "Punctuation:"))
        self.startButton.setText(_translate("MainWindow", "Başla"))
        self.stopButton.setText(_translate("MainWindow", "Durdur"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())