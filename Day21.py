# Day 21 >> Sets 2 ..

fruits = {'apple','orang','banana','kiwi','orang'}
fruits1 = fruits.copy()

# to determine how many items in a set >> use (len(name set)) :
print(len(fruits))

# to remove item :
# 1- remove the specific item >> use (.remove('')) OR (.discard(''))
fruits.remove('orang')
fruits.discard('kiwi')
print(fruits)

# 2- remove an itme (random item ) >> use (.pop()) ..
fruits.pop()
print(fruits)

# to clear the set (delet all items in the set) >> use (.clear())
fruits.clear()
print(fruits)

# to delete the set >> use (del)  
del fruits
#print(fruits)
print(fruits1)

#an other way to create a set >> use set(())
hiSet = set(('hi','hello','weloome'))
print(hiSet)

# Exercises :
fruits2 = set(('apple','banana','kiwi','charry'))
difFruits = fruits1.difference(fruits2)
print(fruits1,fruits2)
print(difFruits)
print(fruits2.difference(fruits1))
print(fruits1.difference(fruits2))
fruits1.difference_update(fruits2) # the set fruits1 have orang which is not in fruits2 >> so set 
print(fruits1)

