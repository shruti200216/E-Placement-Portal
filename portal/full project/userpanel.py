from PyQt5 import QtCore, QtGui, QtWidgets
from add_remove import Ui_Edit
from userdashboard import Ui_Userdashboard
from Edit_profile import Ui_editp
from adminstatus import Ui_Status
import user_panel, sys

class Ui_User_Panel(object):
    def editp(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_editp()
        self.ui.setupUi(self.window)
        self.window.show()
    def toapply(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Userdashboard()
        self.ui.setupUi(self.window)
        self.window.show()
    def status(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Status()
        self.ui.setupUi(self.window)
        self.window.show()

    def addremove(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Edit()
        self.ui.setupUi(self.window)
        self.window.show()



    def setupUi(self, User_Panel):
        User_Panel.setObjectName("User_Panel")
        User_Panel.resize(1200, 700)
        User_Panel.setStyleSheet("background: #FFFFFF;")
        User_Panel.setSizeGripEnabled(False)
        self.frame = QtWidgets.QFrame(User_Panel)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1201, 80))
        self.frame.setStyleSheet("background: #D8F8E8;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lbl_jp = QtWidgets.QLabel(self.frame)
        self.lbl_jp.setGeometry(QtCore.QRect(480, 10, 331, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_jp.setFont(font)
        self.lbl_jp.setStyleSheet("color: #00000\n"
"")
        self.lbl_jp.setObjectName("lbl_jp")
        self.frm_cmp = QtWidgets.QFrame(User_Panel)
        self.frm_cmp.setGeometry(QtCore.QRect(346, 143, 216, 220))
        self.frm_cmp.setStyleSheet("background: #D8F8E8;\n"
"border-radius: 20px;")
        self.frm_cmp.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_cmp.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_cmp.setObjectName("frm_cmp")
        self.img_cmp = QtWidgets.QLabel(self.frm_cmp)
        self.img_cmp.setGeometry(QtCore.QRect(44, 30, 121, 111))
        self.img_cmp.setStyleSheet("image: url(:/All/img/apply.png);")
        self.img_cmp.setObjectName("img_cmp")
        self.btn_cmp = QtWidgets.QPushButton(self.frm_cmp,clicked=lambda: self.toapply())
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
        self.frm_civil = QtWidgets.QFrame(User_Panel)
        self.frm_civil.setGeometry(QtCore.QRect(637, 143, 216, 220))
        self.frm_civil.setStyleSheet("background: #D8F8E8;\n"
"border-radius: 20px;\n"
"")
        self.frm_civil.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_civil.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_civil.setObjectName("frm_civil")
        self.img_civil = QtWidgets.QLabel(self.frm_civil)
        self.img_civil.setGeometry(QtCore.QRect(40, 30, 121, 111))
        self.img_civil.setStyleSheet("image: url(:/All/img/view_status_User.png);")
        self.img_civil.setObjectName("img_civil")
        self.btn_civil = QtWidgets.QPushButton(self.frm_civil,clicked=lambda: self.status())
        self.btn_civil.setGeometry(QtCore.QRect(10, 160, 191, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_civil.setFont(font)
        self.btn_civil.setStyleSheet("color: #00000;\n"
"")
        self.btn_civil.setObjectName("btn_civil")
        self.frm_mech = QtWidgets.QFrame(User_Panel)
        self.frm_mech.setGeometry(QtCore.QRect(492, 420, 216, 220))
        self.frm_mech.setStyleSheet("background: #D8F8E8;\n"
"border-radius: 20px;")
        self.frm_mech.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_mech.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_mech.setObjectName("frm_mech")
        self.img_mech = QtWidgets.QLabel(self.frm_mech)
        self.img_mech.setGeometry(QtCore.QRect(40, 30, 121, 111))
        self.img_mech.setStyleSheet("image: url(:/All/img/edit_profile.png);")
        self.img_mech.setObjectName("img_mech")
        self.btn_mech = QtWidgets.QPushButton(self.frm_mech,clicked=lambda: self.editp())
        self.btn_mech.setGeometry(QtCore.QRect(10, 160, 191, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_mech.setFont(font)
        self.btn_mech.setStyleSheet("color: #0000;\n"
"")
        self.btn_mech.setObjectName("btn_mech")
        self.btn_logout = QtWidgets.QPushButton(User_Panel,)
        self.btn_logout = QtWidgets.QPushButton(User_Panel,)
        self.btn_logout.setGeometry(QtCore.QRect(50, 630, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_logout.setFont(font)
        self.btn_logout.setStyleSheet("background-color:#D8F8E8;")
        self.btn_logout.setObjectName("btn_logout")

        self.retranslateUi(User_Panel)
        QtCore.QMetaObject.connectSlotsByName(User_Panel)

    def retranslateUi(self, User_Panel):
        _translate = QtCore.QCoreApplication.translate
        User_Panel.setWindowTitle(_translate("User_Panel", "Dialog"))
        self.lbl_jp.setText(_translate("User_Panel", "User Panel"))
        self.img_cmp.setText(_translate("User_Panel", "<html><head/><body><p><br/></p></body></html>"))
        self.btn_cmp.setText(_translate("User_Panel", "Apply"))
        self.img_civil.setText(_translate("User_Panel", "<html><head/><body><p><br/></p></body></html>"))
        self.btn_civil.setText(_translate("User_Panel", "View Status"))
        self.img_mech.setText(_translate("User_Panel", "<html><head/><body><p><br/></p></body></html>"))
        self.btn_mech.setText(_translate("User_Panel", "Edit Profile"))
        self.btn_logout.setText(_translate("User_Panel", "Logout"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    User_Panel = QtWidgets.QDialog()
    ui = Ui_User_Panel()
    ui.setupUi(User_Panel)
    User_Panel.show()
    sys.exit(app.exec_())