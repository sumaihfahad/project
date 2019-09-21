# Day 17 .. Tuples2 :
fruits = ('apple','orang','banana','Kiwi','orang')
if 'banana' in fruits :
	print('yes, banana is in the fruits Tuple' )

print(len(fruits))

thisTuple = ('hi',) * 2
thisTuple2 = ('hi') * 2
print(thisTuple)
print(thisTuple2)

majer = fruits + thisTuple
print(majer)

x = (2,1.5,3,1)
x = x + (5,6)
print(x)

thisTuple3 = tuple((1,9,7,4))
print(thisTuple3)

number = [2,6,10,'hi']
thisTuple4 = tuple(number)
print(thisTuple4)

print(number.index('hi'))