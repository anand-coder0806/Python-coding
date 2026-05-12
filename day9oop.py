# class student:
#     def __init__(self,name):
#         self.name=name

# s1=student("anand")
# print(s1.name)
# del s1.name   #for deleting
# print(s1.name)

# class account:
#     def __init__(self,acc_no,acc_pass):
#         self.acc_no=acc_no
#         self.__acc_acc_pass=acc_pass   #for privatization __ is used(double underscor)
# acc1=account("12345","abcd")
# print(acc1.acc_no)  
# print(acc1.__acc_pass)      



# class account:
#     def __init__(self,acc_no,acc_pass):
#         self.acc_no=acc_no
#         self.__acc_pass=acc_pass
    
#     def rest_pass(self):  #becz it is in the class
#         print(self.__acc_pass)


# acc1=account("12345","abcd")
# print(acc1.acc_no)  
# print(acc1.rest_pass)      

#not use out side of the class
class person:
    def __hello(self):
        print("hello person!")

    def welcome(self):
        self.__hello()

p1=person()
print(p1.welcome)