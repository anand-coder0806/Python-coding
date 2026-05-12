# class student:
#     collegename="pote college"
#     def __init__(self,name,mark):   #constructor
#         self.name=name
#         self.mark=mark

#     def welcome(self):    #method
#         print("welecome student")

# s1=student("anand",89)
# print(s1.name,s1.mark)
# s1.welcome()


class student:
    collegename="pote college"
    def __init__(self,name,mark):   #constructor
        self.name=name
        self.mark=mark

    def welcome(self):    #method
        print("welecome",s1.name)

    def getmark(self):   #method
        print( "your mark is: ",self.mark)

s1=student("anand",89)

s1.welcome()
s1.getmark()
        
# class student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
        
#     def get_avg(self):
#         sum=0
#         for val in self.marks:
#             sum+=val
#         print("hi",self.name,"your avg score is",sum/3)

# s1=student("anand",[89,98,78])
# s1.get_avg()

# #by chnaging name anand to jay
# s1.name="jay" 
# s1.get_avg()