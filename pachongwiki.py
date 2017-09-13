#!/usr/bin/python
import json
import re,time
import urllib2
import urllib
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from bs4 import BeautifulSoup

def getHtml (url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                             '(KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36'}
    req = urllib2.Request(url=url, headers=headers)
    page = urllib2.urlopen(req)

    html = page.read()
    return html



def getUrl(html):
    return

# html = getHtml("https://en.wikipedia.org/wiki/List_of_Nobel_laureates")
a = "https://en.wikipedia.org/wiki/List_of_computer_scientists"
html1 = getHtml(a)
# print html1
list =  re.findall('<li><a\shref="(/wiki/(?!L)(?!i)(?!s)(?!t)[^"]*)"',html1)#^((?!XXX).)*$
i = 0
while i<len(list):
    if re.search('Lists', list[i], re.I) != None or re.search('Category',list[i],re.I) != None:
        # print list[i]
        list.pop(i)
        continue
    i+=1

info = []
id = 0
duiying = {}
p = re.compile(r'\W')


for page in list:
    print id

    if (id > 2):
        print "hehhe"
        break
    page = "https://en.wikipedia.org" + page
    # time.sleep(3)
    html = getHtml(page)
    soup = BeautifulSoup(html,'html.parser',from_encoding='utf-8')
    tag = soup.find('table',class_="infobox biography vcard")
    if tag == None:
        continue
    people = {}
    peoplename = ""
    #image = tag.img['src']
    #if image != None:
     #    people["image"] = image
    labels = tag.find_all('tr',recursive=False)


    for label in labels:
        # print label
        tag1 = label.find('th')
        tag2 = label.find('td')

        if tag1 == None and tag2 != None:

            # people["image"] = tag2.get_text()
            # print tag2
            image = tag2.find("img")
            if image != None:
                people["image"] = unicode(image)
            continue
        if tag2 == None:
            peoplename = tag1.get_text()
            people["name"] = peoplename
            continue
        people[tag1.get_text()] = tag2.get_text()


    info.append(people)
    print info
    # print people
    for k,v in people.items():
        if k == "image" or k == u'Website':
            continue
        ss = p.split(v)
        for i in ss:
            if i == '':
                continue
            if duiying.has_key(i) == False:
                duiying[i] = []

            duiying[i].append(id)
            # if len(duiying[i])>1:
              #  print i


    # print duiying
    id += 1
    # people.clear()
    # print info

duiyingjs = json.dumps(duiying)
infojs = json.dumps(info)

file_object = open('info.txt', 'w')
file_object.write(infojs)
file_object.close()


file_object2 = open('duiying.txt', 'w')
file_object2.write(duiyingjs)
file_object2.close()




