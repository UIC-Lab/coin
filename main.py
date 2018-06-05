import BreakingNews_Crawler as Crawl
import getCoinPrice as getCoin
import Input_News as IN
import Ratio as Rt
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
        CoinResult = Rt.getRatio()
        Crawl.main(sys.argv)
        NewsResult = IN.input_news()


        if NewsResult == 'UP':
            if CoinResult >= 2.0:
                QMessageBox.about(self, "Coin Predicting", "4%이상 상승")
            elif CoinResult < 2.0 and CoinResult >=0.0:
                QMessageBox.about(self, "Coin PRedicting", "2~4%이상 상승")
            elif CoinResult < 0.0 and CoinResult >= -5.0:
                QMessageBox.about(self, "Coin Predicting", "-2~2% 현상태 유지")
            else:
                QMessageBox.about(self, "Coin Predicting", "-2%이상 하락")
        else:
            if CoinResult >=0.0 and CoinResult < 5.0:
                QMessageBox.about(self, "Coin Predicting", "-2~2% 현 상태 유지")
            elif CoinResult >= 5.0 :
                QMessageBox.about(self, "Coin Predicting", "2%이상 상승")
            elif CoinResult >= -2.0 and CoinResult < 0.0:
                QMessageBox.about(self, "Coin Predicting", "2~4%이상 하락")
            else:
                QMessageBox.about(self, "Coin Predicting", "4% 이상 하락")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyTest()
    sys.exit(app.exec_())
