# an=[1,2,3,4,5,6,7,8,9]
# for el in an:
#     print(el)

# num="anandbhagat"
# for char in num:
#     if(char== "d"):
#         print("d found")
#         break
#     print(char)    
# else:
#     print("end")

# print list
# num=[1,4,9,16,25,36,49,64,81,100]
# index=0
# for el in num:
#     index<len(num) #or9  
#     print(num[index])
#     index+=1

nums=[1,4,9,16,25,36,49,64,81,100]
x=49
indx=0
for el in nums:
    if(el == x):
        print("number found at index",indx)
        break
    indx+=1

