from konlpy.tag import Twitter
from gensim.models.word2vec import Word2Vec
import re
import os
from datetime import datetime

t = Twitter()

Train_PATH = './train_txt/'
SAVE_PATH = './train_wv/'


def get_file(path):  # txt파일 불러오기
    filelist = []
    files = os.listdir(Train_PATH)  # txt파일에 있는 파일 리스트를 가져옴
    for file in files:
        ext = os.path.splitext(file)[-1]

        if ext == '.txt':
            filelist.append("%s%s" % (path, file))

    content = []
    for file in filelist:
        content.append(preprocessing(open_file(file)))  # content리스트 하나에 하나의 논문

    sentences = [tokenize(d) for d in content]  # 논문 하나가 한 리스트에 토큰화
    return sentences


def open_file(file):  # txt 파일 오픈
    txt_file = open(file, encoding='utf-8')
    content = txt_file.read()
    txt_file.close()
    return content


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


content = []
content = [preprocessing(open(Train_PATH + 'train.txt').read())]

sentences = [tokenize(d) for d in content]

wv_model_coin = Word2Vec(sentences, size=100, window = 8, min_count=10, workers=4, iter=100, sg=1)
#100차원 벡터, 주변단어 2개 참조, 출연빈도 20번이상, CPU 쿼드코어, 100번 반복, CBOW, Skip-Gram중 후자
wv_model_coin.save(SAVE_PATH + 'train_wv')

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

    print(up_sum, down_sum)
    if (up_sum > down_sum):
        result = 'UP'
    else:
        result = 'DOWN'

    return result