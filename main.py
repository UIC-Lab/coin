import BreakingNews_Crawler as Crawl
import getCoinPrice as getCoin
import Input_News as IN
import sys
import os
CoinResult = getCoin.getCoinResult()
Crawl.main(sys.argv)
NewsResult = IN.input_news()



if CoinResult == 'UP':
    CoinRate = 0.4
else :
    CoinRate = 0.0

if NewsResult == 'UP':
    NewsRate = 0.6
else :
    NewsRate = 0.0

FinalRate = CoinRate + NewsRate

if FinalRate == 1.0:
    print("FULL PURCHASE")
elif FinalRate == 0.6 :
    print("HALF PURCHASE")
elif FinalRate == 0.4:
    print("HALF SELLING")
else :
    print("FULL SELLING")
print(CoinResult)
print(NewsResult)
print(FinalRate)

