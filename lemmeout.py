import urllib2;
for x in range (1,5):
        url = "http://letmeoutofyour.net:%d" % x;
        try:
                r = urllib2.urlopen(url, timeout=1);
                print "Port: %d" %x; print "Result: ",r.read();
        except urllib2.URLError, err:
                print "Port: %d" %x; print "Result: Refused";
