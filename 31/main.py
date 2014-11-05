import sys, math

sum = 0
for i in xrange(0, 2):
    for j in xrange(0, (200-i*200)/100+1):
        for k in xrange(0, (200-i*200-j*100)/50+1):
            for l in xrange(0, (200-i*200-j*100-k*50)/20+1):
                for m in xrange(0, (200-i*200-j*100-k*50-l*20)/10+1):
                    for n in xrange(0, (200-i*200-j*100-k*50-l*20-m*10)/5+1):
                        for o in xrange(0, (200-i*200-j*100-k*50-l*20-m*10-n*5)/2+1):
                            sum += 1
print sum
