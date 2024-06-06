##---Data Types are type of value which store in variable
##Might be String,Int,Float,Boolean

Name="Sai Reddy"    # Name variable string data type
Typeofvariable=type(Name)  ##It gives what type the variable is
print(Typeofvariable)

print(Name[0])  ##Slicing of string always starts with 0(ZERO)
print(Name[-1]) ##Negative indicates from ending
print(Name[0:4])    ##start(Included) and end(end is excluded) if start is 0 its optional
print(Name[4:])

Salary=90000    # Name variable string data type
Typeofvariable=type(Salary)  ##It gives what type the variable is
print(Typeofvariable)

##----Type conversion
print(f"Conversion of DataType {type(float(Salary))} ") #We convert int to float and vice-versa

Increment=9.8    # Name variable string data type
Typeofvariable=type(Increment)  ##It gives what type the variable is
print(Typeofvariable)

##----BOOLEAN DATA TYPE
a=10
b=5
print(a<b)
print(a>b)