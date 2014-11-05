from euler import isPentagonal

found = False
i = 0
while not found:
  i += 1
  pi = i*(3*i-1)/2
  for j in xrange(1, i):
    pj = j*(3*j-1)/2
    if isPentagonal(pi-pj) and isPentagonal(pi+pj):
      found = True
      break
print pi-pj
