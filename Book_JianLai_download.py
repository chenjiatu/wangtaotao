#从番外第一章开始，以它的网址作为初始网址
#在当前章节下获取每一章的下一章的网址后缀
#下载每一章的章名及其正文
#2020 2/19

import requests
import re
from bs4 import BeautifulSoup
import time
import datetime

starttime = datetime.datetime.now() #获取程序开始的时间
#从当前章获得当前章的名字以及下一章的后缀
def get_next_chapter():
    first_url = 'http://www.jianlaixiaoshuo.com/book/16.html'  #从感言开始
    res = requests.get(first_url)
    # res.encoding = res.apparent_encoding
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    #当前章节信息
    chapter_info=soup.find(id='BookCon')
    now_chaptername = chapter_info.h1.text    #当前章节名字
    now_content = soup.find(id='BookText').text
    #写入文件
    filename='1.txt'
    with open(filename,'a',encoding='utf-8') as f:
        f.write(now_chaptername)    #写入名字
        f.write(now_content)    #写入当前章正文
    #在当前章节获得下一章的网址后缀
    link = soup.find_all('a',rel=re.compile('^(next)'))
    houzui = link[0].attrs['href']
    a = re.findall('[0-9]',houzui)
    a = [str(i) for i in a]
    last_chapter_number = int(''.join(a))   #下一


    for i in range(705):    #设置一个循环，好让从第二章开始一直取下去
        url = 'http://www.jianlaixiaoshuo.com/book/{}.html'
        # # if i == 1:
        # #     last_chapter_number = 1
        # # else:
        now_url = url.format(last_chapter_number)   #又开始下一章的
        # if i == 1:
        #     now_url = first_url
        #     res = requests.get(first_url)   #第一次时是first_url的网址
        # else:
        #     res = requests.get(now_url)     #从第二次开始就不是了
        res = requests.get(now_url)
        # res.encoding = res.apparent_encoding
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text, 'html.parser')
        #当前章节信息
        chapter_info=soup.find(id='BookCon')
        now_chaptername = chapter_info.h1.text    #当前章节名字
        now_content = soup.find(id='BookText').text
        #写入文件
        # filename='content.txt'
        with open(filename,'a',encoding='utf-8') as f:
            f.write(now_chaptername)    #写入名字
            f.write(now_content)    #写入当前章正文
        #在当前章节获得下一章的网址后缀
        link = soup.find_all('a',rel=re.compile('^(next)'))
        houzui = link[0].attrs['href']
        a = re.findall('[0-9]',houzui)
        a = [str(i) for i in a]
        last_chapter_number = int(''.join(a))   #下一章节的网址数字后缀
        # now_url = url.format(last_chapter_number)
        time.sleep(0.2)


if __name__ == '__main__':
    get_next_chapter()
    endtime = datetime.datetime.now()#获取程序结束的时间
    print(endtime - starttime)
