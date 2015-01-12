#!/usr/bin/python
import sys

if len(str(sys.argv[1])) < 3:
    print "usage: hash.py [hash]"
    sys.exit()

hash = str(sys.argv[1])
with open("hashes.txt") as fd:
    d = dict(line.strip().split(None, 1) for line in fd)

exact = ""
print "---Exact Match---"
for x in d.keys():
    if d[x][:1] is hash[:1] and d[x][1:2] == hash[1:2] and d[x][2:3] == hash[2:3]:
        print str(x) + ":" + d[x]
        exact = str(x)
    if str(d[x]).isalnum() and hash.isalnum() and len(d[x]) == len(hash):
        print str(x) + ":" + d[x]
        exact = str(x)
if (exact):
    sys.exit()
print "\n---Possible Matches---"
for x in d.keys():
    if len(d[x]) == len(hash) and str(x) != exact:
        print str(x) + ":" + d[x]

