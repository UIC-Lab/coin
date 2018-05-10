import coinmarketcap

# Name of Coins
coin_name = ['digibyte', 'loopring', 'digixdao', 'mixin']
market = coinmarketcap.Market()

# init Coin's price of up&down of price
increaseCoin = 0
decreaseCoin = 0

for i in range(4):
    coin_info= 0
    coin = market.ticker(coin_name[i], limit=3, convert="KRW")
    coin_dict = coin[0]
    coin_price = float(coin_dict['price_krw'])
    with open('./coin_currency/'+coin_name[i]+'_price.txt', 'w+') as coin_info :
        # if not exist the coin's price
        preCoinPrice = coin_info.readable()
        if preCoinPrice is None:
            coin_info.write(coin_price + '\n')
            coin_info.close()
            continue;

        # Already exist the coin's price
        else:
            preCoinPrice = float(preCoinPrice)
            # if old one is expensive than present one
            if preCoinPrice > coin_price:
                decreaseCoin+=1

            # if old one is not expensive than present one
            elif preCoinPrice < coin_price:
                increaseCoin+=1

            # As a result
            coin_info.write(str(coin_price)+'\n')
            coin_info.close()

if increaseCoin > decreaseCoin:
    print("UP")
elif increaseCoin < decreaseCoin:
    print("DOWN")
elif increaseCoin == decreaseCoin:
    print("EVEN")
