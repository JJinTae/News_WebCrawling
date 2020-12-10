from apyori import apriori
import numpy as np
import pandas as pd
import re
import networkx as nx
import matplotlib.pyplot as plt

dataset = [['사장', '회사', '시작', '국민', '파일', '저작권', '원장', '직원', '교사', '시간'],
           ['신천지', '회사', '국민', '삼성', '민원', '주주명부', '대표', '코로나', '목사', '직원'],
           ['번방', '성범죄', '사람', '여성', '국민', '대한민국', '병원', '남성', '영상', '성착취', '청소년'],
           ['아이', '여성', 'N번방', '성범죄', '어머니', '강간', '사회', '성폭행', '가족', '대통령'],
           ['여성', '국민', '인권', '남편', '아이', '사회', '회사', '할머니', '친구', '직원'],
           ['회사', '국민', '아이', '학교', '사회', '수술', '가족', '전화', '경리', '대한민국'],
           ['국민', '대한민국', '아이', '대통령', '인권', '박원순', '아들', '여성', '손정우', '미국'],
           ['회사', '국민', '아이', '직원', '학생', '누나', '가족', '대한민국', '아버지', '폭행'],
           ['아이', '여성', '직원', '장애인', '병사', '대표', '국민', '학교', '병원', '차별'],
           ['입원', '병원', '선생님', '응급', '이송', '국민', '아이', '여성', '치료', '보호']]



print('hello py')
result = list(apriori(dataset, min_support=0.1, min_confidence=0.0001, min_lift=1, max_length=2))
print('result : \n', result)
df = pd.DataFrame(result)
print('hello py')
print(df.head(10))
df['length'] = df['items'].apply(lambda x : len(x))
df = df[(df['length'] == 2) & (df['support'] >= 0.08)].sort_values(by='support', ascending=False)
print(df.head(10))

G = nx.Graph()
ar = (df['items'])
G.add_edges_from(ar)



pr = nx.pagerank(G)
nsize = np.array([v for v in pr.values()])
nsize = 30000 * (nsize - min(nsize)) / (max(nsize) - min(nsize))


pos = nx.spring_layout(G)


plt.figure(figsize=(20,30))
plt.axis('off')
nx.draw_networkx(G, font_family='Malgun Gothic', font_size=20, pos=pos, node_color=list(pr.values()),
                 node_size=nsize, alpha=0.5, edge_color='.5')


plt.show()