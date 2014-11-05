import sys, math

minA = 2
maxA= 100
minB = 2
maxB = 100
list = []
for a in xrange(minA, maxA+1):
    for b in xrange(minB, maxB+1):
        r = math.pow(a, b)
        if not r in list:
            list.append(r)
print len(list)
