# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app_it.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import shutil
import os




class Ui_appit(object):
    def openWindow(self):
        self.window =  QtWidgets.QDialog()
        self.ui = Ui_appit()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, appit):
        appit.setObjectName("appit")
        appit.resize(1200, 700)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        appit.setFont(font)
        appit.setStyleSheet("background: #FFFFFF;")
        appit.setSizeGripEnabled(False)
        self.frame = QtWidgets.QFrame(appit)
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
        self.lbl_name = QtWidgets.QLabel(appit)
        self.lbl_name.setGeometry(QtCore.QRect(40, 160, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_name.setFont(font)
        self.lbl_name.setStyleSheet("background-color:#D8F8E8;")
        self.lbl_name.setObjectName("lbl_name")
        self.lbl_gen = QtWidgets.QLabel(appit)
        self.lbl_gen.setGeometry(QtCore.QRect(40, 250, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_gen.setFont(font)
        self.lbl_gen.setStyleSheet("background-color:#D8F8E8;")
        self.lbl_gen.setObjectName("lbl_gen")
        self.lbl_cmpny = QtWidgets.QLabel(appit)
        self.lbl_cmpny.setGeometry(QtCore.QRect(40, 340, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_cmpny.setFont(font)
        self.lbl_cmpny.setStyleSheet("background-color:#D8F8E8;")
        self.lbl_cmpny.setObjectName("lbl_cmpny")
        self.lbl_job = QtWidgets.QLabel(appit)
        self.lbl_job.setGeometry(QtCore.QRect(40, 430, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_job.setFont(font)
        self.lbl_job.setStyleSheet("background-color:#D8F8E8;")
        self.lbl_job.setObjectName("lbl_job")
        self.lbl_eid = QtWidgets.QLabel(appit)
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
        self.lbl_mno = QtWidgets.QLabel(appit)
        self.lbl_mno.setGeometry(QtCore.QRect(630, 250, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_mno.setFont(font)
        self.lbl_mno.setStyleSheet("background-color:#D8F8E8;")
        self.lbl_mno.setObjectName("lbl_mno")
        self.lbl_cgpa = QtWidgets.QLabel(appit)
        self.lbl_cgpa.setGeometry(QtCore.QRect(630, 340, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_cgpa.setFont(font)
        self.lbl_cgpa.setStyleSheet("background-color:#D8F8E8;")
        self.lbl_cgpa.setObjectName("lbl_cgpa")
        self.lbl_rsm = QtWidgets.QLabel(appit)
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
        self.checkBox_chng = QtWidgets.QCheckBox(appit)
        self.checkBox_chng.setGeometry(QtCore.QRect(370, 530, 421, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_chng.setFont(font)
        self.checkBox_chng.setStyleSheet("background-color:#D8F8E8;")
        self.checkBox_chng.setObjectName("checkBox_chng")
        self.comboBox__cmpny = QtWidgets.QComboBox(appit)
        self.comboBox__cmpny.setGeometry(QtCore.QRect(220, 340, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.comboBox__cmpny.setFont(font)
        self.comboBox__cmpny.setObjectName("comboBox__cmpny")
        self.comboBox__cmpny.addItem("")
        self.comboBox__cmpny.addItem("")
        self.comboBox__cmpny.addItem("")
        self.comboBox__cmpny.addItem("")
        self.comboBox_job = QtWidgets.QComboBox(appit)
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
        self.btn_rsm = QtWidgets.QPushButton(appit)
        self.btn_rsm.clicked.connect(self.openfile)
        self.btn_rsm.setGeometry(QtCore.QRect(840, 425, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_rsm.setFont(font)
        self.btn_rsm.setStyleSheet("background-color:rgb(255, 255, 255)\n"
"")
        self.btn_rsm.setObjectName("btn_rsm")
        self.comboBox_cgpa = QtWidgets.QComboBox(appit)
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

        self.retranslateUi(appit)
        QtCore.QMetaObject.connectSlotsByName(appit)

    def retranslateUi(self, appit):
        _translate = QtCore.QCoreApplication.translate
        appit.setWindowTitle(_translate("appit", "Dialog"))
        self.btn_bck.setText(_translate("appit", "Back"))
        self.lbl_app.setText(_translate("appit", "Application"))
        self.btn_sbmt.setText(_translate("appit", "Submit"))
        self.lbl_name.setText(_translate("appit", "Full Name : "))
        self.lbl_gen.setText(_translate("appit", "Gender : "))
        self.lbl_cmpny.setText(_translate("appit", "Company : "))
        self.lbl_job.setText(_translate("appit", "Job Role : "))
        self.lbl_eid.setText(_translate("appit", "Email ID : "))
        self.lbl_mno.setText(_translate("appit", "Mobile No. : "))
        self.lbl_cgpa.setText(_translate("appit", "Total CGPA : "))
        self.lbl_rsm.setText(_translate("appit", "Resume : "))
        self.checkBox_chng.setText(_translate("appit", " This details won\'t change."))
        self.comboBox__cmpny.setItemText(0, _translate("appit", "Select your Company"))
        self.comboBox__cmpny.setItemText(1, _translate("appit", "TCS"))
        self.comboBox__cmpny.setItemText(2, _translate("appit", "Infosys"))
        self.comboBox__cmpny.setItemText(3, _translate("appit", "Wipro"))
        self.comboBox_job.setItemText(0, _translate("appit", "Select your Job Role"))
        self.comboBox_job.setItemText(1, _translate("appit", "Junior Data Analyst"))
        self.comboBox_job.setItemText(2, _translate("appit", "Data Scientist"))
        self.comboBox_job.setItemText(3, _translate("appit", "Software Developer"))
        self.btn_rsm.setText(_translate("appit", "Upload"))
        self.comboBox_cgpa.setItemText(0, _translate("appit", "Select your CGPA"))
        self.comboBox_cgpa.setItemText(1, _translate("appit", "7.0 - 8.0"))
        self.comboBox_cgpa.setItemText(2, _translate("appit", "8.1 - 9.0"))
        self.comboBox_cgpa.setItemText(3, _translate("appit", "9.1 - 10.0"))

    def openfile(self):
        fname = QFileDialog.getOpenFileName(None, "Open File", "", " Document or Images (*.pdf)")
        #shutil.copyfile(fname, "./storage/abc.pdf")
        #shutil.move(fname, os.getcwd())
        #shutil.copy(fname, "os.p")  # dst can be a folder; use shutil.copy2() to preserve timestamp
        #print(fname)
        try:
            shutil.copy(fname[0], os.getcwd()+"/full project/storage")
            print("File copied successfully.")

        # If source and destination are same
        except shutil.SameFileError:
            print("Source and destination represents the same file.")

        # If there is any permission issue
        except PermissionError:
            print("Permission denied.")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    appit = QtWidgets.QDialog()
    ui = Ui_appit()
    ui.setupUi(appit)
    appit.show()
    sys.exit(app.exec_())









