# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_remove.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_Edit(object):
    def setupUi(self, Edit):
        Edit.setObjectName("Edit")
        Edit.resize(1200, 700)
        Edit.setStyleSheet("background: #FFFFFF;")
        Edit.setSizeGripEnabled(False)
        self.frame = QtWidgets.QFrame(Edit)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1201, 701))
        self.frame.setStyleSheet("background:#D8F8E8;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lbl_appsts = QtWidgets.QLabel(self.frame)
        self.lbl_appsts.setGeometry(QtCore.QRect(570, 10, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_appsts.setFont(font)
        self.lbl_appsts.setStyleSheet("color: rgb(0, 0, 0)\n"
"")
        self.lbl_appsts.setObjectName("lbl_appsts")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(100, 200, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(100, 140, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(730, 140, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(730, 200, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(280, 145, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(280, 205, 171, 31))
        self.lineEdit.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(200, 280, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.pushButton.setObjectName("pushButton")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame)
        self.comboBox_2.setGeometry(QtCore.QRect(890, 210, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(850, 280, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(100, 380, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(100, 440, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(100, 500, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.comboBox_3 = QtWidgets.QComboBox(self.frame)
        self.comboBox_3.setGeometry(QtCore.QRect(280, 385, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(280, 510, 171, 31))
        self.lineEdit_2.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(730, 490, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(730, 430, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(730, 370, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.comboBox_6 = QtWidgets.QComboBox(self.frame)
        self.comboBox_6.setGeometry(QtCore.QRect(900, 375, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_6.setFont(font)
        self.comboBox_6.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_7 = QtWidgets.QComboBox(self.frame)
        self.comboBox_7.setGeometry(QtCore.QRect(900, 495, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_7.setFont(font)
        self.comboBox_7.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.comboBox_7.setObjectName("comboBox_7")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 570, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(860, 560, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.pushButton_4.setObjectName("pushButton_4")
        self.comboBox_8 = QtWidgets.QComboBox(self.frame)
        self.comboBox_8.setGeometry(QtCore.QRect(890, 150, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_8.setFont(font)
        self.comboBox_8.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_9 = QtWidgets.QComboBox(self.frame)
        self.comboBox_9.setGeometry(QtCore.QRect(280, 450, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_9.setFont(font)
        self.comboBox_9.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.comboBox_9.setObjectName("comboBox_9")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_4 = QtWidgets.QComboBox(self.frame)
        self.comboBox_4.setGeometry(QtCore.QRect(900, 437, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_4.setFont(font)
        self.comboBox_4.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.btn_bck = QtWidgets.QPushButton(self.frame)
        self.btn_bck.setGeometry(QtCore.QRect(530, 630, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_bck.setFont(font)
        self.btn_bck.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.btn_bck.setObjectName("btn_bck")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(570, 85, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(570, 330, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")

        self.retranslateUi(Edit)
        QtCore.QMetaObject.connectSlotsByName(Edit)

    def retranslateUi(self, Edit):
        _translate = QtCore.QCoreApplication.translate
        Edit.setWindowTitle(_translate("Edit", "Dialog"))
        self.lbl_appsts.setText(_translate("Edit", "Edit"))
        self.label_2.setText(_translate("Edit", "Company :"))
        self.label_3.setText(_translate("Edit", "Job Profile :"))
        self.label_4.setText(_translate("Edit", "Job Profile :"))
        self.label_5.setText(_translate("Edit", "Company :"))
        self.comboBox.setItemText(0, _translate("Edit", "IT/CS"))
        self.comboBox.setItemText(1, _translate("Edit", "Mechanical"))
        self.comboBox.setItemText(2, _translate("Edit", "Civil"))
        self.comboBox.setItemText(3, _translate("Edit", "Extc"))
        self.pushButton.setText(_translate("Edit", "Add"))
        self.comboBox_2.setItemText(0, _translate("Edit", "TCS"))
        self.comboBox_2.setItemText(1, _translate("Edit", "WIPRO"))
        self.comboBox_2.setItemText(2, _translate("Edit", "INFOSYS"))
        self.pushButton_2.setText(_translate("Edit", "Remove"))
        self.label_6.setText(_translate("Edit", "Job Profile :"))
        self.label_7.setText(_translate("Edit", "Company :"))
        self.label_8.setText(_translate("Edit", "Job Role :"))
        self.comboBox_3.setItemText(0, _translate("Edit", "IT/CS"))
        self.comboBox_3.setItemText(1, _translate("Edit", "Mechanical"))
        self.comboBox_3.setItemText(2, _translate("Edit", "Civil"))
        self.comboBox_3.setItemText(3, _translate("Edit", "Extc"))
        self.label_9.setText(_translate("Edit", "Job Role :"))
        self.label_10.setText(_translate("Edit", "Company :"))
        self.label_11.setText(_translate("Edit", "Job Profile :"))
        self.comboBox_6.setItemText(0, _translate("Edit", "IT/CS"))
        self.comboBox_6.setItemText(1, _translate("Edit", "Mechanical"))
        self.comboBox_6.setItemText(2, _translate("Edit", "Civil"))
        self.comboBox_6.setItemText(3, _translate("Edit", "Extc"))
        self.pushButton_3.setText(_translate("Edit", "Add"))
        self.pushButton_4.setText(_translate("Edit", "Remove"))
        self.comboBox_8.setItemText(0, _translate("Edit", "IT/CS"))
        self.comboBox_8.setItemText(1, _translate("Edit", "Mechanical"))
        self.comboBox_8.setItemText(2, _translate("Edit", "Civil"))
        self.comboBox_8.setItemText(3, _translate("Edit", "Extc"))
        self.comboBox_9.setItemText(0, _translate("Edit", "TCS"))
        self.comboBox_9.setItemText(1, _translate("Edit", "WIPRO"))
        self.comboBox_9.setItemText(2, _translate("Edit", "INFOSYS"))
        self.comboBox_4.setItemText(0, _translate("Edit", "TCS"))
        self.comboBox_4.setItemText(1, _translate("Edit", "WIPRO"))
        self.comboBox_4.setItemText(2, _translate("Edit", "INFOSYS"))
        self.btn_bck.setText(_translate("Edit", "Back"))
        self.label.setText(_translate("Edit", "Company"))
        self.label_12.setText(_translate("Edit", "Job"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Edit = QtWidgets.QDialog()
    ui = Ui_Edit()
    ui.setupUi(Edit)
    Edit.show()
    sys.exit(app.exec_())
