# def show(n):
#     if(n==0):
#         return
#     print(n)
#     show(n-1)

# show(10)
def fact(n):
    if(n==1 or n==0):
        return 1
    return fact(n-1)*n
print(fact(5))

#first n natural number
# def nat_num(n):
    
#     if(n==0):
#         return 0
    
    
#     return nat_num(n-1)+n
# sum=nat_num(5)
# print(sum)
#print list with index
# def print_list(list,idx):   #or idx=0
#     if(idx==len(list)):
#         return
#     print(list[idx])
#     print_list(list,idx+1)

# fruits=["mango","banana","orange","greps"]
# print_list(fruits,0)  #(fruits)