#!/usr/bin/env python
# -*- coding: utf-8
#
#* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
# File Name : solve.py
# Creation Date : 25-04-2012
# Last Modified : Wed 25 Apr 2012 02:20:24 PM EEST
# Created By : Greg Liras <gregliras@gmail.com>
#_._._._._._._._._._._._._._._._._._._._._.*/

mapping = {}

def dec(enc):
    message = []
    for i in enc:
        message.append(mapping[i])
    return "".join(message)

def get_map(char1,char2):
    return dict(zip(char1,char2))

def main():
    global mapping
    file1 = open("input1","r")
    file2 = open("output1","r")

    file1.readline()
    char1 = file1.read()
    char2 = file2.read()
    mapping = get_map(char1,char2)
    
    #print mapping
    lines = int(raw_input())
    for line in range(lines):
        enc = raw_input().rstrip()
        print "Case #{0} {1}".format(line,dec(enc))


if __name__=="__main__":
    main()

