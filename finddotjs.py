#!/usr/bin/python3

#script to find .js file references in a webserver log and clean the resulting list

import re

f = open('access_log.txt', 'r')
jsfiles = re.findall(r'\w+\.js', f.read())

#dedup using set
jsfiles = list(set(jsfiles))

#sort
jsfiles.sort()

for jsfile in jsfiles:
    print(jsfile)
