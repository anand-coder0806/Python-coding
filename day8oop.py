# class student:
#     name="anand"
# s1=student()
# print(s1.name)

# s2=student()
# print(s2.name)

# class car:   #class
#     name="BMW"   #diff parameter
#     model="M5"
# car1=car()    #object
# print(car1.name)
# print(car1.model)

# CONSTRUCTOR
# class student:
#     name="anand"
#     def __init__(self):
#         print("adding the new value in our database")
# s1=student()
# print(s1.name)

# class student:
#     def __init__(self,name):
#         self.name=name
#         print("adding new value in our database")  #optional line hai samjne ke liye likha sirf

# s1=student("Anand")
# print(s1.name)

  #by giving multiple parameter to object
# class student:
#     def __init__(self):   #default constructor
#         pass

#     def __init__(self,name,mark):  #parameterized constructor
#         self.name=name
#         self.mark=mark

# s1=student("Anand",97)
# print(s1.name,s1.mark)

# s2=student("jay",96)
# print(s2.name,s2.mark)



# class student:
#     collegename="pote college"
    
#     def __init__(self,name,mark):
#         self.name=name
#         self.mark=mark

# s1=student("anand",89)
# print(s1.name,s1.mark)
# print(s1.collegename)

# s2=student("jay",98)
# print(s2.name,s2.mark,s2.collegename)   #yesa bhi chalta 
        
# class student:
#     collegenmae="pote college"
#     name="xyz"                 #class attribute
#     def __init__(self,name):
#         self.name=name    #object attribute
#         print("adding new value in our database")  #optional line hai samjne ke liye likha sirf

# s1=student("Anand")
# print(s1.name)      #alwyas object attribute getting high priority with same class and object name
