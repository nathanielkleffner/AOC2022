f = open("aoc2.txt","r")

#A,B,C
#Rock,Paper,Scissors
#X,Y,Z
#Lose,Draw,Win
scores = {'X':1,'Y':2,'Z':3}
loses = {'A':'Z', 'B': 'X', 'C':'Y'} 
ties = {'A':'X','B':'Y','C':'Z'}
beats = {'A':'Y','B':'Z','C':'X'}
score = 0 
for line in f:
    p1 = line[0]
    p2 = line[2]
    #part 1
    #score += scores[p2]
    #if(p2 == beats[p1]):
    #    score += 6
    #elif(p2 == ties[p1]):
    #    score += 3
    
    #part 2
    if(p2 == 'X'):
        score += scores[loses[p1]]
    if(p2 == 'Y'):
        score +=  scores[ties[p1]] + 3
    if(p2 == 'Z'):
        score += scores[beats[p1]] + 6

print(score)

    
