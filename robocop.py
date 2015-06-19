#!/usr/bin/python
import urllib2
import sys

if len(str(sys.argv[1])) < 5 or sys.argv[1][0:4] != "http":
    print"What are you doing? I need a real url..."
    print "Usage: robocop.py http://www.google.com"
    sys.exit()

def grab(url):
    robots = urllib2.urlopen(url + "/robots.txt")
    print line

url = sys.argv[1]
grab(url)
