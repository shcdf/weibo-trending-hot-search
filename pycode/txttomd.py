import os

#kword = "郑州"
searchfolder = 'C:/0000temp/git/weibo-trending-hot-search/result'
resultpath = 'C:/0000temp/git/weibo-trending-hot-search/result-md'
#resultfile = ('C:/0000temp/git/weibo-trending-hot-search/result/' + kword + '.txt')
#if os.path.isfile(resultfile): input('The file is existing>>>')

def txttomd(txtfile, mdfile):
    f_r = open(txtfile,'r', encoding='utf-8')
    f_w = open(mdfile,'w', encoding='utf-8')
    for line in f_r.readlines():
        contentli = line.split(' ')
        f_w.write(contentli[0] +'  '+contentli[1] + '  ['+contentli[2]+']' + '('+contentli[3]+')' +'<br>')
        #print(contentli)
    f_r.close()
    f_w.close()
    return None


for root,dirs,files in os.walk(searchfolder):
    for file in files:
        filepath = os.path.join(root,file)
        resultfilename = file.strip('.txt') + '.md'
        resultfile = resultpath+'/'+resultfilename
        print(resultfile)
        txttomd(filepath, resultfile)


