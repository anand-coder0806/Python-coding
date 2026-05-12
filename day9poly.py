#inbuild overloading
# print(1+2) #adding
# print("anand"+"bhagat") #concatination
# print([1,2,3] + [4,5,6])  #merge
# print(type(1))
# print(type("anand"))
# print(type([1,2,3]))


  #manual overloading with  polymorphism
#operator overloading
#dunder function
# class complex:
#     def __init__(self,real,img):
#         self.real=real
#         self.img=img

#     def shownum(self):
#         print(self.real, " i +",self.img, "j")

#     def add(self,num2):
#         newreal=self.real + num2.real
#         newimg=self.img + num2.img
#         return complex(newreal,newimg)
# num1=complex(1,3)
# num1.shownum()
# num2=complex(2,5)
# num2.shownum()
# num3=num1.add (num2)
# num3.shownum()

#addition
# class complex:
#     def __init__(self,real,img):
#         self.real=real
#         self.img=img

#     def shownum(self):
#         print(self.real, " i +",self.img, "j")

#     def __add__(self,num2):   #dunder function
#         newreal=self.real + num2.real
#         newimg=self.img + num2.img
#         return complex(newreal,newimg)
# num1=complex(1,3)
# num1.shownum()
# num2=complex(2,5)
# num2.shownum()
# add=num1+num2
# add.shownum()

#substraction
class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def shownum(self):
        print(self.real, " i +",self.img, "j")

    def __sub__(self,num2):   #dunder function
        newreal=self.real - num2.real
        newimg=self.img - num2.img
        return complex(newreal,newimg)
num1=complex(1,3)
num1.shownum()
num2=complex(2,5)
num2.shownum()
sub=num1-num2
sub.shownum()
