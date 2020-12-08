import pandas as pd
import numpy as np
import re
import os

from soynlp.tokenizer import RegexTokenizer
from soynlp.utils import DoublespaceLineCorpus
from soynlp.noun import LRNounExtractor_v2

from konlpy.tag import Okt
from collections import Counter

DATA_DIR = 'Data_CSV'
CSV_PETITION = os.path.join(DATA_DIR, 'petition_result_v2_content_M10.csv')

STOPWORDS_TXT = open('stopwords.txt', 'r', encoding='utf-8')
stopwords = STOPWORDS_TXT.readlines()
for i in range(len(stopwords)):
    stopwords[i] = stopwords[i].strip()


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