# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'userInterface.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(412, 462)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 10, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 140, 47, 13))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 170, 61, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 200, 61, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 230, 61, 16))
        self.label_7.setObjectName("label_7")
        self.rad1LineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.rad1LineEdit.setGeometry(QtCore.QRect(80, 80, 31, 20))
        self.rad1LineEdit.setObjectName("rad1LineEdit")
        self.rad2LineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.rad2LineEdit.setGeometry(QtCore.QRect(80, 110, 31, 20))
        self.rad2LineEdit.setObjectName("rad2LineEdit")
        self.rad3LineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.rad3LineEdit.setGeometry(QtCore.QRect(80, 140, 31, 20))
        self.rad3LineEdit.setObjectName("rad3LineEdit")
        self.diam1LineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.diam1LineEdit.setGeometry(QtCore.QRect(80, 170, 31, 20))
        self.diam1LineEdit.setObjectName("diam1LineEdit")
        self.diam2LineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.diam2LineEdit.setGeometry(QtCore.QRect(80, 200, 31, 20))
        self.diam2LineEdit.setObjectName("diam2LineEdit")
        self.diam3LineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.diam3LineEdit.setGeometry(QtCore.QRect(80, 230, 31, 20))
        self.diam3LineEdit.setObjectName("diam3LineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 350, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(280, 380, 61, 31))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("logo.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(40, 340, 61, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(40, 370, 111, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(140, 80, 71, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(140, 110, 71, 16))
        self.label_12.setObjectName("label_12")
        self.linealIndexLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.linealIndexLineEdit.setGeometry(QtCore.QRect(210, 80, 31, 20))
        self.linealIndexLineEdit.setObjectName("linealIndexLineEdit")
        self.radialIndexLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.radialIndexLineEdit.setGeometry(QtCore.QRect(210, 110, 31, 20))
        self.radialIndexLineEdit.setObjectName("radialIndexLineEdit")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(140, 230, 61, 16))
        self.label_13.setObjectName("label_13")
        self.dryBut = QtWidgets.QRadioButton(self.centralwidget)
        self.dryBut.setGeometry(QtCore.QRect(260, 80, 121, 17))
        self.dryBut.setObjectName("dryBut")
        self.moistBut = QtWidgets.QRadioButton(self.centralwidget)
        self.moistBut.setGeometry(QtCore.QRect(260, 110, 131, 17))
        self.moistBut.setObjectName("moistBut")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(140, 260, 47, 13))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(140, 290, 47, 13))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(140, 320, 47, 13))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(250, 260, 61, 16))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(250, 290, 61, 16))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(250, 320, 61, 16))
        self.label_19.setObjectName("label_19")
        self.rad1ans = QtWidgets.QLabel(self.centralwidget)
        self.rad1ans.setGeometry(QtCore.QRect(190, 260, 47, 13))
        self.rad1ans.setObjectName("rad1ans")
        self.rad2ans = QtWidgets.QLabel(self.centralwidget)
        self.rad2ans.setGeometry(QtCore.QRect(190, 290, 47, 13))
        self.rad2ans.setObjectName("rad2ans")
        self.rad3ans = QtWidgets.QLabel(self.centralwidget)
        self.rad3ans.setGeometry(QtCore.QRect(190, 320, 47, 13))
        self.rad3ans.setObjectName("rad3ans")
        self.diam1Ans = QtWidgets.QLabel(self.centralwidget)
        self.diam1Ans.setGeometry(QtCore.QRect(320, 260, 47, 13))
        self.diam1Ans.setObjectName("diam1Ans")
        self.diam2Ans = QtWidgets.QLabel(self.centralwidget)
        self.diam2Ans.setGeometry(QtCore.QRect(320, 290, 47, 13))
        self.diam2Ans.setObjectName("diam2Ans")
        self.diam3Ans = QtWidgets.QLabel(self.centralwidget)
        self.diam3Ans.setGeometry(QtCore.QRect(320, 320, 47, 13))
        self.diam3Ans.setObjectName("diam3Ans")
        self.sag1LineEdit = QtWidgets.QLabel(self.centralwidget)
        self.sag1LineEdit.setGeometry(QtCore.QRect(160, 370, 71, 16))
        self.sag1LineEdit.setObjectName("sag1LineEdit")
        self.calcRad = QtWidgets.QCheckBox(self.centralwidget)
        self.calcRad.setGeometry(QtCore.QRect(140, 140, 161, 17))
        self.calcRad.setObjectName("calcRad")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(140, 170, 101, 16))
        self.label_20.setObjectName("label_20")
        self.sagInput = QtWidgets.QLineEdit(self.centralwidget)
        self.sagInput.setGeometry(QtCore.QRect(250, 170, 41, 20))
        self.sagInput.setObjectName("sagInput")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(140, 200, 101, 16))
        self.label_21.setObjectName("label_21")
        self.sag2Input = QtWidgets.QLineEdit(self.centralwidget)
        self.sag2Input.setGeometry(QtCore.QRect(250, 200, 41, 20))
        self.sag2Input.setObjectName("sag2Input")
        self.sagTotal = QtWidgets.QLabel(self.centralwidget)
        self.sagTotal.setGeometry(QtCore.QRect(160, 340, 91, 16))
        self.sagTotal.setObjectName("sagTotal")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 412, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Graficador de Lentes Diaz"))
        self.label.setText(_translate("MainWindow", "Por favor, ingrese las especificaciones"))
        self.label_2.setText(_translate("MainWindow", "Radio 1:"))
        self.label_3.setText(_translate("MainWindow", "Radio 2:"))
        self.label_4.setText(_translate("MainWindow", "Radio 3:"))
        self.label_5.setText(_translate("MainWindow", "Diametro 1:"))
        self.label_6.setText(_translate("MainWindow", "Diametrol 2:"))
        self.label_7.setText(_translate("MainWindow", "Diametrol 3:"))
        self.pushButton.setText(_translate("MainWindow", "Graficar"))
        self.label_9.setText(_translate("MainWindow", "Sagital Total:"))
        self.label_10.setText(_translate("MainWindow", "Sagital 1er diametro:"))
        self.label_11.setText(_translate("MainWindow", "Indice Lineal"))
        self.label_12.setText(_translate("MainWindow", "Indice Radial"))
        self.label_13.setText(_translate("MainWindow", "Resultados"))
        self.dryBut.setText(_translate("MainWindow", "Calcular en seco"))
        self.moistBut.setText(_translate("MainWindow", "Calcular en hidratado"))
        self.label_14.setText(_translate("MainWindow", "Radio 1"))
        self.label_15.setText(_translate("MainWindow", "Radio 2"))
        self.label_16.setText(_translate("MainWindow", "Radio 3"))
        self.label_17.setText(_translate("MainWindow", "Diametro 1"))
        self.label_18.setText(_translate("MainWindow", "Diametro 2"))
        self.label_19.setText(_translate("MainWindow", "Diametro 3"))
        self.rad1ans.setText(_translate("MainWindow", "Valor"))
        self.rad2ans.setText(_translate("MainWindow", "Valor"))
        self.rad3ans.setText(_translate("MainWindow", "Valor"))
        self.diam1Ans.setText(_translate("MainWindow", "Valor"))
        self.diam2Ans.setText(_translate("MainWindow", "Valor"))
        self.diam3Ans.setText(_translate("MainWindow", "Valor"))
        self.sag1LineEdit.setText(_translate("MainWindow", "Valor"))
        self.calcRad.setText(_translate("MainWindow", "Calcular Radios con sagital"))
        self.label_20.setText(_translate("MainWindow", "Sagital 1er diametro:"))
        self.label_21.setText(_translate("MainWindow", "Sagital 2do diametro:"))
        self.sagTotal.setText(_translate("MainWindow", "Valor"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
