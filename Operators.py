##Mathematica Operators

a=4
b=2

print(a+b)  #Addition
print(a-b)  #Substraction
print(a*b)  #Multiplication
print(a**b)  #Exponents
print(a/b)  #division (always returns float value
print(a//b)  #division to get int value

'''order of execution PEMDAS
Paranthesis ()
Exponents **
Multiplication *
Division /
Addistion +
Subtraction -

always calculation starts from LEFT to RIGHT
()
**
*/
+-

'''
print(3*3+3/3-3)    #Result is 7.0 (How to what to do to get 3
print(3/3+3*3-3)
print(3*(3+3/3-3))

x=8
y=3
print(x/y)  #2.666666666
print(type(x/y))    #float
print(int(x/y)) #2
print(round(x/y))   #3
print(round(x/y,2)) #2.67

a=2
print(a)
a +=a
print(a)
a -=a
print(a)
a *=a
print(a)

A=5
A /=5
print(A)
