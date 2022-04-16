numberOfLoops = 0
numberOfApples = 2
while numberOfLoops < 10:
    print(numberOfLoops)
    numberOfApples *= 2
    numberOfApples += numberOfLoops
    numberOfLoops -= 1
    print(numberOfApples)
print("Number of apples: " + str(numberOfApples))
