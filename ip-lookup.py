#!/usr/bin/python
#Script to take list of ip addresses and geolocate them
#Requires GeoLiteCity.dat file 


#useage: script.py ips.txt [--non-usa]
#use --non-usa to exclude US ips

import sys
import GeoIP

gi = GeoIP.open(
     "/IR/owa/GeoLiteCity.dat",
     GeoIP.GEOIP_INDEX_CACHE | GeoIP.GEOIP_CHECK_CACHE)

file = sys.argv[1]

if len(sys.argv) > 2:
    flag = sys.argv[2]
else:
    flag = "nope"

if flag == '--non-usa':
    nonusa = True
else:
    nonusa = False


file = open(file, "r")
for ip in file:
    ip = ip.strip()
    gidata = gi.record_by_name(ip)
    #if "192.168" in ip or "172.16" in ip:
        #gidata['country_name'] = Internal-IP
    if gidata and nonusa is True:
        if gidata['country_name'] != "United States":
            print ip + "," + str(gidata['city']) + "," + str(gidata['country_name'])
    elif gidata and nonusa is False:
            print ip + "," + str(gidata['city']) + "," + str(gidata['country_name'])
