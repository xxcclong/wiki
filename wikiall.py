# !/usr/bin/python
import json
import re, time
import urllib2
import urllib
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from bs4 import BeautifulSoup


def getHtml(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                             '(KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36'}
    req = urllib2.Request(url=url, headers=headers)
    page = urllib2.urlopen(req)

    html = page.read()
    return html


def human(url):
    html = getHtml(url)
    list = re.findall('<li><a\shref="(/wiki/List[^"]*)"', html)
    for page in list:
        page = "https://en.wikipedia.org" + page
        smallpage = getHtml(page)
        smalllist = re.findall('<li><a\shref="(/wiki/List[^"]*)"', smallpage)
        if smalllist != None:
            for o in smalllist:
                human(o)
            return




def getUrl(html):
    return


# html = getHtml("https://en.wikipedia.org/wiki/List_of_Nobel_laureates")
a = "https://en.wikipedia.org/wiki/Lists_of_people_by_occupation"
html1 = getHtml(a)
# print html1
list = re.findall('<li><a\shref="(/wiki/List[^"]*)"', html1)  # ^((?!XXX).)*$
info = []
id = 0
duiying = {}
p = re.compile(r'\W')
i = 0
for page in list:
    page = "https://en.wikipedia.org" + page
    print "page:" + page
    html = getHtml(page)
    smalllist = re.findall('<li><a\shref="(/wiki[^"]*)"', html)
    i = 0
    while i < len(smalllist):
        if re.search('List', smalllist[i], re.I) != None or re.search('Category', smalllist[i], re.I) != None:
            # print list[i]
            smalllist.pop(i)
            continue
        i += 1



    for smallpage in smalllist:

        smallpage = "https://en.wikipedia.org" + smallpage
        # print "small page:" + smallpage
        hh = getHtml(smallpage)
        soup = BeautifulSoup(hh, 'html.parser', from_encoding='utf-8')
        tag = soup.find('table', class_=re.compile("^infobox"))
        if tag == None:
            continue

        people = {}
        peoplename = ""
        labels = tag.find_all('tr', recursive=False)

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
                if peoplename != "":
                    print peoplename
                    continue
                else:
                    peoplename = tag1.get_text()
                    people["name"] = peoplename
                    continue
            people[tag1.get_text()] = tag2.get_text()

        info.append(people)


        # print people
        print id
        for k, v in people.items():
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
                # print duiying
        # print info
        id += 1
        if id%100 == 0:
            print "lalala"
            duiyingjs = json.dumps(duiying)
            infojs = json.dumps(info)

            file_object = open('infoall.txt', 'w')
            file_object.write(infojs)
            file_object.close()

            file_object2 = open('duiyingall.txt', 'w')
            file_object2.write(duiyingjs)
            file_object2.close()

            # people.clear()
        # print info

duiyingjs = json.dumps(duiying)
infojs = json.dumps(info)

file_object = open('infoall2.txt', 'w')
file_object.write(infojs)
file_object.close()

file_object2 = open('duiyingall2.txt', 'w')
file_object2.write(duiyingjs)
file_object2.close()




