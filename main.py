import BreakingNews_Crawler as Crawl
import getCoinPrice as getCoin
import Input_News as IN
import sys
import os
CoinResult = getCoin.getCoinResult()
Crawl.main(sys.argv)
NewsResult = IN.input_news()

if CoinResult == "UP":
    if NewsResult == "UP":
        result = "FULL PURCHASE"
    elif NewsResult == "DOWN":
        result = "HALF SELLING"

elif CoinResult == "DOWN" or CoinResult == "EVEN":
    if NewsResult == "UP":
        result = "HALF PURCHASING"
    elif NewsResult == "DOWN" :
        result = "FULL SELLING"


print(result)
