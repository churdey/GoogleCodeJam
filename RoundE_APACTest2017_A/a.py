#!/usr/bin/python
#Code for Round E APAC Test 2017

import sys
data = sys.stdin.readlines()
#print data
 
T = int(data.pop(0))
for t in range(T):
  c = str(data.pop(0))
  l = data.pop(0).split()
  i = int(l[0])
  j = int(l[1])
  print c, i, j, len(c)
  print "Case #" + str(t+1) + ": " 


