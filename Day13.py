# Day 13 >>
# Lists >> list is written with []

# Exp:
s = []
print (s)

numbers = [1,2,3,4]
print(numbers)

fruits = ['apple','orang','banana']
print(fruits)

list1 = ['apple','orang','banana',1,2,3]
print(list1)

list2 = [1.2,3.4,1.0,5.5,0.0]
print(list2)

list3 = ['hi',0,'hello',1]
print(list3)

# print item in list :
print(numbers[0])
print(fruits[1])
print(list1[-1])

# print all items in the list :
for x in fruits:
	print(x)

# change the value of a specific item in list >> here we choose item 3 which is number one(1) 
list1[3] = 'cherry'
print(list1)

# removes the specific item from the list >> use (del)
del list2[0]
del list2[3] # note the index 3 here is 0.0 which have 3 index after remove previous item
print(list2)

# delete the list
del list3
print(list3)







