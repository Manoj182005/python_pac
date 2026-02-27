def firstn(n, a):
    if(n == a-1):
        return 
    print(a, end=" ")
    firstn(n, a+1)
    

n = int(input("enter the number of rows:"))
firstn(n, 1)