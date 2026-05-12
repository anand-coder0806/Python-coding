#print 1 to 100 number
# i=1
# while i<=100:
#     print(i)
#     i=i+1
# for i in range(1,101):
#     print(i)

#print 100 to 1 number
# i=100
# while i>=1:
#     print(i)
#     i=i-1

# for i in range(100,0,-1):
#     print(i)

#print multiplication table of a number
# i=int(input("enter any integir no. : "))
# # n=1
# # while n<=10:
# #     print(i*n)
# #     n=n+1
# for n in range(1,11):
#     print(i*n)

# #print square of a number
# i=int(input("enter any integir no. : "))
# print(i*i)
        
#print the square of a number 1to 10

# while i<=10:
#     print(i*i)
#     i+=1

# for n in range(1,11):
#     print(n*n)

#print list of number
# num=[1,4,9,16,25,36,49,64,81,10]   #list
# index=0
# while index<len(num):   #travesing of a list
#     print(num[index])
#     index+=1 
    






#print nimber from tuple
# num=(1,4,9,16,25,36,49,64,81,10)  #tuple
# x=36
# i=0
# while i<len(num):
#     if(num[i]==x):
#         print("number found at index",i)
#     i+=1

# num=(1,4,9,16,25,36,49,64,81,10,36,67,34,36)  #tuple
# x=36
# i=0
# while i<len(num):
#     if(num[i]==x):
#         print("number found at index",i)
#     else:
#         print("finding..")
#     i+=1


#by using break keyword

# num=(1,4,9,16,25,36,49,64,81,10,36,67,34,36)  #tuple
# x=36
# i=0
# while i<len(num):
#     if(num[i]==x):
#         print("number found at index",i)
#         break
#     else:
#         print("finding..")
#     i+=1
# print("end of loop")

#for skiping odd number 
# i=0
# while i<=10:
#     if(i%2==0):
#         i+=1
#         continue
#     print(i)
#     i+=1

 #for printing even no 
# i=0
# while i<=10:
#     if(i%2 !=0):
#         i+=1
#         continue
#     print(i)
#     i+=1


#print given no. is prime or not
# n=int(input("enter the number : "))
# i=2
# while i<= n-1:
#     if n%i == 0:
#         print("non prime number")
#     else:
#         i+=1
# print("prime number")

# num = 3
# # # Negative numbers, 0 and 1 are not primes
# if num > 1:
  
#     # Iterate from 2 to n // 2
#     for i in range(2, (num//2)+1):
        
#         # If num is divisible by any number between
#         # 2 and n / 2, it is not prime
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, "is a prime number")
# else:
#     print(num, "is not a prime number")


#print addition of n number using for loop
# n=int(input("enter any value : "))
# sum=0
# for i in range(1,n+1):
#     sum=sum+i
# print("total sum = " , sum)


#using while
# n=int(input("enter any value : "))
# sum=0
# i=1
# while i<=n:
#     sum+=i
#     i+=1
# print("toatl sum = ",sum)


#wap of factorial for loop
# n=5
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print("factorail of number = ",fact)


#with while loop
# n=int(input("enter any value : "))
# fact=1
# i=1
# while i<=n:
#     fact*=i
#     i+=1
# print("factorial= ",fact)


# num = 3

# # Negative numbers, 0 and 1 are not primes
# if num > 1:
#     for i in range(2, (num // 2) + 1):
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             break
#     else:
#         # This else belongs to the for-loop, not the if
#         print(num, "is a prime number")
# else:
#     print(num, "is not a prime number")
