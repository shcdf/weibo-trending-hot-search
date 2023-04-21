

import os
import json

tWord = input('Enter a word:')

def wordCount(tWord):
    tNo = 0
    with open('C:/0000temp/git/weibo-trending-hot-search/jieba/word.txt',"r", encoding='utf-8') as f_word:
        for line in f_word.readlines():
            word = line.strip('\n')
            if tWord == word:
                tNo += 1 
    f_word.close()
    return (tNo)


print(tWord, wordCount(tWord))
input('press any key to continue>>>')


topFolder = 'C:/0000temp/git/weibo-trending-hot-search/raw'

def wordToUrl(tWord, tFile):
    f_r = open(tFile,'r', encoding='utf-8')
    titleli = []
    
    raw_list = json.load(f_r)
    i = 0
    for dic in raw_list:
        i += 1
        if i > 100:break
        titlleContent = dic['title']
        if tWord in titlleContent:
            print(tFile[-15:-5],i,dic['title'])
            # titleli.append([tFile[-15:-5],i,dic['title']])
            # print(dic['title'], dic['url'])
    return titleli


for root,dirs,files in os.walk(topFolder):
    for fileName in files:
        filePath = os.path.join(root,fileName)
        # print(fileName.strip('.json'))
        for item in wordToUrl(tWord,filePath): print(item)

