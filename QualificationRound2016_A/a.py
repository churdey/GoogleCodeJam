#!/usr/bin/python
#Code for codejam 2017 Practice A
import sys
data = sys.stdin.readlines()
#print data
 
T = int(data.pop(0))
#print "Cases", T
for t in range(T):
  N = int(data.pop(0))
  lnums = [0,0,0,0,0,0,0,0,0,0]
  for n in range(1,10000):
    Nstr = list(str(n*N))
    if str(0) in Nstr:
      lnums[0] = 1
    if str(1) in Nstr:
      lnums[1] = 1
    if str(2) in Nstr:
      lnums[2] = 1
    if str(3) in Nstr:
      lnums[3] = 1
    if str(4) in Nstr:
      lnums[4] = 1
    if str(5) in Nstr:
      lnums[5] = 1
    if str(6) in Nstr:
      lnums[6] = 1
    if str(7) in Nstr:
      lnums[7] = 1
    if str(8) in Nstr:
      lnums[8] = 1
    if str(9) in Nstr:
      lnums[9] = 1
    if (lnums[0] & lnums[1] & lnums[2] & lnums[3] & lnums[4] & lnums[5] & lnums[6] & lnums[7] & lnums[8] & lnums[9]) == 1:
      #print ''.join(Nstr)
      break
    #print ''.join(Nstr), lnums
  if (lnums[0] & lnums[1] & lnums[2] & lnums[3] & lnums[4] & lnums[5] & lnums[6] & lnums[7] & lnums[8] & lnums[9]) == 1:
    print "Case #" + str(t+1) + ": " + ''.join(Nstr)
  else:
    print "Case #" + str(t+1) + ": " + "INSOMNIA"
