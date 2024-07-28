n = int(input())

i=1
while i<=n:
    spaces = 1
    #spaces
    while spaces<=n-i:
        print(" ",end="")
        spaces+=1
    #increasing seq
    p=i
    j=1
    while j<=i:
        print(p,end="")
        p+=1
        j+=1
    #decreasing seq
    j=1
    p=2*i-2
    while j<=i-1:
        print(p,end="")
        p-=1
        j+=1
    print()
    i+=1
