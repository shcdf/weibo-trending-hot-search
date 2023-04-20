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

with open('C:/0000temp/git/weibo-trending-hot-search/jieba/word.txt',"r", encoding='utf-8') as f_word:
    for word in f_word.readlines():
    # word = f_word.readline()
        if word in dic: 
            dic[word] += 1
        else:
            dic[word] = 1
f_word.close()


sorted(dic.values(),reverse=True)

print(sorted(dic.items(),key = lambda s:s[1],reverse=True))
   



