import jieba

import os
import json


f_r = open('C:/0000temp/git/weibo-trending-hot-search/raw/2020-11-24.json', encoding='utf-8')
f_w = open('C:/0000temp/git/weibo-trending-hot-search/jieba/2020-11-24.txt',"w", encoding='utf-8')

raw_list = json.load(f_r)

for dic in raw_list:
    print(dic['title'])
    f_w.write(dic['title'] + '\n')

f_w.close()