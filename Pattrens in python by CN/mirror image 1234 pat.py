n = int(input())

i = 1
while i<=n:
    spaces=1
    while spaces <=n-i:
        print(" ",end="")
        spaces+=1
    nums=1
    while nums <=i:
        print(nums,end="")
        nums+=1
    print()
    i+=1