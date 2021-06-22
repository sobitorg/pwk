#!/usr/bin/python3

#script to search log file for .js files


# opening a log file
file1 = open("access_log.txt", "r")

string1 = '.js'

# read file content
readfile = file1.read()

# checking condition for string found or not
if string1 in readfile: 
    print('String', string1, 'Found In File')
else: 
    print('String', string1 , 'Not Found')   
# closing a file

file1.close() 
