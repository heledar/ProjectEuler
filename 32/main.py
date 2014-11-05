import sys, math

def divisors(n):
    div = set()
    for i in xrange(2, 1+int(math.sqrt(n))):
        if n % i == 0:
            div.add(i)
    return div

def is_pandigital(n):
  for div in divisors(n):
    tmp = str(div)+str(n)+str(n/div)
    if "0" in tmp:
      continue
    if len(tmp) == 9:
        p = dict()
        for c in tmp:
          if c not in p:
            p[c] = True
        if len(p) == 9:
          return True
  return False

sum = 0
for i in xrange(1, 10000):
  if is_pandigital(i):
    sum += i

print sum
