#金鳞岂非池中物txt下载      2020 2.10

import requests
import re
from bs4 import BeautifulSoup
import datetime
import time

starttime = datetime.datetime.now() #获取程序开始的时间
def get_book():
    #初始网址，从第一章开始
    url = 'http://m.imayitxt.com/chapter/65848/22659512.html'
    #基本网址
    basic_url='http://m.imayitxt.com/chapter/65848/{}'
    #从第一章开始
    res = requests.get(url)
    res.encoding='utf-8'
    html = res.text
    #正文内容包含在标签<div class="textarticle">与</div>内
    chapter_reg = r'<div class="textarticle">(.*?)</div>'
    chapter_reg = re.compile(chapter_reg,re.S)
    #获取正文内容
    chapter_contents = re.findall(chapter_reg,html)[0]  #可以直接将正则表达式放在findall里，只不过可以使用compile（用来返回匹配对象）更有效率
    #把无关的内容用""代替
    chapter_contents=chapter_contents.replace("&nbsp;&nbsp;&nbsp;&nbsp;","")    #把"&nbsp;&nbsp;&nbsp;&nbsp;"全替换成""
    chapter_contents=chapter_contents.replace("&nbsp;&nbsp;&nbsp;&nbsp;<table&nbsp;align=right><tr><td></td></tr></table>&nbsp;&nbsp;","")
    chapter_contents=chapter_contents.replace("本章未完，继续下章阅读","")
    chapter_contents=chapter_contents.replace("免费小说，无弹窗小说网，txt下载，请记住蚂蚁阅读网www.mayitxt.com","")
    chapter_contents=chapter_contents.replace("要看完整版本请百度搜：()&nbsp;进去后再搜：金鳞岂是池中物","")
    chapter_contents=chapter_contents.replace("&nbsp;&nbsp;","")
    chapter_contents=chapter_contents.replace("《阿+雅+小+说+网&nbsp;手#机阅#读&nbsp;ayaxs.co","")
    chapter_contents=chapter_contents.replace("<table&nbsp;align=right><tr><td></td></tr></table>","")
    chapter_contents=chapter_contents.replace("<br/>>>","")
    chapter_contents=chapter_contents.replace("<br />","")
    #获取下一章节的网址后缀
    soup = BeautifulSoup(res.text, 'html.parser')
    chapter_name = soup.find(class_='read_tit').h4.text
    links=soup.find_all('a',class_=re.compile('^(zjBtn)'))
    next_chapter = links[3].attrs['href']
    #由于有的章节未完待续在下一个页面继续显示，但也是要点当前页面最右下角的下一章按钮
    #但是未完待续的章节网址不完整，只有后缀，真正的下一章的内容是完整的，所以需要进行判断
    if re.match(r'http',next_chapter):
        next_chapter = next_chapter
        #建立文档保存
        filename = '资料.txt'
        with open(filename,'a') as f:
            f.write(chapter_contents)
    else:
        next_chapter = basic_url.format(next_chapter)
        #建立文档保存
        filename = '资料.txt'
        with open(filename,'a') as f:
            f.write(chapter_name)       #如果是完整的目录，就写入章节名字
            f.write(chapter_contents)

    #先获取第一章后，再建立个循序获取从第二章到n-1的正文内容。。。。。。。（这是因为要获得next_chapter）
    for i in range(154):

        #获取网页正文并保存到文档
        res = requests.get(next_chapter)     #首先从第一章开始
        res.encoding='utf-8'
        html = res.text
        chapter_reg = r'<div class="textarticle">(.*?)</div>'
        chapter_reg = re.compile(chapter_reg,re.S)
        chapter_contents = re.findall(chapter_reg,html)[0]
        #把无关的内容用""代替
        chapter_contents=chapter_contents.replace("&nbsp;&nbsp;&nbsp;&nbsp;","")    #把"&nbsp;&nbsp;&nbsp;&nbsp;"全替换成""
        chapter_contents=chapter_contents.replace("&nbsp;&nbsp;&nbsp;&nbsp;<table&nbsp;align=right><tr><td></td></tr></table>&nbsp;&nbsp;","")
        chapter_contents=chapter_contents.replace("本章未完，继续下章阅读","")
        chapter_contents=chapter_contents.replace("免费小说，无弹窗小说网，txt下载，请记住蚂蚁阅读网www.mayitxt.com","")
        chapter_contents=chapter_contents.replace("&nbsp;&nbsp;","")
        chapter_contents=chapter_contents.replace("你现在所看的《金鳞岂是池中物》&nbsp;金鳞岂是池中物","")
        chapter_contents=chapter_contents.replace("<table&nbsp;align=right><tr><td></td></tr></table>","")
        chapter_contents=chapter_contents.replace("要看完整版本请百度搜：()&nbsp;进去后再搜：金鳞岂是池中物","")
        chapter_contents=chapter_contents.replace("《阿+雅+小+说+网&nbsp;手#机阅#读&nbsp;ayaxs.co","")
        chapter_contents=chapter_contents.replace("<br/>>>","")
        chapter_contents=chapter_contents.replace("<br />","")
        #获取下一章节的网址后缀
        soup = BeautifulSoup(res.text, 'html.parser')
        chapter_name = soup.find(class_='read_tit').h4.text
        links=soup.find_all('a',class_=re.compile('^(zjBtn)'))
        next_chapter = links[3].attrs['href']
        #由于有的章节未完待续在下一个页面显示，也是要点当前页面最右下角的下一章按钮
        #但是未完待续的章节网址不完整，真正的下一章的内容是完整的，所以需要进行判断
        if re.match(r'http',next_chapter):
            next_chapter = next_chapter
            #建立文档保存
            filename = '资料.txt'
            with open(filename,'a') as f:
                f.write(chapter_contents)
        else:
            next_chapter = basic_url.format(next_chapter)
            #建立文档保存
            filename = '资料.txt'
            with open(filename,'a') as f:
                f.write(chapter_name)
                f.write(chapter_contents)
        #友好爬虫
        time.sleep(0.2)

if __name__ == '__main__':
    get_book()
    #获取程序结束的时间
    endtime = datetime.datetime.now()
    print(endtime - starttime)