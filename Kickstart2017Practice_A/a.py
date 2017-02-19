#!/usr/bin/python
import sys
data = sys.stdin.readlines()
#print data
 
T = int(data.pop(0))
#print "Cases", T
for t in range(T):
  N = int(data.pop(0))
  mydat = data[:N]
  data = data[N:]
  maxlen = 0
  longname = ""
  mydat.sort()
  for name in mydat:
    oname = name.strip('\n')
    name = ''.join(name.split())
    name = "".join(set(name))
    if len(name) > maxlen:
      maxlen = len(name)
      longName = oname
#    print "** " + name + ", " + oname +", "+ longName
  print "Case #" + str(t+1) + ": " + longName


