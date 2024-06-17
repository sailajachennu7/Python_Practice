list1=[1,2,3,2,1]
list2=[5,6,7,5]

copy_list1=list1.copy()
copy_list1.reverse()

if(copy_list1==list1):
    print("it is a palindrome")
else:
    print("not a palindrome")