#!/usr/bin/python
import urllib2
import sys
import webbrowser

#Function to grab file and do stuff
def grab(url):
    robots = urllib2.urlopen(url + "/robots.txt")
    data = robots.read()
    data = data.split('\n')
    entries = len(data)
    resp = raw_input("Found " + str(entries) + " potential pages. About to open them in the browser. Cool? Y/N ")
    webbrowser.get('firefox').open('http://www.google.com')
    if resp == 'Y' or 'y':
        for line in data:
            if line.find('Disallow') != -1:
                list = line.split(' ')
                for url2 in list:
                    if url2.find('Disallow') == -1:
                        webbrowser.get('firefox').open_new_tab(url + url2)
    else:
        sys.exit()

#Function to parse argument
def parse(argument):
    if len(str(argument)) > 7 and argument[0:4] == "http":
        return True
    else:
        print "What are you doing? I need a real url..."
        print "Usage: robocop.py http://www.google.com"

if parse(sys.argv[1]):
    grab(sys.argv[1])
