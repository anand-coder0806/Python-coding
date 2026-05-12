# collection=set()
# collection.add(1)
# collection.add(2)
# collection.add(2)
# collection.add(3)
# collection.add("anand")
# collection.add((1,2,3,4))   #touple
# #collection.add([1,2,3,4])   #list and dict are not add in sets
# print(collection)
# print(type(collection))


# collection={"anand","python","world","HP"}
# collection.remove("anand")
# collection.pop()   #random value picked up
# print(collection)

set1={1,2,3,4}
set2={1,2,6,7}
print(set1.union(set2))
print(set1.intersection(set2))