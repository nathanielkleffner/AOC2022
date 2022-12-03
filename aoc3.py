f = open("input3.txt","r")
lines = f.readlines()
score = 0

#PART 2 
n = 3
groups = [lines[i:i+n] for i in range(0,len(lines),n)]
for group in groups:
    commonSet = set(group[0].strip()) & set(group[1].strip()) & set(group[2].strip())
    commonItem = list(commonSet)[0]

#PART 1
#for line in f:

    #part one
    #comp1, comp2 = line[:len(line)//2], line[len(line)//2:]
    #commonSet = set(comp1).intersection(comp2)
    #commonitem = list(commonSet)[0]
    if (commonItem.isupper()):
        score += ord(commonItem) - 38
    if (commonItem.islower()): 
       score += ord(commonItem) - 96



print(score)
    
    

    
