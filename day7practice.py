# with open("practice.txt","w") as f:
#     f.write("hi everyone\nwe are learning file I\O\n")
#     f.write("using python\nI like programing in python")


# with open("practice.txt","r") as f:
#     data=f.read()

# newdata=data.replace("python","java")
# print(newdata)

# with open("practice.txt","w") as f:
#     f.write(newdata)

# word="learning"
# with open("practice.txt","r") as f:
#     data=f.read()
#     if(data.find(word) !=-1):
#         print("found")
#     else:
#         print("not found")


#by using function
# def check_for_word():
#     word="learning"
#     with open("practice.txt","r")  as f:
#         data=f.read()
#         if(word in data):
#             print("found")
#         else:
#             print("not found")

# def check_for_line():
#     word="pyq"
#     data=True
#     line_no=1
#     with open("practice.txt","r")  as f:
#         while data:
#             data=f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no+=1
#     return -1 
# print(check_for_line())

# with open("integer.txt","r")  as f:
#     data=f.read()
#     print(data)
#     num=""
#     for i in range(len(data)):
#         if(data[i]== ","):
#             print(int(num))
#             num=""
#         else:
#             num+=data[i]


#or split method
count=0
with open("integer.txt","r")  as f:
     data=f.read()
     num=data.split(",")
     for val in num :
          if(int(val)%2==0):
               count+=1
print(count)

