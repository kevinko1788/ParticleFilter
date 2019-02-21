from math import *
import random

N = # Number of particles
w = # weights of each particles len(N) = len (w)
p = [] # Particle vectors (x,y,heading)
p2 = [] # result

index = int(random.random() * N)
mw = max(w) #max weight
beta = #probability

for i in range(N): #|| len(p)
	beta += random.random() * 2 * mw

	while w[index] < beta:
		beta-= w[index]
		index = (index + 1) % N
	p2.append(p[index])
print p2

