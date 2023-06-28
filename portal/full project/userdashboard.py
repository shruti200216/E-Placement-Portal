from PyQt5 import QtCore, QtGui, QtWidgets
from app_it import Ui_appit
from app_extc import Ui_App_Extc
from app_civil import Ui_App_Civil
from app_mech import Ui_App_mech
import userdash, sys


class Ui_Userdashboard(object):
    def openWindow1(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_appit()
        self.ui.setupUi(self.window)
        self.window.show()

    def openWindow2(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_App_Extc()
        self.ui.setupUi(self.window)
        self.window.show()

    def openWindow3(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_App_Civil()
        self.ui.setupUi(self.window)
        self.window.show()

    def openWindow4(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_App_mech()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, Userdashboard):
        Userdashboard.setObjectName("Userdashboard")
        Userdashboard.resize(1200, 700)
        Userdashboard.setStyleSheet("background: #FFFFFF;")
        Userdashboard.setSizeGripEnabled(False)
        self.frame = QtWidgets.QFrame(Userdashboard)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1201, 80))
        self.frame.setStyleSheet("background: #D8F8E8;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lbl_jp = QtWidgets.QLabel(self.frame)
        self.lbl_jp.setGeometry(QtCore.QRect(380, 17, 491, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_jp.setFont(font)
        self.lbl_jp.setStyleSheet("color: #00000\n"
                                  "")
        self.lbl_jp.setObjectName("lbl_jp")
        self.frm_cmp = QtWidgets.QFrame(Userdashboard)
        self.frm_cmp.setGeometry(QtCore.QRect(346, 143, 216, 220))
        self.frm_cmp.setStyleSheet("background: #D8F8E8;\n"
                                   "border-radius: 20px;")
        self.frm_cmp.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_cmp.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_cmp.setObjectName("frm_cmp")
        self.img_cmp = QtWidgets.QLabel(self.frm_cmp)
        self.img_cmp.setGeometry(QtCore.QRect(44, 30, 121, 111))
        self.img_cmp.setStyleSheet("image: url(:/all/img/cmp.png);")
        self.img_cmp.setObjectName("img_cmp")
        self.btn_cmp = QtWidgets.QPushButton(self.frm_cmp, clicked=lambda: self.openWindow1())
        self.btn_cmp.setGeometry(QtCore.QRect(10, 160, 191, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_cmp.setFont(font)
        self.btn_cmp.setStyleSheet("color: #0000;\n"
                                   "\n"
                                   "")
        self.btn_cmp.setObjectName("btn_cmp")
        self.frm_civil = QtWidgets.QFrame(Userdashboard)
        self.frm_civil.setGeometry(QtCore.QRect(637, 143, 216, 220))
        self.frm_civil.setStyleSheet("background: #D8F8E8;\n"
                                     "border-radius: 20px;\n"
                                     "")
        self.frm_civil.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_civil.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_civil.setObjectName("frm_civil")
        self.img_civil = QtWidgets.QLabel(self.frm_civil)
        self.img_civil.setGeometry(QtCore.QRect(50, 30, 121, 111))
        self.img_civil.setStyleSheet("image: url(:/all/img/civil.png);")
        self.img_civil.setObjectName("img_civil")
        self.btn_civil = QtWidgets.QPushButton(self.frm_civil, clicked=lambda: self.openWindow3())
        self.btn_civil.setGeometry(QtCore.QRect(10, 160, 191, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_civil.setFont(font)
        self.btn_civil.setStyleSheet("color: #00000;\n"
                                     "")
        self.btn_civil.setObjectName("btn_civil")
        self.frm_extc = QtWidgets.QFrame(Userdashboard)
        self.frm_extc.setGeometry(QtCore.QRect(637, 425, 216, 220))
        self.frm_extc.setStyleSheet("background: #D8F8E8;\n"
                                    "border-radius: 20px;\n"
                                    "")
        self.frm_extc.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_extc.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_extc.setObjectName("frm_extc")
        self.img_extc = QtWidgets.QLabel(self.frm_extc)
        self.img_extc.setGeometry(QtCore.QRect(50, 30, 121, 111))
        self.img_extc.setStyleSheet("image: url(:/all/img/extc.png);")
        self.img_extc.setObjectName("img_extc")
        self.btn_extc = QtWidgets.QPushButton(self.frm_extc, clicked=lambda: self.openWindow2())
        self.btn_extc.setGeometry(QtCore.QRect(10, 160, 191, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_extc.setFont(font)
        self.btn_extc.setStyleSheet("color: #000000;\n"
                                    "")
        self.btn_extc.setObjectName("btn_extc")
        self.frm_mech = QtWidgets.QFrame(Userdashboard)
        self.frm_mech.setGeometry(QtCore.QRect(346, 425, 216, 220))
        self.frm_mech.setStyleSheet("background: #D8F8E8;\n"
                                    "border-radius: 20px;")
        self.frm_mech.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_mech.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_mech.setObjectName("frm_mech")
        self.img_mech = QtWidgets.QLabel(self.frm_mech)
        self.img_mech.setGeometry(QtCore.QRect(50, 30, 121, 111))
        self.img_mech.setStyleSheet("image: url(:/all/img/mech.png);")
        self.img_mech.setObjectName("img_mech")
        self.btn_mech = QtWidgets.QPushButton(self.frm_mech, clicked=lambda: self.openWindow4())
        self.btn_mech.setGeometry(QtCore.QRect(10, 160, 191, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_mech.setFont(font)
        self.btn_mech.setStyleSheet("color: #0000;\n"
                                    "")
        self.btn_mech.setObjectName("btn_mech")
        self.btn_logout = QtWidgets.QPushButton(Userdashboard)
        self.btn_logout.setGeometry(QtCore.QRect(50, 630, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_logout.setFont(font)
        self.btn_logout.setStyleSheet("background-color:#D8F8E8;")
        self.btn_logout.setObjectName("btn_logout")

        self.retranslateUi(Userdashboard)
        QtCore.QMetaObject.connectSlotsByName(Userdashboard)

    def retranslateUi(self, Userdashboard):
        _translate = QtCore.QCoreApplication.translate
        Userdashboard.setWindowTitle(_translate("Userdashboard", "Dialog"))
        self.lbl_jp.setText(_translate("Userdashboard", "Select Your Job Profile"))
        self.img_cmp.setText(_translate("Userdashboard", "<html><head/><body><p><br/></p></body></html>"))
        self.btn_cmp.setText(_translate("Userdashboard", "IT / CS Engineer"))
        self.img_civil.setText(_translate("Userdashboard", "<html><head/><body><p><br/></p></body></html>"))
        self.btn_civil.setText(_translate("Userdashboard", "Civil Engineer"))
        self.img_extc.setText(_translate("Userdashboard", "<html><head/><body><p><br/></p></body></html>"))
        self.btn_extc.setText(_translate("Userdashboard", "EXTC Engineer"))
        self.img_mech.setText(_translate("Userdashboard", "<html><head/><body><p><br/></p></body></html>"))
        self.btn_mech.setText(_translate("Userdashboard", "Mechanical Engineer"))
        self.btn_logout.setText(_translate("Userdashboard", "Logout"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Userdashboard = QtWidgets.QDialog()
    ui = Ui_Userdashboard()
    ui.setupUi(Userdashboard)
    Userdashboard.show()
    sys.exit(app.exec_())