'''
you can check for year 2000,2023,2024,2100
'''
# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? \n "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
IF=year%4
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("1This is  a leap year")
        else:
            print("1This is not a leap year")
    else:
        print("2This is a leap year")
else:
    print("2This is not a leap year")


