f = open("input6.txt","r")

s = f.readlines()[0]

queue = []
n = 4 #14
for i in range(0,n):
    queue.append(s[i])

for i in range(n, len(s)):
    if len(set(queue)) == n:
        print(i)
        break
    else:
        queue.pop(0)
        queue.append(s[i])

        
