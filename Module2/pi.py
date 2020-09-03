import random , math
inside = 0
ntrials = 100000
for i in range(ntrials):
    x = random.random()
    y = random.random()
    if (x**2 + y**2) < 1.0:
        inside = inside + 1
pi = 4. * inside/ntrials
print("N=%d Error=%85f"%(ntrials, pi-math.pi), pi , math.pi)

