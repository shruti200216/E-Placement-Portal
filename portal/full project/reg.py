# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reg.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as mc
from PyQt5.QtWidgets import QMessageBox
import userdash,sys

class Ui_Reg(object):
    def setupUi(self, Reg):
        Reg.setObjectName("Reg")
        Reg.resize(1200, 700)
        Reg.setStyleSheet("background: #FFFFFF;")
        Reg.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhSensitiveData)
        Reg.setSizeGripEnabled(False)
        self.txt_name = QtWidgets.QTextEdit(Reg)
        self.txt_name.setGeometry(QtCore.QRect(160, 150, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.txt_name.setFont(font)
        self.txt_name.setStyleSheet("border: 2px solid #000000;\n"
"border-radius: 20px;")
        self.txt_name.setObjectName("txt_name")
        self.btn_reg = QtWidgets.QPushButton(Reg)
        self.btn_reg.clicked.connect(self.database)
        self.btn_reg.setGeometry(QtCore.QRect(160, 560, 341, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_reg.setFont(font)
        self.btn_reg.setStyleSheet("position: absolute;\n"
"width: 274px;\n"
"height: 41px;\n"
"\n"
"background: #D8F8E8;\n"
"border-radius: 20px;\n"
"\n"
"")
        self.btn_reg.setObjectName("btn_reg")
        self.txt_mno = QtWidgets.QTextEdit(Reg)
        self.txt_mno.setGeometry(QtCore.QRect(160, 310, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.txt_mno.setFont(font)
        self.txt_mno.setStyleSheet("border: 2px solid #000000;\n"
"border-radius: 20px;")
        self.txt_mno.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhMultiLine|QtCore.Qt.ImhPreferNumbers)
        self.txt_mno.setObjectName("txt_mno")
        self.txt_unme = QtWidgets.QTextEdit(Reg)
        self.txt_unme.setGeometry(QtCore.QRect(160, 230, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.txt_unme.setFont(font)
        self.txt_unme.setStyleSheet("border: 2px solid #000000;\n"
"border-radius: 20px;")
        self.txt_unme.setObjectName("txt_unme")
        self.txt_eid = QtWidgets.QTextEdit(Reg)
        self.txt_eid.setGeometry(QtCore.QRect(160, 390, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.txt_eid.setFont(font)
        self.txt_eid.setStyleSheet("border: 2px solid #000000;\n"
"border-radius: 20px;")
        self.txt_eid.setObjectName("txt_eid")
        self.lbl_reg = QtWidgets.QLabel(Reg)
        self.lbl_reg.setGeometry(QtCore.QRect(250, 30, 231, 81))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_reg.setFont(font)
        self.lbl_reg.setObjectName("lbl_reg")
        self.img_reg = QtWidgets.QLabel(Reg)
        self.img_reg.setGeometry(QtCore.QRect(630, 70, 631, 561))
        self.img_reg.setStyleSheet("image: url(:/all/img/registration.jpg);")
        self.img_reg.setObjectName("img_reg")
        self.lineEdit = QtWidgets.QLineEdit(Reg)
        self.lineEdit.setGeometry(QtCore.QRect(10, 470, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border: 2px solid #000000;\n"
"border-radius: 20px;")
        self.lineEdit.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhPreferNumbers|QtCore.Qt.ImhSensitiveData)
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setMaxLength(8)
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setCursorPosition(0)
        self.lineEdit.setDragEnabled(True)
        self.lineEdit.setReadOnly(False)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Reg)
        self.lineEdit_2.setGeometry(QtCore.QRect(320, 470, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("border: 2px solid #000000;\n"
"border-radius: 20px;")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.retranslateUi(Reg)
        QtCore.QMetaObject.connectSlotsByName(Reg)

    def retranslateUi(self, Reg):
        _translate = QtCore.QCoreApplication.translate
        Reg.setWindowTitle(_translate("Reg", "Dialog"))
        self.txt_name.setHtml(_translate("Reg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt; font-weight:400;\"><br /></p></body></html>"))
        self.txt_name.setPlaceholderText(_translate("Reg", "              Full Name"))
        self.btn_reg.setText(_translate("Reg", "Sign Up"))
        self.txt_mno.setHtml(_translate("Reg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt; font-weight:400;\"><br /></p></body></html>"))
        self.txt_mno.setPlaceholderText(_translate("Reg", "              Mobile No."))
        self.txt_unme.setHtml(_translate("Reg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt; font-weight:400;\"><br /></p></body></html>"))
        self.txt_unme.setPlaceholderText(_translate("Reg", "              Username"))
        self.txt_eid.setHtml(_translate("Reg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt; font-weight:400;\"><br /></p></body></html>"))
        self.txt_eid.setPlaceholderText(_translate("Reg", "               Email Id"))
        self.lbl_reg.setText(_translate("Reg", "Register"))
        self.img_reg.setText(_translate("Reg", "<html><head/><body><p><br/></p></body></html>"))
        self.lineEdit.setPlaceholderText(_translate("Reg", "          Password"))
        self.lineEdit_2.setPlaceholderText(_translate("Reg", "   Confirm password"))

    def database(self):
        try:
            fnme = self.txt_name.text()
            usrnme = self.txt_unme.text()
            mobileno = self.txt_mno.text()
            email = self.txt_eid.text()
            pswd = self.lineEdit.text()



            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="placement"


            )

            mycursor = mydb.cursor()
            query = "SELECT fname,usrname,eid,mno,pwd from register where fname like'"+fnme + "'+ and usrname like'"+usrnme + "'+ and eid like'"+email + "'+ and mno like'"+mobileno + "'+ and pwd like'"+pswd + "'+"
            mycursor.execute(query)
            result = mycursor.fetchone()

            if result == None:
                self.lbl_reg.setText("Incorrect email or password")

            else:
                self.lbl_reg.setText("You are logged in")
                mydialog =QMessageBox()
                mydialog.setModal(True)
                mydialog.exec_()


        except mc.Error as e:
            self.lbl_reg.setText("Error")





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Reg = QtWidgets.QDialog()
    ui = Ui_Reg()
    ui.setupUi(Reg)
    Reg.show()
    sys.exit(app.exec_())
