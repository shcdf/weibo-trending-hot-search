import jieba

import os
# import re
import json

# cwd = os.getcwd()  # Get the current working directory (cwd)
# files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in %r: %s" % (cwd, files))


# with open('C:/0000temp/git/weibo-trending-hot-search/raw/2020-11-24.json', encoding='utf-8') as f:
#     rawfile = f.read()

f_read = open('C:/0000temp/git/weibo-trending-hot-search/raw/2020-11-24.json', encoding='utf-8')
f_w = open('C:/0000temp/git/weibo-trending-hot-search/jieba/2020-11-24.txt',"w", encoding='utf-8')

raw_list = json.load(f_read)

for dic in raw_list:
    print(dic['title'])
    f_w.write(dic['title'] + '\n')

f_w.close()


# for line in lines:
#     # print(line)
#     regex = r'title(.*)'
#     title = re.search(regex,line)
#     if title: print(title.group(1))
    # matchObj = re.match( regex, line, re.M|re.I)
    # if matchObj:
    #     print ("matchObj.group(1) : ", matchObj.group(1))
    # else:
    #     print ("No match!!")


print('Done')

# import markdown

# with open('C:/0000temp/git/weibo-trending-hot-search/raw/2020-11-24.json', 'r',encoding='ASCII') as f:
#     text = f.read()
#     html = markdown.markdown(text)

# with open('C:/0000temp/git/weibo-trending-hot-search/jieba/2020-11-24.html', 'w') as f:
#     f.write(html)