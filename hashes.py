#!/usr/bin/python
import sys

if len(str(sys.argv[1])) < 3:
    print "usage: hash.py [hash]"
    sys.exit()

hash = str(sys.argv[1])
with open("hashes.txt") as fd:
    d = dict(line.strip().split(None, 1) for line in fd)

print "---Match Found---"
for x in d.keys():
    if len(d[x]) == len(hash) and d[x][:1] is hash[:1] and d[x][1:2] == hash[1:2] and d[x][2:3] == hash[2:3]:
        print str(x) + ":" + d[x]
print "---Other Possible Matches---"
for x in d.keys():
    if len(d[x]) == len(hash):
        print str(x) + ":" + d[x]

