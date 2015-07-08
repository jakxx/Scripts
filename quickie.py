#!/usr/bin/python
import sys
import urllib2

file = sys.argv[1]
f = open(file, "r")
lines = f.readlines()
for line in lines:
    target = ".htaccess"
    line2 = line.strip()
    if line2[-1:] == '/':
        url = line2 + target
        urlclean = url.replace ('\n', '')
        try:
            response = urllib2.urlopen(urlclean)
            html = response.read()
            if html.find("doctype") == -1:
                if response.code == 200:
                    print "Found at: " + urlclean
        except:
            pass 