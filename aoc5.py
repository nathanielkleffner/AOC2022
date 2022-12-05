f = open("input5.txt","r")

grid = {}
lines = f.readlines()



#make a dict of arrays 
row = 1
column = 0 
for line in lines:
    if line.strip()[0] == "1":
        break
    x = line[1::4]
    y = [*x]
    for i in range(0,len(y)):
        c = y[i]
        if len(c.strip()) != 0:
            if i+1 in grid.keys():
                grid[i+1].insert(0,c)
            else:
                grid.update({i+1:[c]})
        column = i+1
            
            
    row += 1
            
for line in lines[row+1:]:
    split = line.strip().split(" ")
    qty, from_, to_ = int(split[1]), int(split[3]), int(split[5])
    stack = []
    
    #part 1
    for i in range(qty):
       c = grid[from_].pop(-1)
       grid[to_].append(c)

    #part 2
    #for i in range(qty):
    #    c = grid[from_].pop(-1)
    #    stack.append(c)

    #for j in range(len(stack)):
    #    grid[to_].append(stack.pop(-1))
        

ret = ""
for j in range(1,column+1):
    ret += grid[j][-1]

print(ret)

    

