# Form implementation generated from reading ui file 'C:\Users\admin\PycharmProjects\BaitapnhomK234111E\MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(614, 606)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\admin\\PycharmProjects\\BaitapnhomK234111E\\../ListMathProject/images/student.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(255, 210, 244);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 10, 461, 81))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 136, 219);\n"
"color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 100, 171, 171))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("C:\\Users\\admin\\PycharmProjects\\BaitapnhomK234111E\\../../OneDrive/Pictures/Ảnh chụp màn hình/Ảnh chụp màn hình 2024-11-14 014553.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(340, 100, 171, 171))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("C:\\Users\\admin\\PycharmProjects\\BaitapnhomK234111E\\../../OneDrive/Pictures/Ảnh chụp màn hình/Ảnh chụp màn hình 2024-11-14 014611.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(100, 310, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(360, 310, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.pushButtonMua = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonMua.setGeometry(QtCore.QRect(250, 340, 113, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonMua.setFont(font)
        self.pushButtonMua.setStyleSheet("background-color: rgb(255, 255, 255);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:\\Users\\admin\\PycharmProjects\\BaitapnhomK234111E\\../../Downloads/326700_cart_shopping_icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonMua.setIcon(icon1)
        self.pushButtonMua.setObjectName("pushButtonMua")
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(50, 510, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 85, 83);")
        self.label_8.setObjectName("label_8")
        self.lineEditThanhtienmatle = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditThanhtienmatle.setGeometry(QtCore.QRect(240, 510, 211, 21))
        self.lineEditThanhtienmatle.setStyleSheet("background-color: rgb(240, 255, 173);\n"
"color: rgb(0, 0, 0);")
        self.lineEditThanhtienmatle.setObjectName("lineEditThanhtienmatle")
        self.label_9 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(460, 510, 60, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(250, 400, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(255, 64, 245);")
        self.label_10.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(160, 450, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(140, 480, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.lineEditMatnuoc = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditMatnuoc.setGeometry(QtCore.QRect(240, 480, 211, 21))
        self.lineEditMatnuoc.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lineEditMatnuoc.setObjectName("lineEditMatnuoc")
        self.lineEditMatle = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditMatle.setGeometry(QtCore.QRect(240, 450, 211, 21))
        self.lineEditMatle.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.lineEditMatle.setObjectName("lineEditMatle")
        self.label_13 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(460, 450, 60, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(460, 480, 60, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.lineEdit_8 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(20, 410, 211, 10))
        self.lineEdit_8.setMaximumSize(QtCore.QSize(16777215, 10))
        self.lineEdit_8.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(380, 410, 211, 10))
        self.lineEdit_9.setMaximumSize(QtCore.QSize(16777215, 10))
        self.lineEdit_9.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEditThanhtienmatnuoc = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditThanhtienmatnuoc.setGeometry(QtCore.QRect(240, 540, 211, 21))
        self.lineEditThanhtienmatnuoc.setStyleSheet("background-color: rgb(240, 255, 173);\n"
"color: rgb(0, 0, 0);")
        self.lineEditThanhtienmatnuoc.setObjectName("lineEditThanhtienmatnuoc")
        self.label_15 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(460, 540, 60, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(20, 540, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: rgb(255, 85, 83);")
        self.label_16.setObjectName("label_16")
        self.radioButtonMatle = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButtonMatle.setGeometry(QtCore.QRect(120, 280, 91, 17))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.radioButtonMatle.setFont(font)
        self.radioButtonMatle.setObjectName("radioButtonMatle")
        self.radioButtonMatnuoc = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButtonMatnuoc.setGeometry(QtCore.QRect(380, 276, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.radioButtonMatnuoc.setFont(font)
        self.radioButtonMatnuoc.setObjectName("radioButtonMatnuoc")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 614, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BaitapnhomK234111E"))
        self.label.setText(_translate("MainWindow", "Cửa hàng Baby Three"))
        self.label_6.setText(_translate("MainWindow", "Giá: 300.000 VND"))
        self.label_7.setText(_translate("MainWindow", "Giá: 500.000 VND"))
        self.pushButtonMua.setText(_translate("MainWindow", "Mua "))
        self.label_8.setText(_translate("MainWindow", "Thành tiền mắt lé: "))
        self.label_9.setText(_translate("MainWindow", "VND"))
        self.label_10.setText(_translate("MainWindow", "Số lượng"))
        self.label_11.setText(_translate("MainWindow", "Mắt lé:"))
        self.label_12.setText(_translate("MainWindow", "Mắt nước:"))
        self.label_13.setText(_translate("MainWindow", "Con"))
        self.label_14.setText(_translate("MainWindow", "Con"))
        self.label_15.setText(_translate("MainWindow", "VND"))
        self.label_16.setText(_translate("MainWindow", "Thành tiền mắt nước: "))
        self.radioButtonMatle.setText(_translate("MainWindow", "Mắt lé"))
        self.radioButtonMatnuoc.setText(_translate("MainWindow", "Mắt nước"))
