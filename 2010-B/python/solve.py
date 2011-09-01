#!/usr/bin/python
#/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
#
#* File Name : solve.py
#
#* Purpose :
#
#* Creation Date : 01-09-2011
#
#* Last Modified : Thu 01 Sep 2011 09:21:39 PM EEST
#
#* Created By : Greg Liras <gregliras@gmail.com>
#
#_._._._._._._._._._._._._._._._._._._._._.*/

f = open("B-small-practice.in","r")
cases = int(f.readline())
for i in range(cases):
  case = f.readline()
  casels=case.split()
  casels.reverse()
  ans = ":"
  for c in casels:
    ans = ans +" "+ c
  print "Case #"+str(i+1)+ans
