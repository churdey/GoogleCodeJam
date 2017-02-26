#!/usr/bin/python
#Code for codejam 2017 Practice A
import sys
data = sys.stdin.readlines()
#print data
 
T = int(data.pop(0))
print "Cases", T
for t in range(T):
  N = str(data.pop(0)).strip()
  print "Case #" + str(t+1) + ": " + N
