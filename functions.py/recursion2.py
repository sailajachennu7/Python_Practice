def print_list(list,idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)
    

movies=["isq","damarukam","lovely","love today"]
print_list(movies)