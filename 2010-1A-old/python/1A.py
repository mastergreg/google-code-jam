#!/usr/bin/python
#/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
#
#* File Name : 1A.py
#
#* Purpose :
#
#* Creation Date : 29-08-2011
#
#* Last Modified : Tue 30 Aug 2011 01:52:27 AM EEST
#
#* Created By : Greg Liras <gregliras@gmail.com>
#
#_._._._._._._._._._._._._._._._._._._._._.*/
import string

def gravity(L):
  newL = []
  for i in L:
    if i != '.':
      newL.append(i)
  start = len(newL)
  newL.reverse()
  for j in range(start,len(L)):
    newL.append('.')
  newL.reverse()
  return newL

def check_horiz_R(L,K):
  sub = ""
  for i in range(K):
    sub=sub+"R"
  for ls in L:
    s = "".join(ls)
    if string.find(s,sub) != -1:
      return "R"
  return ""

def check_horiz_B(L,K):
  sub = ""
  for i in range(K):
    sub=sub+"B"
  for ls in L:
    s = "".join(ls)
    if string.find(s,sub) != -1:
      return "B"
  return ""

def check_horiz(L,K):
  ret1 = check_horiz_R(L,K)
  ret2 = check_horiz_B(L,K)
  ret = ret1 + ret2
  return ret
    
def check_diag_B(L,K,N):
  for i in range(N-K):
    for j in range(N-K):
      curr = L[i][j]
      if curr == "B":
        for k in range(1,K):
          temp = L[i+k][j+k]
          if temp == ".":
            break
          elif temp != curr:
            break
          else:
            if k == K-1:
              return "B"
            else:
              continue
    for j in range(N-1,K-2,-1):
      curr = L[i][j]
      if curr == "B":
        for k in range(1,K):
          temp = L[i+k][j-k]
          print temp
          if temp == ".":
            break
          elif temp != curr:
            break
          else:
            if k == K-1:
              return "B"
            else:
              continue
  return ""
def check_diag_R(L,K,N):
  for i in range(N-K):
    for j in range(N-K):
      curr = L[i][j]
      if curr == "R":
        print curr
        for k in range(1,K):
          temp = L[i+k][j+k]
          if temp == ".":
            break
          elif temp != curr:
            break
          else:
            if k == K-1:
              return "R"
            else:
              continue
    for j in range(N-1,K-2,-1):
      curr = L[i][j]
      if curr == "R":
        for k in range(1,K):
          temp = L[i+k][j-k]
          if temp == ".":
            break
          elif temp != curr:
            break
          else:
            if k == K-1:
              return "R"
            else:
              continue
  return ""

def check_diag(L,K,N):
  ret1 = check_diag_B(L,K,N)
  ret2 = check_diag_R(L,K,N)
  ret = ret1+ret2
  return ret









class case:
  def __init__(self,T,N,K,STR_LST):
    self.T,self.N,self.K,self.STR_LST = T,N,K,STR_LST
  def rotate(self):
    self.STR_LST = zip(*self.STR_LST[::-1])
  def printMe(self):
    print "Case #",self.T,",",self.N,",",self.K
    for ln in self.STR_LST:
      print "".join(ln)
  def gravity(self):
    newSTR_LST = []
    for ln in self.STR_LST:
      newLn = gravity(ln)
      newSTR_LST.append(newLn)
    self.STR_LST=newSTR_LST
  def check(self):
    r1 = check_horiz(self.STR_LST,self.K)
    if len(r1) == 2:
      return "Both"
    rd1 = check_diag(self.STR_LST,self.K,self.N)
    if len(rd1) == 2:
      return "Both"
    self.rotate()
    r2 = check_horiz(self.STR_LST,self.K)
    if len(r2) == 2:
      return "Both"
    ans = "".join([r1,rd1,r2])
    if ans == "":
      return "Neither"
    elif string.find(ans,"R") != -1:
      if string.find(ans,"B") != -1:
        return "Both"
      else:
        return "Red"
    else:
      return "Blue"
      

def parseInput(f):
  myin = open(f,"r")
  first_lines = myin.readline()
  ALL_cases=[]
  cases = int(first_lines[:len(first_lines)-1])
  for i in range(cases):
    case_N = i+1
    first_case_line = myin.readline().split()
    N = int(first_case_line[0])
    K = int(first_case_line[1])
    case_LS = []
    for j in range(N):
      case_LS.append(myin.readline()[:N])
    ALL_cases.append(case(case_N,N,K,case_LS))
  return ALL_cases

cases = parseInput("A-small-practice.in")
for c in cases:
  #c.printMe()
  c.gravity()
  c.printMe()
  ans = c.check()
  print "Case #"+str(c.T)+": "+ans
  
"""
  rlines=[]
  for line in lines:
    rline = line[:len(line)-1]
    rlines.append(rline)
  return rlines

for gr in grammes:
  print gr

  """
  
