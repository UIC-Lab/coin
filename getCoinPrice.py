import coinmarketcap
import os
# Name of Coins
coin_name = ['digibyte', 'loopring', 'digixdao', 'mixin']
market = coinmarketcap.Market()

# init Coin's price of up&down of price
increaseCoin = 0
decreaseCoin = 0

for Name in coin_name:
    coin_info= 0
    coin = market.ticker(Name, limit=3, convert="KRW")
    coin_dict = coin[0]
    coin_price = float(coin_dict['price_krw'])

    if os.path.isfile('./coin_currency/'+Name+'_price.txt'):

            coin_info= open('./coin_currency/'+Name+'_price.txt', 'rt')
            preCoinPrice = coin_info.readline()
            preCoinPrice = float(preCoinPrice)

            if preCoinPrice > coin_price:
                decreaseCoin+=1

            elif preCoinPrice < coin_price:
                increaseCoin+=1

            coin_info = open('./coin_currency/'+Name+'_price.txt', 'wt')
            coin_info.write(str(coin_price)+'\n')
            coin_info.close()

    else :
            coin_info= open('./coin_currency/'+Name+'_price.txt', 'wt')
            coin_info.write(str(coin_price)+'\n')
            coin_info.close()

if increaseCoin == 0 and decreaseCoin == 0 :
    print("EVEN")
else :
    if increaseCoin > decreaseCoin :
        print("UP")
    elif increaseCoin < decreaseCoin :
        print("DOWN")
