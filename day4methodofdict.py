student={
     "name":"anand",
     "subsject" :{
         "math":87,
        "phy":78,
         "chem":89,

     }
}
# print(student.keys())   #only keys   not nested keys
# print(list(student.keys()))   #type casting   dict into list
# print(student.values())  #all values
# print(list(student.values()))
# print(student.items())
# print(list(student.items()))
# an=list(student.items())       #for getting specificnitems
# print(an[1])
# print(student.get("name"))    #method for specific keys
# print(list(student.get("name")))
# student.update({"city":"amravati"})
# print(student)
#for getting new dict to update the key values
newdict=({"age":20})
student.update(newdict)
print(student)
# print(student["name"])