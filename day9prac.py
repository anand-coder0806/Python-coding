# class circle:
#     def __init__(self,radius):
#         self.radius=radius

#     def area(self):
#         print( 3.14 * self.radius **2)

#     def perimeter(self):
#         return 2 * 3.14 * self.radius
# c1=circle(2)
# print(c1.area)
# print(c1.perimeter)

# class emp:
#     def __init__(self,role,dept,salary):
#         self.role=role
#         self.dept=dept
#         self.salary=salary

#     def showdetails(self):
#         print("role=",self.role)
#         print("dept=",self.dept)
#         print("salary=",self.salary)

# class engg(emp):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         super().__init__("engineer","IT","80,000")
    


# engg1=engg("anand",21)
# engg1.showdetails()
# print("name=",engg1.name)
# print("age=",engg1.age)

class order:
    def __init__(self,item,price):
        self.item=item
        self.price=price
    def __gt__(self,ord2):
        print(self.price> ord2.price)

ord1=order("chips",20)
ord2=order("tea",15)
print(ord1>ord2)
