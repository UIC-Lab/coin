import BreakingNews_Crawler as Crawl
import getCoinPrice as getCoin
import Input_News as IN
import sys
import os
CoinResult = getCoin.getCoinResult(self)
Crawl.main(sys.argv)
NewsResult = IN.input_news()

if CoinResult == 'UP' :
    Coinrate = 0.4
else:
    Coinrate = 0.0

if NEwsResult == 'UP':
    Newsrate = 0.6
else:
    Newsrate = 0.0

Finalrate = Coinrate + Newsrate
if Finalrate == 1.0:
    print("FULL PURCHASE")
elif Finalrate == 0.6 :
    print("HALF PURCHASE")
elif Finalrate == 0.4 :
    print("HALF SELLING")
else:
    print("FULL SELLING")
