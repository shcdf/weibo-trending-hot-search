
import os
import json

topFolder = 'C:/0000temp/git/weibo-trending-hot-search/raw'
#f_word = open('C:/0000temp/git/weibo-trending-hot-search/jieba/word.txt',"w", encoding='utf-8')
targetfolder = 'C:/0000temp/git/weibo-trending-hot-search/jieba/archives_txt'

for root,dirs,files in os.walk(topFolder):
    for fileName in files:
        filePath = os.path.join(root,fileName)
        targetfilname = fileName.strip('.json') + '.txt'
        # print(filePath)
        f_r = open(filePath, encoding='utf-8')
        f_w = open(os.path.join(targetfolder,targetfilname), 'w', encoding='utf-8')
        raw_list = json.load(f_r)
        index = 1
        for dic in raw_list:
            titllecontent = dic['title']
            titleurl = ('https://s.weibo.com/'+dic['url'])
            f_w.write(str(index) +' '+ titllecontent +''+ titleurl+'\n')
            index += 1
            # print(titlleContent)
        f_r.close()
        f_w.close()
            

#f_word.close()

