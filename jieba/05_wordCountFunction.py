
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

