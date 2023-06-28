# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app_civil.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_App_Civil(object):
    def setupUi(self, App_Civil):
        App_Civil.setObjectName("App_Civil")
        App_Civil.resize(1200, 700)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        App_Civil.setFont(font)
        App_Civil.setStyleSheet("background: #FFFFFF;")
        App_Civil.setSizeGripEnabled(False)
        self.frame = QtWidgets.QFrame(App_Civil)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1201, 791))
        self.frame.setStyleSheet("background:#D8F8E8;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btn_bck = QtWidgets.QPushButton(self.frame)
        self.btn_bck.setGeometry(QtCore.QRect(380, 610, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_bck.setFont(font)
        self.btn_bck.setStyleSheet("background-color:rgb(255, 255, 255)\n"
"")
        self.btn_bck.setObjectName("btn_bck")
        self.lbl_app = QtWidgets.QLabel(self.frame)
        self.lbl_app.setGeometry(QtCore.QRect(480, 20, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_app.setFont(font)
        self.lbl_app.setStyleSheet("color:rgb(0, 0, 0)\n"
"")
        self.lbl_app.setObjectName("lbl_app")
        self.btn_sbmt = QtWidgets.QPushButton(self.frame)
        self.btn_sbmt.setGeometry(QtCore.QRect(660, 610, 120, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_sbmt.setFont(font)
        self.btn_sbmt.setStyleSheet("background-color:rgb(255, 255, 255)\n"
"\n"
"")
        self.btn_sbmt.setObjectName("btn_sbmt")
        self.txt_nme = QtWidgets.QLineEdit(self.frame)
        self.txt_nme.setGeometry(QtCore.QRect(220, 160, 161, 31))
        self.txt_nme.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.txt_nme.setObjectName("txt_nme")
        self.txt_gen = QtWidgets.QLineEdit(self.frame)
        self.txt_gen.setGeometry(QtCore.QRect(220, 250, 161, 31))
        self.txt_gen.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.txt_gen.setObjectName("txt_gen")
        self.txt_eid = QtWidgets.QLineEdit(self.frame)
        self.txt_eid.setGeometry(QtCore.QRect(840, 160, 161, 31))
        self.txt_eid.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.txt_eid.setObjectName("txt_eid")
        self.txt_mno = QtWidgets.QLineEdit(self.frame)
        self.txt_mno.setGeometry(QtCore.QRect(840, 250, 161, 31))
        self.txt_mno.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.txt_mno.setObjectName("txt_mno")
        self.lbl_name = QtWidgets.QLabel(App_Civil)
        self.lbl_name.setGeometry(QtCore.QRect(40, 160, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_name.setFont(font)
        self.lbl_name.setStyleSheet("background-color:#D8F8E8;")
        self.lbl_name.setObjectName("lbl_name")
        self.lbl_gen = QtWidgets.QLabel(App_Civil)
        self.lbl_gen.setGeometry(QtCore.QRect(40, 250, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_gen.setFont(font)
        self.lbl_gen.setStyleSheet("background-color:#D8F8E8;")
        self.lbl_gen.setObjectName("lbl_gen")
        self.lbl_cmpny = QtWidgets.QLabel(App_Civil)
        self.lbl_cmpny.setGeometry(QtCore.QRect(40, 340, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_cmpny.setFont(font)
        self.lbl_cmpny.setStyleSheet("background-color:#D8F8E8;")
        self.lbl_cmpny.setObjectName("lbl_cmpny")
        self.lbl_job = QtWidgets.QLabel(App_Civil)
        self.lbl_job.setGeometry(QtCore.QRect(40, 430, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_job.setFont(font)
        self.lbl_job.setStyleSheet("background-color:#D8F8E8;")
        self.lbl_job.setObjectName("lbl_job")
        self.lbl_eid = QtWidgets.QLabel(App_Civil)
        self.lbl_eid.setGeometry(QtCore.QRect(630, 160, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_eid.setFont(font)
        self.lbl_eid.setStyleSheet("background-color:#D8F8E8;\n"
"")
        self.lbl_eid.setObjectName("lbl_eid")
        self.lbl_mno = QtWidgets.QLabel(App_Civil)
        self.lbl_mno.setGeometry(QtCore.QRect(630, 250, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_mno.setFont(font)
        self.lbl_mno.setStyleSheet("background-color:#D8F8E8;")
        self.lbl_mno.setObjectName("lbl_mno")
        self.lbl_cgpa = QtWidgets.QLabel(App_Civil)
        self.lbl_cgpa.setGeometry(QtCore.QRect(630, 340, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_cgpa.setFont(font)
        self.lbl_cgpa.setStyleSheet("background-color:#D8F8E8;")
        self.lbl_cgpa.setObjectName("lbl_cgpa")
        self.lbl_rsm = QtWidgets.QLabel(App_Civil)
        self.lbl_rsm.setGeometry(QtCore.QRect(630, 430, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_rsm.setFont(font)
        self.lbl_rsm.setStyleSheet("background-color:#D8F8E8;\n"
"")
        self.lbl_rsm.setObjectName("lbl_rsm")
        self.checkBox_chng = QtWidgets.QCheckBox(App_Civil)
        self.checkBox_chng.setGeometry(QtCore.QRect(370, 530, 421, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_chng.setFont(font)
        self.checkBox_chng.setStyleSheet("background-color:#D8F8E8;")
        self.checkBox_chng.setObjectName("checkBox_chng")
        self.comboBox_cmpny = QtWidgets.QComboBox(App_Civil)
        self.comboBox_cmpny.setGeometry(QtCore.QRect(220, 340, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.comboBox_cmpny.setFont(font)
        self.comboBox_cmpny.setObjectName("comboBox_cmpny")
        self.comboBox_cmpny.addItem("")
        self.comboBox_cmpny.addItem("")
        self.comboBox_cmpny.addItem("")
        self.comboBox_cmpny.addItem("")
        self.comboBox_job = QtWidgets.QComboBox(App_Civil)
        self.comboBox_job.setGeometry(QtCore.QRect(220, 430, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.comboBox_job.setFont(font)
        self.comboBox_job.setObjectName("comboBox_job")
        self.comboBox_job.addItem("")
        self.comboBox_job.addItem("")
        self.comboBox_job.addItem("")
        self.comboBox_job.addItem("")
        self.btn_rsm = QtWidgets.QPushButton(App_Civil)
        self.btn_rsm.setGeometry(QtCore.QRect(840, 425, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_rsm.setFont(font)
        self.btn_rsm.setStyleSheet("background-color:rgb(255, 255, 255)\n"
"")
        self.btn_rsm.setObjectName("btn_rsm")
        self.comboBox_cgpa = QtWidgets.QComboBox(App_Civil)
        self.comboBox_cgpa.setGeometry(QtCore.QRect(840, 340, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.comboBox_cgpa.setFont(font)
        self.comboBox_cgpa.setObjectName("comboBox_cgpa")
        self.comboBox_cgpa.addItem("")
        self.comboBox_cgpa.addItem("")
        self.comboBox_cgpa.addItem("")
        self.comboBox_cgpa.addItem("")

        self.retranslateUi(App_Civil)
        QtCore.QMetaObject.connectSlotsByName(App_Civil)

    def retranslateUi(self, App_Civil):
        _translate = QtCore.QCoreApplication.translate
        App_Civil.setWindowTitle(_translate("App_Civil", "Dialog"))
        self.btn_bck.setText(_translate("App_Civil", "Back"))
        self.lbl_app.setText(_translate("App_Civil", "Application"))
        self.btn_sbmt.setText(_translate("App_Civil", "Submit"))
        self.lbl_name.setText(_translate("App_Civil", "Full Name : "))
        self.lbl_gen.setText(_translate("App_Civil", "Gender : "))
        self.lbl_cmpny.setText(_translate("App_Civil", "Company : "))
        self.lbl_job.setText(_translate("App_Civil", "Job Role : "))
        self.lbl_eid.setText(_translate("App_Civil", "Email ID : "))
        self.lbl_mno.setText(_translate("App_Civil", "Mobile No. : "))
        self.lbl_cgpa.setText(_translate("App_Civil", "Total CGPA : "))
        self.lbl_rsm.setText(_translate("App_Civil", "Resume : "))
        self.checkBox_chng.setText(_translate("App_Civil", " This details won\'t change."))
        self.comboBox_cmpny.setItemText(0, _translate("App_Civil", "Select your Company"))
        self.comboBox_cmpny.setItemText(1, _translate("App_Civil", "Tata Projects Ltd"))
        self.comboBox_cmpny.setItemText(2, _translate("App_Civil", "GMR Group"))
        self.comboBox_cmpny.setItemText(3, _translate("App_Civil", "Hindustan Construction Company"))
        self.comboBox_job.setItemText(0, _translate("App_Civil", "Select your Job Role"))
        self.comboBox_job.setItemText(1, _translate("App_Civil", "Civil engineer"))
        self.comboBox_job.setItemText(2, _translate("App_Civil", "Construction and management engineer"))
        self.comboBox_job.setItemText(3, _translate("App_Civil", "Commissioning engineer"))
        self.btn_rsm.setText(_translate("App_Civil", "Upload"))
        self.comboBox_cgpa.setItemText(0, _translate("App_Civil", "Select your CGPA"))
        self.comboBox_cgpa.setItemText(1, _translate("App_Civil", "7.0 - 8.0"))
        self.comboBox_cgpa.setItemText(2, _translate("App_Civil", "8.1 - 9.0"))
        self.comboBox_cgpa.setItemText(3, _translate("App_Civil", "9.1 - 10.0"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    App_Civil = QtWidgets.QDialog()
    ui = Ui_App_Civil()
    ui.setupUi(App_Civil)
    App_Civil.show()
    sys.exit(app.exec_())