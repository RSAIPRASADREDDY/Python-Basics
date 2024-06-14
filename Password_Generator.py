#Password_Generator Project
import random
letters = ['a','b','c','d','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','^','&','*','(',')']

print('Welcome to the password generator')
Required_letters=int(input("How many letters required for password \n"))
Required_symbols=int(input("How many symbols required for password \n"))
Required_numbers=int(input("How many numbers required for password \n"))
'''
#Easy level password
password=''
for char in range(1,Required_letters+1):
    password += random.choice(letters)
for char in range(1, Required_symbols + 1):
    password += random.choice(symbols)
for char in range(1, Required_numbers + 1):
    password += random.choice(numbers)
print(password)
'''
#Hard level password
password_list=[]
for char in range(1,Required_letters+1):
    password_list += random.choice(letters)
for char in range(1, Required_symbols + 1):
    password_list += random.choice(symbols)
for char in range(1, Required_numbers + 1):
    password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

newpassword=''
for char in password_list:
    newpassword = newpassword+char
print(f'your password is {newpassword}')



