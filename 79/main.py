import time
startTime = time.time()

class Number:

  def __init__(self, val):
    self.val = val
    self.after = set()
    self.before = set()

  def getVal(self):
    return self.val

  def getAfter(self):
    return self.after

  def getBefore(self):
    return self.before

  def addAfter(self, N):
    if N not in self.after:
      self.after.add(N)

  def addBefore(self, N):
    if N not in self.before:
      self.before.add(N)

def printL(L):
  for a in L:
    print a
    print L[a].getBefore()
    print L[a].getAfter()

L = dict()
for i in xrange(0, 10):
  L[i] = Number(i)
f = open("try.txt", "r")
for line in f:
  line = line.replace("\n", "")
  temp = [int(i) for i in line]
  for i in xrange(len(temp)):
    for j in xrange(0, i):
      L[temp[i]].addAfter(temp[j])
    for j in xrange(i+1, len(temp)):
      L[temp[i]].addBefore(temp[j])

tmp = dict(L)
for k in L:
  if len(L[k].getBefore()) == 0 and len(L[k].getAfter()) == 0:
    del tmp[k]

L = dict(tmp)
made = False
ans = str()
while not made:
  for a in L:
    if len(L[a].getAfter()) == len(ans):
      ans += str(a)
      del tmp[a]
  if len(tmp) == 0:
    made = True
endTime = time.time()
print "Possible passcode is "+ans
print "Computation took "+str(endTime-startTime)+" seconds"
