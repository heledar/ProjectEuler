import sys, math

def pgcd(a,b):
  if b==0:
    return a
  else:
    r=a%b
    return pgcd(b,r)

n = 1
d = 1
for i in xrange(11, 100):
  if "0" in str(i):
    continue
  for j in xrange(11, 100):
    if "0" in str(j):
      continue
    for c in str(i):
      if c in str(j):
        if float(str(i).replace(c, "", 1))/float(str(j).replace(c, "", 1)) == float(i)/float(j) and float(i)/float(j) < 1:
          n *= int(str(i).replace(c, "", 1))/pgcd(int(str(i).replace(c, "", 1)),int(str(j).replace(c, "", 1)))
          d *= int(str(j).replace(c, "", 1))/pgcd(int(str(i).replace(c, "", 1)),int(str(j).replace(c, "", 1)))
print str(n/pgcd(n,d)) + " / " + str(d/pgcd(n,d))
