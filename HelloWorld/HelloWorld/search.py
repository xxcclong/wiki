# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response
import re,json
def search_form(request):
	return render_to_response('search_form.html')

def sovle(ques):
	global poses
	global info
	global num
	global duiying
	
	p = re.compile(r'\s')
	ask = p.split(ques)
	array = []
	for i in range(20000):
		array = array + [0]
	for Q in ask:
		bonus = 10
		if duiying.has_key(Q) == False:
			continue
		added = []
		for nk in duiying[Q]:
			if array[nk] == None:
				array[nk] = 0
			array[nk] += 1
			if nk in added:
				continue
			array[nk] += bonus
			added.append(nk)
			
	num = 0
	poses = []
	while num < 20:
		min = 0
		minpos = 0
		for i in range(len(array)):
			if array[i]>min:
				min = array[i]
				minpos = i
		if min == 0:
			break
		poses.append(minpos)
		array[minpos] = 0
		num += 1

def search(request):
	global poses
	global info
	request.encoding = 'utf-8'
	if 'q' in request.GET:
		kind = 'all'
		p = re.compile(r'\s')
		newq = request.GET['q']
		if kind != 'all':
			ask - p.split(request.GET['q'])
			for ite in ask:
				newq += kind+':'+ite+' '

		ye = 0
		if 'PAGE' in request.GET:
			ye = int(request.GET['PAGE']) - 1
		
		ask = p.split(newq)
		searchname = ""
		for ww in range(len(ask)):
			searchname += ask[ww]
			if ww != len(ask)-1:
				searchname+= '+'

		sovle(newq)
		pp = []
		newposes = []
		for uu in poses:
			if pp.count(info[uu])==0:
				newposes.append(uu)
				pp.append(info[uu])
		people = []
		i = 3*ye
		p = re.compile(r'\s')
		ask = p.split(newq)
		while i<len(newposes) and i<3*(ye+1):
			person = {}
			person['shortcontent'] = ""
			for k in pp[i]:
				if k == 'name':
					person['name'] = pp[i][k]
					continue
				if k == 'image':
					continue
				stri = pp[i][k]
				flag = 0
				for Q in ask:
					if re.search(Q, pp[i][k], re.I)!= None:
				 	 	stri = re.sub(Q,"<font color=\"red\">"+Q+"</font>",pp[i][k])
				 	 	flag = 1
				 	 	# person['shortcontent'] = person['shortcontent'] + k + " : " + stri +"</br>"
				if flag:
					person['shortcontent'] = person['shortcontent'] + k + " : " + stri +"</br>"
					


			if person.has_key('name')==True:
				person['id'] = 'http://127.0.0.1:8000/search?k=' + str(newposes[i])
				people.append(person)	
			
			i += 1
		meses = []
		stri = 'http://127.0.0.1:8000/search?q='+ searchname + '&PAGE='
		L = 0
		u = len(newposes)
		if u%3:
			u = (int)(u/3)*3 +3
		while 3*L<u:
			mes = {}
			mes['web'] = stri + str(L)
			mes['num'] = 'page '+str(L)
			meses.append(mes)
			L += 1
		
		if request.GET['q']=='':
			searchname = "Welcome!"
		
		return render_to_response('aaa.html', {'searchname':searchname,'people':people,'meses':meses})

	elif 'k' in request.GET:
		num = int(request.GET['k'])
		Name = ''
		image = ''
		infoma = []
		for k in info[num]:
			if k == 'name':
				Name = info[num][k]
				continue
			if k == 'image':
				image = info[num][k]
				continue
			temp = {}
			temp['k'] = k
			temp['v'] = info[num][k]
			infoma.append(temp)
		if infoma == []:
			return 1
		return render_to_response('bbb.html', {'searchname':Name,'info':infoma,'image':image})


info = []
duiying = []
poses = []
num = 0
searchname = ""

file_object = open('infoall_2.txt')
try:
     infojs = file_object.read()
finally:
     file_object.close()


file_object2 = open('duiyingall_2.txt')
try:
    duiyingjs = file_object2.read()
finally:
    file_object2.close()



info = json.loads(infojs)
duiying = json.loads(duiyingjs)
