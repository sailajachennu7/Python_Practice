# N = int(input())

# n1=(N+1)//2
# n2=n1-1 #1

# i=1
# #1st half
# while i<=n1:
#     #spaces
#     spaces=1
#     while spaces<=n1-i:
#         print(" ",end="")
#         spaces+=1
#     #stars
#     stars=1
#     while stars<=2*i-1:
#         print("*",end="")
#         stars+=1
#     print()
#     i+=1
#     #2nd half
# i=n2 #1
# while i>=1:
#         #spaces
#     spaces=1
#     while spaces<=n2-i+1:
#         print(" ",end="")
#         spaces+=1
#         #stars
#     stars=1
#     while stars<=2*i-1:
#         print("*",end="")
#         stars+=1
#     print()
#     i-=1

N = int(input())

n1=4
n2=n1-1

#1st half
for i in range(1,n1+1):
    for spaces in range(1,(n1+1)-i):
        print(" ",end="")
    for stars in range(1,2*i):
        print("*",end="")
    print()
for i in range(n2,0,-1):
    for spaces in range(1,(n1+1)-i):
        print(" ",end="")
    for stars in range(1,2*i):
        print("*",end="")
    print()






