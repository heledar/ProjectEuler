import sys, math

def is_narcissist(n):
    sum = 0
    for i in str(n):
        sum += math.pow(int(i), 5)
    return sum == n

sum = 0
for i in xrange(2, 1000000):
    if is_narcissist(i):
        sum += i
print sum
