#!/usr/bin/python
#/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
#
#* File Name : solve.py
#
#* Purpose :
#
#* Creation Date : 01-09-2011
#
#* Last Modified : Fri 02 Sep 2011 12:34:55 AM EEST
#
#* Created By : Greg Liras <gregliras@gmail.com>
#
#_._._._._._._._._._._._._._._._._._._._._.*/

import sys
import string
from mpmath import *



def my3(p):
  ans1=1
  for i in range(p):
    ans1*=mpf(3+sqrt(5))
    fract = modf(ans1,1)
    ans1-=fract
    ans1=ans1(modf,1000)
    ans1+=fract
  ans1= floor(ans1)
  print ans1
  ans1=str(ans1)
  ans=""
  l = len(ans1)
  if l < 3:
    for i in range(3-l):
      ans+="0"
    ans+=ans1
  else:
    ans=ans1[len(ans1)-3:]
  return ans
    

f = sys.stdin


cases = int(f.readline())




for i in range(cases):
  p = int(f.readline())
  answer=my3(p)
  #for j in range(size):
  #  answer=answer+v1[j]*v2[j]
  print "Case #"+str(i+1)+": "+answer
