import sys, math

max = 0
sol = 0

for i in xrange(2, 1000+1, 2):
  nSol = 0
  for j in xrange(2, i/3+1):
    if i*(i-2*j) % (2*(i-j)) == 0:
      nSol += 1
  if nSol > sol:
    max = i
    sol = nSol

print max
