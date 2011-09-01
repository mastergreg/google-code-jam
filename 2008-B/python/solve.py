#!/usr/bin/python
#/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
#
#* File Name : solve.py
#
#* Purpose :
#
#* Creation Date : 01-09-2011
#
#* Last Modified : Thu 01 Sep 2011 11:25:31 PM EEST
#
#* Created By : Greg Liras <gregliras@gmail.com>
#
#_._._._._._._._._._._._._._._._._._._._._.*/

import sys

f = sys.stdin


cases = int(f.readline())



for i in range(cases):
  size = int(f.readline())
  v1 = map(int,f.readline().split())
  v2 = map(int,f.readline().split())
  v1.sort()
  v2.sort()
  v2.reverse()
  answer=0
  for j in range(size):
    answer=answer+v1[j]*v2[j]
  print "Case #"+str(i+1)+": "+str(answer)
