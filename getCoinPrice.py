import coinmarketcap
from pymarketcap import Pymarketcap
import os
# Name of Coins
market = Pymarketcap()

#Get the KRW Price of Coins
cur = market.ticker(convert="KRW")

# init Coin's price of up&down of price
increaseCoin = 0
decreaseCoin = 0


#Rank from 50 to 100
for i in range(50, 100):

    #Convert array to Dict to get which I want
    CurInfo = cur[i]

    #Get the price and name of the coin which is necessary
    Price = float(CurInfo['price_krw'])
    Name = CurInfo['name']

    #if file is exist. for avoid error whether file is exist or not
    if os.path.isfile('./coin_currency/'+Name+'_price.txt'):

            #get the old one from file
            PreInfo= open('./coin_currency/'+Name+'_price.txt', 'rt')
            PrePrice = PreInfo.readline()
            PrePrice = float(PrePrice)


            #compare the price
            if PrePrice > Price:
                decreaseCoin+=1

            elif PrePrice < Price:
                increaseCoin+=1

            #write down the new price to file
            PreInfo = open('./coin_currency/'+Name+'_price.txt', 'wt')
            PreInfo.write(str(Price)+'\n')
            PreInfo.close()
    else :
            #For the first execution which don't have coin's priceInfo
            PreInfo = open('./coin_currency/'+Name+'_price.txt', 'wt')
            PreInfo.write(str(Price)+'\n')
            PreInfo.close()

#Compare the number of the coin
if increaseCoin == 0 and decreaseCoin == 0 :
    print("EVEN")
else :
    if increaseCoin > decreaseCoin :
        print("UP")
    elif increaseCoin < decreaseCoin :
        print("DOWN")
