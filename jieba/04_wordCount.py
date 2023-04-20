# import jieba

# import os
# import json



# f_r = open('C:/0000temp/git/weibo-trending-hot-search/raw/2020-11-24.json', encoding='utf-8')
# f_w = open('C:/0000temp/git/weibo-trending-hot-search/jieba/2020-11-24.txt',"w", encoding='utf-8')
# f_word = open('C:/0000temp/git/weibo-trending-hot-search/jieba/word.txt',"w", encoding='utf-8')

import os
import json
import jieba

dic = dict()
targetWord = "通报"
targetNo = 0

with open('C:/0000temp/git/weibo-trending-hot-search/jieba/word.txt',"r", encoding='utf-8') as f_word:
    for line in f_word.readlines():
        word = line.strip('\n')
        if targetWord == word:
            targetNo += 1 

f_word.close()


print(targetWord,': ',targetNo)
   



