import sys, math

def divisors(n):
    div = set()
    for i in xrange(2, 1+int(math.sqrt(n))):
        if n % i == 0:
            div.add(i)
            div.add(n/i)
    return div

def is_abundant(n):
    return sum(divisors(n)) > n

def is_sum_abundant(n, abundant_numbers, abundant_numbers_set):
    for i in abundant_numbers:
        if i > n:
            return False
        if n-i in abundant_numbers_set:
            return True
    return False

abundant_numbers = list()
for i in xrange(12, 28123+1):
    if is_abundant(i):
      abundant_numbers.append(i)
abundant_numbers_set = set(abundant_numbers)

sum = 0
for i in xrange(1, 28123):
    test = is_sum_abundant(i, abundant_numbers, abundant_numbers_set)
    if not test:
        sum += i

print sum
