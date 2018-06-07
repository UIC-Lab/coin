from pymarketcap import Pymarketcap
import os

def getRatio():
    market = Pymarketcap()

    cur = market.ticker(convert="KRW")
    sum=0
    for i in range(50, 100):
        CurInfo = cur[i]

        Price = float(CurInfo['price_krw'])
        Name = CurInfo['name']

        if os.path.isfile('./coin_currency/'+Name+'_price.txt'):
            PreInfo = open('./coin_currency/'+Name+'_price.txt', 'rt')
            PrePrice = PreInfo.readline()
            PrePrice = float(PrePrice)

            cur_ratio = ((Price-PrePrice)/Price)*100
            sum+=cur_ratio

            PreInfo = open('./coin_currency/'+Name+'_price.txt', 'wt')
            PreInfo.write(str(Price)+'\n')
            PreInfo.close()
        else:
            PreInfo = open('./coin_currency/'+Name+'_price.txt', 'wt')
            PreInfo.write(str(Price)+'\n')
            PreInfo.close()

    result = sum /50
    return result
