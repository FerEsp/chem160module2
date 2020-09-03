prev1 = 0
prev2 = 1
for i in range(20):
    current = prev1 + prev2
    print(current)
    prev2 , prev1 = prev1 , current
