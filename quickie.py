#!/usr/bin/python
import sys
import urllib2
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def usage():
   print " "
   print "Script to enumerate specific file from many urls"
   print "USAGE: python quickie.py urls.txt \"/.htaccess\""
   print " "
   sys.exit()

if len(sys.argv) < 3 or sys.argv[1] == '-h':
    usage()

file = sys.argv[1]
target = sys.argv[2]

f = open(file, "r")
lines = f.readlines()
for line in lines:
    line2 = line.strip()
    if line2[-1:] == '/' or target[:1] == '/':
        url = line2 + target
        urlclean = url.replace ('\n', '')
        try:
            response = requests.get(urlclean,verify=False,timeout=1)
            #html = response.read()
            #if html.find("doctype") == -1:  #edit this for more specific results
            if response.status_code == 200:    #edit this for mere specific results
                redir = requests.get(urlclean + "/test.txt",verify=False,timeout=1)
                if redir.status_code == 200:
                   print "Found at: " + urlclean + " (likely a universal redirect)"
                else:
                   print "Found at: " + urlclean
        except:
            pass
