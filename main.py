



import urllib2
import urlparse
from bs4 import BeautifulSoup
import string
import re
import time
from threading import Thread
from operator import itemgetter




file = open("List.txt")

file_content = file.read()

table =  file_content.splitlines()

names = table[0:table.index('')]
curse_word = table[len(table)-1]

record = []


for name in names:
    first_letter = name[0]
    url = "http://www.azlyrics.com/"+str(first_letter)+"/"+str(name)+".html"

    htmltext = urllib2.urlopen(url).read()
    counter = 0
    soup = BeautifulSoup(htmltext, "lxml")

    check = 0
    for tag in soup.select('a[href^="../lyrics/'+str(name)+'/"]'):

        #print str(tag) + " " + str(counter)
        if check == 3:
            break

        htmllink = "http://www.azlyrics.com/"+str(tag)[12:str(tag).find("target")-2]
        print htmllink
        htmlfile = urllib2.urlopen(htmllink)
        htmltext = htmlfile.read()
        counter += htmltext.count(str(curse_word))
        print (counter)
        time.sleep(5)
        check+=1
        print check
    record.append({'name': name, 'number': counter})



newlist = sorted(record, key=itemgetter('number'), reverse=True)

for dictionary in newlist:
    print dictionary['name']+" -- number of times profanity used -- "+str(dictionary['number'])





