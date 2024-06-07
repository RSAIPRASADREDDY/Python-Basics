print ("Thank you for choosing PYTHON PIZZA's !!!")

size = input("Please size of PIZZA S,M or L? \n")
add_pepperoni = input("Do you need pepperoni Y or N? \n")
extra_Cheese = input("Do you need extra cheese Y or N? \n")
bill=0
if size == "S":
    bill=15
    print ("your Bill amount is $15 ")
elif size == "M":
    bill = 20
    print("your Bill amount is $20 ")
else:
    bill = 25
    print("your Bill amount is $25 ")

if   add_pepperoni == 'Y':
    if size == "S":
        bill +=2
    else:
        bill +=3

if extra_Cheese == 'Y':
    bill += 1
print(f"Thank you for choosing your total bill is: {bill}")

