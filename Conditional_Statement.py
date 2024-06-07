# Depending on the condiation below is the syntax
'''
if condition:
    Do This
else:
    Do this
'''

##'''
print ("Welcome to the ROllerCoaster!")
Height = int(input("What is your height in CM?\n"))
Bill = 0
if Height >= 120:
    print("Cangrtualtion's, "+"You can ride th rollercoaster")
    Age = int(input("what is your age? \n" ))
    if Age < 12:
        Bill = 5
        print("child ticket pay $5 Rs.")
    elif Age >= 12 and Age <= 18:
        Bill = 7
        print("please pay $7 Rs")
    else:
        Bill = 12
        print ("adults pay $12 Rs")

    Want_Photos = input("Do you want a photo taken? Y or N.")
    if Want_Photos == 'Y':
        Bill += 3
    print (f"your final bill is {Bill}")

else:
    print("Sorry, you have to grow taller before you can ride")
##'''


'''###---Assignement check weather number is even or odd
Number = int(input("Please enter number you would like to check? "))
if Number %2 == 0:
    print(f"{Number} number is even")
else:
    print(f"{Number} number is ODD")
'''

###---Assignement of Multiple if else statement

