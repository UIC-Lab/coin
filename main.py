import BreakingNews_Crawler as Crawl
import getCoinPrice as getCoin
import Input_News as IN
import sys
import os
from PyQt5.QtWidgets import *

class MyTest(QMainWindow):




    def __init__(self):
        super().__init__()
        btn1 = QPushButton("투자를 해야할까요?", self)
        btn1.move(30, 50)

        btn1.clicked.connect(self.button1_clicked)
        self.statusbar = self.statusBar()
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Coin Predictor')
        self.show()

    def button1_clicked(self):
        CoinResult = getCoin.getCoinResult(self)
        Crawl.main(sys.argv)
        NewsResult = IN.input_news()

        if CoinResult == 'UP':
            Coinrate = 0.4
        else:
            Coinrate = 0.0

        if NewsResult == 'UP':
            Newsrate = 0.6
        else:
            Newsrate = 0.0

        Finalrate = Coinrate + Newsrate
        if Finalrate == 1.0:
            QMessageBox.about(self, "Coin Predicting","매우상승")

        elif Finalrate == 0.6 :
            QMessageBox.about(self, "Coin Predicting","조금상승")

        elif Finalrate == 0.4 :
            QMessageBox.about(self, "Coin Predicting","조금하락")

        else :
            QMessageBox.about(self, "Coin Predicting","매우하락")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyTest()
    sys.exit(app.exec_())
