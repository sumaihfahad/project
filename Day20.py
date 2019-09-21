# Day20 >> Sets >> {} ..
# the set is unorder ..
fruits = {'apple','orang','banana','kiwi','orang'}
print(fruits)  #Note the set does not print the item twice.

# we can't use index in set >> so if we want to ceek if item in set >> we use :
# 1) for >> print all set ..
for i in fruits:
 	print(i)
# 2) in >> True or False
print ('orang' in fruits)

# Note : we can't change the items in the set..

# ADD ITEMS : we can add an items in the set >> use :
# 1) to add one item >> use (.add('')):
fruits.add('charry')
print(fruits)

# 2) to add more than one item >> use (.update(['',''])) :
fruits.update(['mango','strawberry'])
print(fruits)