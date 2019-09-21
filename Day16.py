# Day 16 .. Tuples :
thisTuple = ()
print(thisTuple)
thisTuple2 = (3)
print(thisTuple2)
fruits = ('apple','orang','banana','Kiwi','orang')
print(fruits)
thisTuple3 = (2,1,3.5,6,'Sara')
print(thisTuple3)
print(thisTuple3[4])
print(thisTuple3[4][2])
print(thisTuple3[1:4])

for i in fruits :
	print(i)

# we can't change Tuple Values :
#thisTuple2[0] = 'hi'
#print(thisTuple2)
thisTuple4 = ['hello']
thisTuple4[0] = 'hi'
print(thisTuple4)

del thisTuple2 
#print(thisTuple2)