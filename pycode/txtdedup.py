
import os

tfolder = 'C:/0000temp/git/weibo-trending-hot-search/archivestxt'
dedupfolder = 'C:/0000temp/git/weibo-trending-hot-search/archivestxtdedup'

for root,dirs,files in os.walk(tfolder):
    for filename in files:
        txtfile = os.path.join(root,filename)
        #targetfilname = fileName.strip('.json') + '.txt'
        f_r = open(txtfile,'r' ,encoding='utf-8')
        f_w = open(os.path.join(dedupfolder,filename), 'w', encoding='utf-8')
        
        for line in f_r.readlines():
            if (line.split(' ')).[2] is in 
        index = 1
        for dic in raw_list:
            titllecontent = dic['title']
            titleurl = ('https://s.weibo.com/'+dic['url'])
            f_w.write(str(index) +' '+ titllecontent +' '+ titleurl+'\n')
            index += 1
        
        f_r.close()
        f_w.close()
            

#f_word.close()

