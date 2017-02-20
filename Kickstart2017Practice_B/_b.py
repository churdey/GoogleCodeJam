#!/usr/bin/python
#Code for codejam 2017 Practice B
class ListElement:
  def __init__(self, value, next):
    self.value = value
    self.next = next
  def nth(self, n):
    o = self
    i = 0
    while i < n and o.next is not None:
       o = o.next
       i += 1
    return o

def init(multiset):
  multiset.sort() # ensures proper non-increasing order
  h = ListElement(multiset[0], None)
  for item in multiset[1:]:
    h = ListElement(item, h)
  return h, h.nth(len(multiset) - 2), h.nth(len(multiset) - 1)

def visit(h):
  """Converts our bespoke linked list to a python list."""
  o = h
  l = []
  while o is not None:
    l.append(o.value)
    o = o.next
  return l

def permutations(multiset):
  """Generator providing all multiset permutations of a multiset."""
  h, i, j = init(multiset)
  yield visit(h)
  while j.next is not None or j.value < h.value:
    if j.next is not None and i.value >= j.next.value:
      s = j
    else:
      s = i
    t = s.next
    s.next = t.next
    t.next = h
    if t.value < h.value:
      i = t
    j = i.next
    h = t
    yield visit(h)


if __name__ == '__main__':
  import sys
  import math
  import itertools

  data = sys.stdin.readlines()
#print data
 
  T = int(data.pop(0))
  #print "Cases", T
  for t in range(T):
    l = []
    N = data.pop(0)
    Nv = int(N.split()[0])
    Mv = int(N.split()[1])
    Tv = Nv+Mv
    for i in range(Tv):
      if i < Mv:
        l.insert(0,-1)
      else:
        l.insert(0,1)
    P = math.factorial(Tv)/(math.factorial(Nv)*math.factorial(Mv))
    print Nv, Mv, Tv, P, l
#    print perm, set, count, sum, leads, count/leads
    count = 0
    total = 0
    for permutation in permutations(l):
      goesneg = 0
      permsum = 0
      for item in permutation:
        permsum = item + permsum
        if (permsum <= 0):
          goesneg = 1
#        print item,
#      print
      count = float(count + 1)
      if (goesneg == 0):
        total = total + 1
#      print goesneg, count, total, float(total/count)
    print "Case #" + str(t+1) + ": "+ str(float(total/count))
    sys.stdout.flush()

