# a=int(input("enter a number:"))
# if a>=0 :
#     print("the number is positive ")
# else:
#     print("the number is negative")

# num=[1,-2,3,4,6,-8,-20,4]
# positive_num_count=0
# for i in num:
#     if i>0:
#         positive_num_count+=1
# print("final count:",positive_num_count)

# num=10
# even_count=0
# for i in range(1,num+1):
#     if i%2==0:
#         even_count+=1
# print("even count:",even_count)

# num=3
# for i in range(1,11):
#     if i==5:
#         continue
#     print(num,"x",i,"=",num*i)

#reverse string using loop
# input="python"
# reves_str=""
# for char in input:
#     reves_str=char+reves_str
# print("reversed string:",reves_str)


#FIRST  NON REPET CHAR
# str="teeateracac"
# for char in str:
#     print(char)
#     if str.count(char)==1:
#         print("char is:",char)
#         break #(use only 1st nonrepating  char)

#FACTORIAL USING WHILE
# num=int(input("enter a number is:"))
# fact=1
# while num>0:
#     fact=fact*num
#     num=num-1
# print("factorail of number",4,"is",fact)

#FOR NUMBER BETWEEN 1 TO 10
# while True:
#     num=int(input("enter a number from 1 to 10:"))
#     if 1<= num<=10:
#         print("thanks")
#         # break
#     else:
#         print("try again")

#PRIME NUMBER

# num=int(input("Enter a number:"))
# is_prime=True
# if num>1:
#     for i in range(2,num):
#         if(num%i)==0:
#             is_prime=False
#             break
# print(is_prime)

# Q UNIQ ITEM IN LIST
# items=["mango","banana","apple","orange","apple","orange"]
# uniq_items=set()
# for item in items:
#     if item in uniq_items:
#         print("dupplicate:",item)
#         break
#     uniq_items.add(item)


#Q
import time
wait_time=1
max_retrive=5
attempt=0
while attempt<max_retrive:
    print("attempt",attempt+1,"waittime",wait_time)
    time.sleep(wait_time)
    wait_time*=2
    attempt+=1

