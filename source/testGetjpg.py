#coding = utf-8
'''
Created on 2016年8月3日

@author: Administrator
'''
import urllib.request
import re   

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    x = 0
    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl, '%s.jpg' % x)
        x +=1

html = getHtml("http://tieba.baidu.com/p/4680783910")
print getImg(html)