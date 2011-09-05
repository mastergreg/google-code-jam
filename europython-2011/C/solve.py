#!/usr/bin/python
#/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
#
#* File Name : solve.py
#
#* Purpose :
#
#* Creation Date : 01-09-2011
#
#* Last Modified : Sun 04 Sep 2011 07:07:53 PM EEST
#
#* Created By : Greg Liras <gregliras@gmail.com>
#
#_._._._._._._._._._._._._._._._._._._._._.*/

import sys
import re
import string

f = sys.stdin


cases = int(f.readline())



for i in range(cases):
  spell = f.readline()[:-1]
  m = re.search('.*?(?P<word>[aeiouy]+.*?)+(.[aeiouy].)+(?P=word).*?',spell)
  try:
    ans = m.group(0)
    ans="Spell!"
    print "Case #"+str(i+1)+": "+ans#+" "+spell
  except AttributeError:
    print "Case #"+str(i+1)+": Nothing."#+spell

