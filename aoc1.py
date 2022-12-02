f = open("aoc1.txt", "r")


sums = []
currentSum = 0 
for line in f: 
    if len(line.strip()) == 0:
        sums.append(currentSum)
        currentSum = 0
    if line.strip():
        currentSum += int(line)

#part one
##print(max(sums)) 

#part two 
sums.sort()
ret = sums[-1] + sums[-2] + sums[-3] 
print(ret)
