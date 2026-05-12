mark=int(input("enter the mark of student: "))

if(mark>=90):
    grade="a"
elif(mark>=80 and mark<90):
    grade="b"
elif(mark>=70 and mark<80):
    grade="c"
elif(mark<35):
    grade="f"
else:
    grade="d"
print("grade of the student:" ,grade)