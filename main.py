import BreakingNews_Crawler as Crawl
import getCoinPrice as getCoin
import Input_News as IN
import sys
import os
from PyQt5 import *

Crawl.main(sys.argv)
Coin_result = getCoin.getCoinResult()
News_Result = IN.input_news()

if Coin_result == 'UP':
    Coin_rate = 0.4
else:
    Coin_rate = 0.0


if News_Result == 'UP':
    News_rate = 0.6
else:
    News_rate = 0.0

Final_rate = Coin_rate + News_rate

if Final_rate == 1.0:
    print("Highly Recommanded for your investigation")
elif Final_rate == 0.6 :
    print("Recommand for your investigation")
elif Final_rate == 0.4 :
    print("Not so much recommand for your investigation")
else :
    print("Never do that!")
