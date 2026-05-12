#  OPEN MODE
# f=open("demo.text","r")
# data=f.read()
# print(data)
# print(type(data))
# f.close() 
# 
#  
# f=open("demo.text","r")
# line1=f.readline()
# print(line1)
# f.close()

#WRITE MODE
# f=open("demo.text","w")
# f.write(" i fuck mama on my gadi\n om chutkhaycha")
# f.close()

# f=open("demo.text","r")
# print(f.read())
# f.close()
#APEND MODE
# f=open("demo.text","a")
# f.write("\n mama padara bc")
# f.close()

# #for write and apend mode atomatic file will bw created which is not be existed
# f=open("sample.txt","w")  #or "a"
# print(f.write("anand om"))
# f.close()

#r+
# f=open("demo.text","r+")
# f.write("abc xyz pqr")
# print(f.read())
# f.close()

#truncate file
# f=open("demo.text","w+")   #or "a+"
# print(f.read())
# f.write("abc")
# f.close()

#WITH SYNTAX
# with open("demo.text","r") as f:
#     data=f.read()
#     print(data)

# with open("demo.text","w") as f:
#     f.write("new data")


# f=open("demo.text","r")
# lines=f.readlines()
# #print(" ".join(map(lambda x:x.strip("\n"),lines))) or
# cleaned_lines=[]
# for i in lines:
#     cleaned_lines.append(i.strip("\n"))
# print(" ".join(cleaned_lines))

# f.close()

f=open("demo.text","w")
l=f.write("hey\nhii\nhello")
print(l)
for i in range(0,l):
    print(i)
f.close()

f=open("integer.txt","w")
l1=f.write("hey\nhii\nhello")
print(l1)
f.close()
