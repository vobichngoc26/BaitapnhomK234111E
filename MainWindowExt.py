from MainWindow import Ui_MainWindow


class MainWindowExt(Ui_MainWindow):
    price_matle=300000
    price_matnuoc=500000
    num_matle = 0
    num_matnuoc = 0
    money_matle = 0
    money_matnuoc = 0
    total = 0
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()

    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButtonMua.clicked.connect(self.process_mua)

    def process_mua(self):
        n_hoa = int(self.lineEditSoluong.text())
        if self.radioButtonDalat.isChecked():
            money_dalat = n_hoa * 100000
            self.num_dalat = self.num_dalat + n_hoa
            self.money_dalat = self.money_dalat + money_dalat
        elif self.radioButtonSapa.isChecked():
            money_sapa = n_hoa * 100000
            self.num_sapa = self.num_dalat + n_hoa
            self.money_sapa = self.money_sapa + money_sapa
        self.lineEditMatle.setText(str(self.num_dalat))
        self.lineEditMatnuoc.setText(str(self.num_sapa))
        self.lineEditThanhtien.setText(str(self.money_dalat))
        self.lineEditTienHoaSapa.setText(str(self.money_sapa))