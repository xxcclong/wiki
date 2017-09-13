#!/usr/bin/python
import json
import re,time
import urllib2
import urllib
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from bs4 import BeautifulSoup






file_object = open('info.txt')
try:
     infojs = file_object.read()
finally:
     file_object.close()


file_object2 = open('duiying.txt')
try:
    duiyingjs = file_object2.read()
finally:
    file_object2.close()



info = json.loads(infojs)
duiying = json.loads(duiyingjs)


print info
print duiying

print info[1]


print "dsas"

print duiying['Computer']