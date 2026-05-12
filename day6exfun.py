# def avg_num(a,b,c):
#     avg=(a+b+c)/2
#     print(avg)
#     return avg
# avg_num(10,2,5)
# avg_num(78,5,57)

cities=["nagpur","pune","mumbai","amravati"]
num=[1,2,3,4,6,7,9]
def cal_len(list):
    print(list)
# cal_len(len(num))    no need of erese the function becz the not be a printing statment
# cal_len(len(cities)  )  
def cal_lenth(list):
    for items in list:
        print(items, end=" ")
cal_lenth(cities)
cal_lenth(num)

# def cal_fact(n):
    
#     fact=1
#     for i in range(1,n+1):
#         fact*=i
#         print(fact)
# cal_fact(6)

# def con_vert(usd_val):
#     inr_val = usd_val *83
#     print( usd_val ,"USD", inr_val, "INR")
# con_vert(78)

# def even_odd(n):
#     if (n%2== 0):
#         print("even")
#     else:
#         print("odd")
# even_odd(7)