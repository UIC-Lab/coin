import coinmarketcap
market = coinmarketcap.Market()
coin = market.ticker('bitcoin', limit=3, convert="KRW")
coin_dict = coin[0]
coin_price = coin_dict['price_krw']
file_opner = open('./coin_currency/bitcoin_price.txt', 'at')
file_opner.write(coin_price+'\n')
file_opner.close()