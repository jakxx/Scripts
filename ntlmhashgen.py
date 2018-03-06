#!/usr/bin/python

import hashlib,binascii
import sys

input = sys.argv[1]

hash = hashlib.new('md4',input.encode('utf-16le')).digest()
print binascii.hexlify(hash)
