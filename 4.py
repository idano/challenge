#!/usr/bin/env python

import urllib
import re

#12345
# and the next nothing is 99257

urlbase = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
param = ["12345"]
url = urlbase + param[0]

for i in range(400):
    #print url
    fo = urllib.urlopen(url)
    result = fo.read()
    print result
    #words = result.split(' ')
    #for word in words:
        #if word.isdigit():
            #param = word
    matches = re.findall(r'[0-9]+', result)
    #print len(matches)
    if matches:
        url = urlbase + matches[0]
    else:
        print "EEEEEEXIT"
        exit(1)

    print i

