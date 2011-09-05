#!/usr/bin/python
#/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
#
#* File Name : solve.py
#
#* Purpose :
#
#* Creation Date : 01-09-2011
#
#* Last Modified : Fri 02 Sep 2011 01:38:18 PM EEST
#
#* Created By : Greg Liras <gregliras@gmail.com>
#
#_._._._._._._._._._._._._._._._._._._._._.*/

import sys

f = sys.stdin


cases = int(f.readline())

planet_dict = { 'a':'a queen',
'b':'a king',
'c':'a king',
'd':'a king',
'e':'a queen',
'f':'a king',
'g':'a king',
'h':'a king',
'i':'a queen',
'j':'a king',
'k':'a king',
'l':'a king',
'm':'a king',
'n':'a king',
'o':'a queen',
'p':'a king',
'q':'a king',
'r':'a king',
's':'a king',
't':'a king',
'u':'a queen',
'v':'a king',
'w':'a king',
'x':'a king',
'y':'nobody',
'z':'a king',
'A':'a queen',
'B':'a king',
'C':'a king',
'D':'a king',
'E':'a queen',
'F':'a king',
'G':'a king',
'H':'a king',
'I':'a queen',
'J':'a king',
'K':'a king',
'L':'a king',
'M':'a king',
'N':'a king',
'O':'a queen',
'P':'a king',
'Q':'a king',
'R':'a king',
'S':'a king',
'T':'a king',
'U':'a queen',
'V':'a king',
'W':'a king',
'X':'a king',
'Y':'nobody',
'Z':'a king'
}






for i in range(cases):
  country = f.readline()
  answer=planet_dict[country[-2]]
  print "Case #"+str(i+1)+": "+country[:-1]+" is ruled by "+answer+"."

