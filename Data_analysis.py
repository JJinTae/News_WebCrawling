import pandas as pd
import numpy as np
import re
import os

from soynlp.tokenizer import RegexTokenizer
from soynlp.utils import DoublespaceLineCorpus
from soynlp.noun import LRNounExtractor_v2

DATA_DIR = 'Data_CSV'
CSV_PETITION = os.path.join(DATA_DIR, 'petition_result_v2.csv')

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


