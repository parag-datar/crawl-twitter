# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 17:47:48 2015

@author:sarang dev 
"""
import json
# if you are using python 3, you should 
#import urllib.request
import urllib2

import codecs

content=[]
myFile = codecs.open("part-b-tweets\queries.txt",encoding='utf-8')
for line in myFile:
    content.append(line)

import detectlanguage

detectlanguage.configuration.api_key = "0b56398dc06929d4f027ab5c95d5a025"


for string in content:
    qid = string[0:3:1]
    string = string[4:-1:]
    result=detectlanguage.simple_detect(string)
    text_field = "text_en"
    if result == 'de':
    	text_field = "text_de"
    if result == 'ru':
	text_field = "text_ru"
    strings = string.split(" ")
    queryArr = u""
    for word in strings:
        queryArr = queryArr+'+'+word
    queryArr = queryArr[1::]
    queryArr = queryArr.replace(":","\:")
    # change the url according to your own koding username and query
    inurl = u"http://parag7777.koding.io:8983/solr/tweetindex/select?q="+text_field+":"+urllib2.quote(queryArr.encode('UTF-8'),safe='')+u"&fl=id%2Cscore&wt=json&indent=true&rows=1000"
    #inurl = u"http://parag7777.koding.io:8983/solr/tweetindex/select?q="+urllib2.quote(queryArr.encode('UTF-8'),safe='')+u"&fl=id%2Cscore&wt=json&indent=true&rows=1000"
    #outfn = 'output.txt'
    outfn = 'output.txt'
# change query id and IRModel name accordingly

    IRModel='default'
    outf = open(outfn, 'a+')
    data = urllib2.urlopen(inurl)
    # if you're using python 3, you should use
    #data = urllib.request.urlopen(inurl)

    docs = json.load(data)['response']['docs']
    # the ranking should start from 1 and increase
    rank = 1
    for doc in docs:
        outf.write(qid + ' ' + 'Q0' + ' ' + str(doc['id']) + ' ' + str(rank) + ' ' + str(doc['score']) + ' ' + IRModel + '\n')
        rank += 1
    outf.close()
