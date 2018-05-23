import coin_word2vec
import getCoinPrice
import breakingnews_crawler
import sys
import os

#initialize the each module
breakingnews_crawler.main(sys.argv)
AltCoin_result = getCoinPrice.getCoinPrice()
Word2vec_result = coin_word2vec.input_news()


print("AltCoin's result is : ",AltCoin_result)
print("Article's result is : ", Word2vec_result)
