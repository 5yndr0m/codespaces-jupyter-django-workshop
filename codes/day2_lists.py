list1 = ["apple","banana","cherry","orange"]
print("List 1 : ", list1)
print("data type : ", type(list1))
print("iterate through list using for")
for x in list1:
    print(x)
print()
#lists can be modified

list1[2]="watermelon"
print("list 1 :", list1)
print("length of list : ", len(list1))
print("remove element : ", list1.pop())
print("after removing : ", list1)
list1.insert(1,"strawberry")
print("after adding new element : ", list1)
print()

tuple1 = ("car", "bus", "van")
print("tuple1 : ", tuple1)
print("data type : ", type(tuple1))
list1.extend(tuple1)
print("list with tuple : ", list1)
#tuples cant be modified
print()

set1 = {'a', 'b', 'c', 'd'}
print("set : ",set1)
print("data type : ", type(set1))
#set will be changing indexes
#set cant have duplicated values : even if it contains duplicates, it only shows one
set1.add('e')
print("after adding element : ", set1)
print()

dit1 = {"number" : 2, "brand" : "sofa"}
print("dictionery : ", dit1)
print("data type : ", type(dit1))
print("brand : ", dit1["brand"])
