import numpy as np
f = open("input8.txt","r")


def viewDistance(trees,n,b):
    if b:
        trees.reverse()
    ret = 0
    for i in range(0,len(trees)):
        if(trees[i] >= n):
            ret += 1
            break
        elif (n > trees[i]):
            ret +=1
    return ret 



if __name__ == "__main__":
    lines = f.readlines()
    rows = []

    for line in lines:
        rows.append([int(x) for x in line.strip()])


    numColumns = len(rows[0])
    numRows = len(rows)

    columns = [] 
    for a in range(0,numRows): 
        column = [] 
        for b in range(0,numColumns):
            column.append(rows[b][a])
        columns.append(column)

    maxscore = 0
    for i in range(1,numRows-1):
        row = rows[i]
        for j in range(1,numColumns-1):
            column = columns[j]
            n = row[j]
            #part 1
            up = max(column[:i])
            left = max(row[:j])
            down = max(column[i+1:])
            right = max(row[j+1:])
            if( n > up or n > left or n > down or n > right):
                maxscore +=1
            
            #part 2 
            #up  = viewDistance(column[:i],n,True)
            #left = viewDistance(row[:j],n,True)
            #down = viewDistance(column[i+1:],n,False)
            #right = viewDistance(row[j+1:],n,False)
            #score = up * left * down * right
            #if (score > maxscore):
            #       maxscore = score
            
    #part 1
    print(maxscore + 2*numColumns + 2*(numRows-2))
        
    #part 2
    #print(maxscore)



    
    
        
        
        
