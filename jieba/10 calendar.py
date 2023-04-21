

import os
import json

# tWord = input('Enter a word:')
tWord = '疫苗'

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
            # print(tFile[-15:-5],i,dic['title'])
            titleli.append([tFile[-15:-5],i,dic['title']])
            # print(dic['title'], dic['url'])
    return titleli


sourceli = []
for root,dirs,files in os.walk(topFolder):
    for fileName in files:
        filePath = os.path.join(root,fileName)
        # print(fileName.strip('.json'))
        # for item in wordToUrl(tWord,filePath): print(item)
        sourceli = sourceli + (wordToUrl(tWord,filePath))

#for item in sourceli:print(item)

# import matplotlib.pyplot as plt
# fig = plt.figure()
# ax = fig.subplots()


# print(len(sourceli))

i = 0 
x = []
y = []
while i < 100:
# while i < len(sourceli):
    x.append(sourceli[i][0])
    y.append(sourceli[i][1])
    i += 1

# print(x)
# print(y)

for i in range(len(x)):
    print(x[i],y[i])


# ax.scatter(x,y)
# ax.invert_yaxis()
# plt.show()



import random
import datetime

import pyecharts.options as opts
from pyecharts.charts import Calendar


# begin = datetime.date(2021, 1, 1)
# end = datetime.date(2021, 2, 19)
data = [x,y]


(
    Calendar()
    .add(
        series_name="444",
        yaxis_data = y,
        calendar_opts=opts.CalendarOpts(
            pos_top="120",
            pos_left="30",
            pos_right="30",
            range_="2021",
            yearlabel_opts=opts.CalendarYearLabelOpts(is_show=True),
        ),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(pos_top="30", pos_left="center", title="2021"),
        visualmap_opts=opts.VisualMapOpts(
            max_=200, min_=1, orient="horizontal", is_piecewise=False
        ),
    )
    .render("calendar.html")
)