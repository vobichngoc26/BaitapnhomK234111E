from MainWindow import Ui_MainWindow


class MainWindowExt(Ui_MainWindow):
    num_matle = 0
    num_matnuoc = 0
    money_matle = 0
    money_matnuoc = 0

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()

    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButtonMua.clicked.connect(self.process_mua)

    def process_mua(self):
        price_matle = 300000
        price_matnuoc = 500000
        try:
            num_matle = int(self.lineEditMatle.text())
        except ValueError:
            num_matle = 0

        try:
            num_matnuoc = int(self.lineEditMatnuoc.text())
        except ValueError:
            num_matnuoc = 0

        if self.radioButtonMatle.isChecked():
            money_matle = num_matle* price_matle
            self.num_matle = self.num_matle + num_matle
            self.money_matle = self.money_matle + money_matle
        elif self.radioButtonMatnuoc.isChecked():
            money_matnuoc = num_matnuoc* price_matnuoc
            self.num_matnuoc = self.num_matnuoc + num_matnuoc
            self.money_matnuoc = self.money_matnuoc + money_matnuoc

        self.lineEditMatle.setText(str(self.num_matle))
        self.lineEditMatnuoc.setText(str(self.num_matnuoc))
        self.lineEditThanhtienmatle.setText(str(self.money_matle))
        self.lineEditThanhtienmatnuoc.setText(str(self.money_matnuoc))