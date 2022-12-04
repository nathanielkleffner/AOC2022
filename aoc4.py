

#part 1
def check_range(a,b,n,m):
    return  (a <= n and m <= b) or (n <= a and b <= m)

#part 2
def check_range2(a,b,n,m):
    return (n <= a <= m) or (n <= b <=m) or (a <= n <= b) or (a <= m <= b) 

if __name__ == "__main__":
    f = open("input4.txt","r")
    sum = 0 
    for line in f:
        first, second = line.split(",")[0], line.split(",")[1].strip()
        a,b = int(first.split("-")[0]), int(first.split("-")[1])
        n,m = int(second.split("-")[0]), int(second.split("-")[1])
        if(check_range2(a,b,n,m)):
            sum += 1
        
    print(sum)
        
        
    
    
        
