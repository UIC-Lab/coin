import coin_word2vec
import getCoinPrice
import breakingnews_crawler
import sys
import os

#get the CoinPrice class

AltCoin_result = getCoinPrice.getCoinPrice()
Crawler_result = breakingnews_crawler.main(sys.argv)
Word2vec_result = coin_word2vec.input_news()


#get the coin_word2vec class
