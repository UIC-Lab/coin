# -*- coding: utf8 -*-

from konlpy.tag import Twitter
from gensim.models.word2vec import Word2Vec
import re
import os

t = Twitter()

Train_PATH = './train_txt/'
SAVE_PATH = './train_wv/'


def preprocessing(content):  # 전처리
    content = re.sub('\\xa0', '', content)
    content = re.sub('\\n', '', content)
    content = re.sub('\\\\xa0', '', content)
    content = re.sub('\\\\n', '', content)
    content = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@#$%&\\\=\(\'\")]', '', content)
    content = ' '.join(content.split())

    return content


def tokenize(doc):  # 토크나이징
    return ['/'.join(t) for t in t.pos(doc, norm=True, stem=True)]


wv_model_coin = Word2Vec.load(SAVE_PATH + 'train_wv')


def input_news():
    content = preprocessing(open('result.txt', 'rt', encoding='utf-8').read())

    input = [d for d in t.nouns(content)]

    up_sum = 0
    down_sum = 0
    for i in input:
        try:
            a = tokenize(i)
            up = tokenize('UP')
            down = tokenize('DOWN')
            up_result = wv_model_coin.wv.similarity(a[0], up[0])
            down_result = wv_model_coin.wv.similarity(a[0], down[0])
            up_sum = up_sum + up_result
            down_sum = down_sum + down_result
        except:
            continue

    if (up_sum > down_sum):
        result = 'UP'
    else:
        result = 'DOWN'

    return result
