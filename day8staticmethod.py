# class student:
#     collegename="pote college"
#     def __init__(self,name,mark):   #constructor
#         self.name=name
#         self.mark=mark
    

#     @staticmethod    #decoretor
#     def hello():
#         print("hello")

    

# s1=student("anand",89)
# print(s1.name,s1.mark)
# s1.hello()


# ABSTRACTION
class car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False

    def start(self):
        self.clutch=True
        self.acc=True
        print("car started")

car1=car()
car1.start()
    

#practice Q
# class account:
#     def __init__(self,bal,acc):
#         self.balance=bal
#         self.account_no=acc

# acc1=account(1000,"abc56788")
# print(acc1.balance)
# print(acc1.account_no)

class account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc

    def debit(self,amount):
        self.balance-=amount
        print("rs",amount,"was debited")
        print("total balance= ",self.getbalance())

    def credit(self,amount):
        self.balance+=amount
        print("rs",amount,"was credited")
        print("total balance= ",self.getbalance())

    def getbalance(self):
        return self.balance


acc1=account(1000,"abc56788")
acc1.credit(500)
acc1.debit(1500)
acc1.credit(50000)
acc1.debit(3400)
