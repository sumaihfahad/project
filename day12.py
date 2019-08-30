
# Method 1 :
import re
x=5
y=7
order = 'Please, I want {} sandwishes and {} donutes'
change = 'a' 
order = re.sub(change,change.upper(),order)
print(order.format(x,y).replace('I','we'))


# Method 2 :
x=5
y=7
order = 'Please, I want {} sandwishes and {} donutes'
l = 'a'
table = str.maketrans(l,l.upper())
print(order.translate(table).format(x,y).replace('I','we'))


#Exp : how to use >> str.maketrans(   ,   )  and  translate (   )
old = '12345'
new = 'abcde'
table = str.maketrans(old,new)
A = 'I 1m h1ppy, th1nks for this ni35 qu5stion ^^ '
print(A.translate(table))