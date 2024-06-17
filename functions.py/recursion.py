def cal_sum(n):
    if(n==0):
        return 0
    return cal_sum(n-1) +n
sum=cal_sum(10)
print(sum)