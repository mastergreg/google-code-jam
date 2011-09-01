#!/usr/bin/python
#/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
#
#* File Name : solve.py
#
#* Purpose :
#
#* Creation Date : 01-09-2011
#
#* Last Modified : Thu 01 Sep 2011 09:54:16 PM EEST
#
#* Created By : Greg Liras <gregliras@gmail.com>
#
#_._._._._._._._._._._._._._._._._._._._._.*/
import sys


f = sys.stdin


leters = {
  'a':'2',
  'b':'22',
  'c':'222',
  'd':'3',
  'e':'33',
  'f':'333',
  'g':'4',
  'h':'44',
  'i':'444',
  'j':'5',
  'k':'55',
  'l':'555',
  'm':'6',
  'n':'66',
  'o':'666',
  'p':'7',
  'q':'77',
  'r':'777',
  's':'7777',
  't':'8',
  'u':'88',
  'v':'888',
  'w':'9',
  'x':'99',
  'y':'999',
  'z':'9999',
  ' ':'0',
  '\n':''
}


cases = int(f.readline())

for i in range(cases):
  line = f.readline()
  ret=[]
  for c in line:
    ret.append(leters[c])
  startl=ret[0][0]
  answer=ret[0]
  #print answer,startl
  for r in ret[1:]:
    if len(r)>0:
      if r[0] == startl:
        answer = answer +' '+r
      else:
        answer = answer + r
      startl = r[0]
    else:
      answer = answer+''
  print "Case #"+str(i+1)+": "+answer

