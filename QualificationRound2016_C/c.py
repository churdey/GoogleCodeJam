#!/usr/bin/python
#Code for codejam 2017 Practice A
import sys
data = sys.stdin.readlines()
#print data

#PrimeList, primes from 2-1000
primeList = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

#6 Digits, 33 through 66
#             123456
#startNum = 0b100001
#stopNum =  0b111111

#16 Digits, 32769 through 65535
#             1234567890123456
#startNum = 0b1000000000000001
#stopNum =  0b1111111111111111

#32 Digits
#             12345678901234567890123456789012
#startNum = 0b10000000000000000000000000000001
#stopNum =  0b11111111111111111111111111111111
 
T = int(data.pop(0))
#print "Cases", T
for t in range(T):
  Data = data.pop(0).split()
  N = int(Data[0])
  J = int(Data[1])
  #print N
  #print J
  print "Case #" + str(t+1) + ": "
  startNum = int(bin(2**(N-1)+1),2)
  stopNum = int(bin(2**(N)-1),2)
  testNum = startNum
  #print testNum
  all_composites = 0
  while ((testNum <= stopNum) & (all_composites < J)):
    testNumStr = str(bin(testNum))[2:]
    #print '********' + testNumStr
    Composite=True
    compList = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(2,11):
      factor = 0
      curVal = int(testNumStr,i)
      for primeVal in primeList:
        if (curVal % primeVal == 0) & (primeVal < curVal):
          factor = primeVal
          break
      if factor != 0:    
        #print i, curVal, factor
        compList[i-2] = factor
      else:
        #print i, curVal, "NOT_COMPOSITE"
        Composite = False
    if Composite:
      all_composites = all_composites+1
      print testNumStr + " " + " ".join(str(x) for x in compList)

    testNum = testNum + 2
    