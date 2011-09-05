#!/usr/bin/python
#/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
#
#* File Name : solve.py
#
#* Purpose :
#
#* Creation Date : 01-09-2011
#
#* Last Modified : Fri 02 Sep 2011 03:50:49 PM EEST
#
#* Created By : Greg Liras <gregliras@gmail.com>
#
#_._._._._._._._._._._._._._._._._._._._._.*/

import sys
import string

f = sys.stdin


cases = int(f.readline())


def getSubStrings(initstr):
  l = len(initstr)
  r=[]
  for i in range(l):
    for j in range(l-i):
      c=initstr[i:i+j+1]
      if c != '':
        r.append(c)
  s=set(r)
  return s


def byLength(w1,w2):
  return len(w1)-len(w2)


for i in range(cases):
  songs = int(f.readline())
  slist=[]
  for j in range(songs):
    slist.append((string.upper(f.readline()[:-1])))
  print "Case #"+str(i+1)+":"
  if songs==1:
    print "\"\""
  else:
    for i in range(songs):
      blist=list(slist)
      blist.pop(i)
      s=slist[i]
      ans=getSubStrings(s)
      for b in blist:
        bsstrings=getSubStrings(b)
        ans=ans - bsstrings
      ansr=sorted(list(ans),cmp=byLength)
      if len(ansr) > 0:
        minlength=len(ansr[0])
        answr=[]
        for a in ansr:
          if len(a)==minlength:
            answr.append(a)
        answer = sorted(answr)
        print "\""+answer[0]+"\""
      else:
        print ":("
