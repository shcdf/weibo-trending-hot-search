import os

kword = "郑州"
searchfolder = 'C:/0000temp/git/weibo-trending-hot-search/archivestxt'
resultfile = ('C:/0000temp/git/weibo-trending-hot-search/result/' + kword + '.txt')
if os.path.isfile(resultfile): input('The file is existing>>>')

def wordtourl(keyword, searchfile):
    f_r = open(searchfile,'r', encoding='utf-8')
    for line in f_r.readlines():
        #print(line)
        if keyword in line: f_w.write((filepath[-14:-4]+' '+line))
    f_r.close()
    return None


for root,dirs,files in os.walk(searchfolder):
    f_w = open(resultfile, 'w', encoding='utf-8')
    for filename in files:
        filepath = os.path.join(root,filename)
        wordtourl(kword,filepath)
    f_w.close()


f_count = open(resultfile,'r', encoding='utf-8') 
count = len(f_count.readlines())
print(str(count) + ' records are hit')