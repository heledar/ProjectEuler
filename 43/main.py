from euler import isPandigital
from itertools import permutations

def t43(i):
  if int(i[1]+i[2]+i[3])%2 == 0:
    if int(i[2]+i[3]+i[4])%3 == 0:
      if int(i[3]+i[4]+i[5])%5 == 0:
        if int(i[4]+i[5]+i[6])%7 == 0:
          if int(i[5]+i[6]+i[7])%11 == 0:
            if int(i[6]+i[7]+i[8])%13 == 0:
              if int(i[7]+i[8]+i[9])%17 == 0:
                return True
  return False

data = [''.join(p) for p in permutations('0123456789')]
sum = 0
for i in data:
  if t43(i):
    sum += int(i)
print sum
