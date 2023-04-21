

import json


# dic = dict()
tWord = "超越"


t = r'C:/0000temp/git/weibo-trending-hot-search/raw/2020-11-24.json'




def wordToUrl(tWord, tFile):
    f_r = open(tFile,'r', encoding='utf-8')
    tdic = dict()
    
    raw_list = json.load(f_r)
    for dic in raw_list:
        titlleContent = dic['title']
        if tWord in titlleContent:print(dic['title'], dic['url'])
    return None



wordToUrl("超越", t)