# Day9
###format() fonction : using to combine strings and numbers >>


# without (format) >> error
age = 26
#txt = 'My name is Sumaih, I am' + age
#print(txt)


# ^^ with format()
txt = 'My name is Sumaih, I am {}'
print(txt.format(age))


guantity = 2
itemNo = 100
price = 75.8
MyOrder = 'I want {} pieces of item {} for {} SR'
print(MyOrder.format(guantity,itemNo,price))

MyOrder2 = 'I want to pay {2} SR for {0} pieces of item {1}'
print(MyOrder2.format(guantity,itemNo,price))

# Exercises for myself : 
print(MyOrder,MyOrder2.format(guantity,itemNo,price),sep='\n') # >> it is not working

person = {'name': 'Ahmad', 'age': 5 ,'nationality':'Saudi'}
fruit = ['apple','orange','banana']
print('my name is {0[name]}, I\'m {0[nationality]}, I\'m {0[age]} years old and I like {1[1]}'.format(person,fruit))