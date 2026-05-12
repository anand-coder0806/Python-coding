class car: #parent class    #inheritance
    @staticmethod
    def start():
        print("car started")
    
    @staticmethod
    def stop():
        print("car stoped")
    

class toyotacar(car):  #child class
    def __init__(self,name):
        self.name=name
    
car1=toyotacar("fortuner")
car2=toyotacar("inova")
print(car1.name)
print(car1.start())

#multiple level inheritance
# class car: #grandparent class
#     @staticmethod
#     def start():
#         print("car started")
    
#     @staticmethod
#     def stop():
#         print("car stoped")
    

# class toyotacar(car):  #parent class
#     def __init__(self,brand):
#         self.brand=brand


# class fortuner(toyotacar):  #child class
#     def __init__(self,type):
#         self.type=type

# car1=fortuner("petrol")
# car2=fortuner("CNG")
# car3=toyotacar("inova")
# print(car3.brand)
# print(car1.type,car2.type)
# print(car1.start())


#multiple inheritance
# class A:
#     varA="welcome to class A"

# class B:
#     varB="welcome to class B"

# class C(A,B):
#     varC="welcomr to class C"

# c1=C()
# print(c1.varC)
# print(c1.varB)
# print(c1.varA)


#supermethod
# class car:
#     def __init__(self,type):
#         self.type = type
#     @staticmethod
#     def start():
#         print("car started")
    
#     @staticmethod
#     def stop():
#         print("car stoped")
    

# class toyotacar(car):  #child class
#     def __init__(self,name,type):
        
#         super().__init__(type)
#         super().start()
#         self.name=name

# car1=toyotacar("fortuner","CNG")

# print(car1.name)
# print(car1.type)

# class person:
#     name="anonymous"
     
#     def changename(self,name):
#         self.name=name

# p1=person()
# p1.changename("Anand Bhagat")
# print(p1.name)


# class person:
#     name="anonymous"
     
#     def changename(self,name):
#         person.name=name

# p1=person()
# p1.changename("Anand Bhagat")
# print(p1.name)
# print(person.name)


# class person:
#     name="anonymous"
     
#     def changename(self,name):
#         self.__class__.name="anand"

# p1=person()
# p1.changename("Anand Bhagat")
# print(p1.name)

#CLASS METHOD
# class person:
#     name="anonymous"
     
#     def changename(cls,name):
#         cls.name=name

# p1=person()
# p1.changename("Anand Bhagat")
# print(p1.name)


# class person:
#     def __init__(self,phy,chem,math):
#         self.phy=phy
#         self.chem=chem
#         self.math=math
#         self.percentage=str((self.phy + self.chem + self.math)/3) + "%"

# std1=person(90,89,88)
# print(std1.percentage)


# class person:
#     def __init__(self,phy,chem,math):
#         self.phy=phy
#         self.chem=chem
#         self.math=math
#         self.percentage=str((self.phy + self.chem + self.math)/3) + "%"
        
#     def calcpercentage(self):
#          self.percentage=str((self.phy + self.chem + self.math)/3) + "%"



# std1=person(90,89,88)
# print(std1.percentage)

# std1.phy=86
# print(std1.phy)
# std1.calcpercentage()
# print(std1.percentage)


#property
# class person:
#     def __init__(self,phy,chem,math):
#         self.phy=phy
#         self.chem=chem
#         self.math=math

#     @property
#     def percentage(self):
#         return str((self.phy + self.chem +self.math)/3)+"%"
    

# std1=person(89,78,65)
# print(std1.percentage)
# std1.phy=89
# print(std1.percentage)