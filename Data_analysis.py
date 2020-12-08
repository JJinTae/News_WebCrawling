import pandas as pd
import numpy as np
import re
import os

from soynlp.tokenizer import RegexTokenizer
from soynlp.utils import DoublespaceLineCorpus
from soynlp.noun import LRNounExtractor_v2

from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud
from PIL import Image

import matplotlib.pyplot as plt
import numpy as np

# from nltk.corpus import stopwords

DATA_DIR = 'Data_CSV'
CSV_PETITION = os.path.join(DATA_DIR, 'petition_result_v2.csv')

# nouns detect stopwords
STOPWORDS_TXT = open('stopwords.txt', 'r', encoding='utf-8')
stopwords = STOPWORDS_TXT.readlines()
for i in range(len(stopwords)):
    stopwords[i] = stopwords[i].strip()

# wordcloud stopwords
STOPWORDS_WORDCLOUD_TXT = open('stopwords_wordcloud.txt', 'r', encoding='utf-8')
stopwords_wordcloud = STOPWORDS_WORDCLOUD_TXT.readlines()
for i in range(len(stopwords_wordcloud)):
    stopwords_wordcloud[i] = stopwords_wordcloud[i].strip()

# wordcloud
def _word_count(df, kon):
    konp = kon
    result = []
    for i in df.values:
        for s in konp.nouns(str(i)):
            if s not in stopwords_wordcloud:
                result.append(s)

    res_count = Counter(result)
    return res_count


def wordcloud(df, kon, n):
    okt_count = _word_count(df,kon)
    word_data = okt_count.most_common(n)
    wc = WordCloud(font_path='/NGULIM.TTF', background_color='white', width=800, height=600)
    cloud = wc.generate_from_frequencies(dict(word_data))
    plt.figure(figsize=(10, 8))
    plt.imshow(cloud)
    plt.axis('off')
    plt.show()
    return word_data

f = open(CSV_PETITION, "r", encoding='utf-8')
lines = f.read()
nlpy = Okt()

df = pd.read_csv(CSV_PETITION, parse_dates=['date'])

status = wordcloud(df, kon=nlpy, n=50)
print(status)

"""
# knolpy
f = open(CSV_PETITION, "r", encoding='utf-8')
lines = f.read()

nlpy = Okt()
nouns = nlpy.nouns(lines)

count = Counter(nouns)

tag_count = []
tags = []

for n, c in count.most_common(50):
    dics = {'tag': n, 'count':c}
    if len(dics['tag']) >=2 and len(tags) <= 19:
        if n not in stopwords:
            tag_count.append(dics)
            tags.append(dics['tag'])

for tag in tag_count:
    print(" {:<14}".format(tag['tag']), end='\t')
    print("{}".format(tag['count']))

"""

"""
def preprocessing(text):
    text = re.sub('\\\\n', ' ', text)
    return text

# soynlp
df = pd.read_csv(CSV_PETITION, parse_dates=['date'])
print(df.shape)
print(df.tail())

sample_title = df['title'].str.split(' ')
print(sample_title)


#print('토큰화 시작...')
#tokenizer = RegexTokenizer()

#sentences = df['title'].apply(preprocessing)
#tokens = sentences.apply(tokenizer.tokenize(sample_title))


print('명사화 시작...')
sents = DoublespaceLineCorpus(CSV_PETITION, iter_sent=True)

noun_extractor = LRNounExtractor_v2(verbose=True)
nouns = noun_extractor.train_extract(sents)

print(sorted(nouns.items(), key=lambda t : t[1], reverse=True))
"""