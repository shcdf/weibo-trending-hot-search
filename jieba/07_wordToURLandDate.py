

import os
import json


tWord = "疫苗"
topFolder = 'C:/0000temp/git/weibo-trending-hot-search/raw'


def wordToUrl(tWord, tFile):
    f_r = open(tFile,'r', encoding='utf-8')
    tdic = dict()
    
    raw_list = json.load(f_r)
    for dic in raw_list:
        titlleContent = dic['title']
        if tWord in titlleContent:
            print(tFile[-15:-6])
            print(dic['title'], dic['url'])
    return None


for root,dirs,files in os.walk(topFolder):
    for fileName in files:
        filePath = os.path.join(root,fileName)
        # print(fileName.strip('.json'))
        wordToUrl(tWord,filePath)

