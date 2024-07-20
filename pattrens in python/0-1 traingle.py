n=5

for i in range(n+1):
    for j in range(i):
        sum=i+j
        if (sum%2==0):
            print("0",end="")
        else:
            print("1",end="")
    print()