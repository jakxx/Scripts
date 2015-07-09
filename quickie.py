import sys
import urllib2

file = sys.argv[1]
target = sys.argv[2]

f = open(file, "r")
lines = f.readlines()
for line in lines:
    line2 = line.strip()
    if line2[-1:] == '/':
        url = line2 + target
        urlclean = url.replace ('\n', '')
        try:
            response = urllib2.urlopen(urlclean)
            html = response.read()
            if html.find("doctype") == -1:  #edit this for more specific results
                if response.code == 200:    #edit this for mere specific results
                    print "Found at: " + urlclean
        except:
            pass
