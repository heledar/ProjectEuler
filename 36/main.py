import sys, math
MAX = 1000000

def isPalyndrome(n):
  tmp = str(n)
  for i in xrange(0, len(tmp)/2):
    if not tmp[i] == tmp[len(tmp)-1-i]:
      return False
  return True

getBin = lambda x: x >= 0 and str(bin(x))[2:] or "-" + str(bin(x))[3:]

ans = 0
for i in xrange(1, MAX+1):
  if isPalyndrome(i) and isPalyndrome(getBin(i)):
    ans += i
print ans
