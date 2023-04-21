
import os
import json
import jieba

topFolder = 'C:/0000temp/git/weibo-trending-hot-search/raw'
f_word = open('C:/0000temp/git/weibo-trending-hot-search/jieba/word.txt',"w", encoding='utf-8')

for root,dirs,files in os.walk(topFolder):
    for fileName in files:
        filePath = os.path.join(root,fileName)
        # print(filePath)
        f_r = open(filePath, encoding='utf-8')
        raw_list = json.load(f_r)
        for dic in raw_list:
            titlleContent = dic['title']
            # print(titlleContent)
            seg_list = jieba.cut(titlleContent, cut_all=False)  # 精确模式
            for word in seg_list:
                f_word.write(word + '\n')
        f_r.close()
            

f_word.close()

