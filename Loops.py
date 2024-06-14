#Loops are running continuesly untill it fails for next condition

'''
Family_Names = ['Satyavathi','Venkatesh','Supriya','Sai Prasad reddy','Mounica','Laasya','Veera','Kush'];
for family in Family_Names:
    print('Reddy ' + family)
print(Family_Names)


#Calculate Average height ,hiegest Height,no.of of student from the list
student_Height=input().split()
print(student_Height)
total_students=len(student_Height)
print(total_students)

total_height=0
hiegest_Height=0
for hieght in student_Height:
    #print(hieght)
    total_height = total_height+int(hieght)
    #print(hieght)
    if int(hieght)>hiegest_Height:
        hiegest_Height=int(hieght)
        #print(hiegest_Height)

    #student_Height +=student_Height
print(f'Total hieght of Students {total_height}')
print(f'Total no of Students {total_students}')
Average_Height= int(total_height/total_students)
print(f'Avg hieght of Students {Average_Height}')
print(f'hiegest_Height of Student {hiegest_Height}')
'''

'''
##----Some practice on generating even and odd number
a=1
b=20
#printing odd numbers
for number in range(a,b,2):
    print(number)
#printing even numbers
for number in range(2,b,2):
    print(number)
'''

##FizzBuzz job inteview question

for n in range(1, 101):
    if n%3==0 and n%5==0:
        print('FizzBuzz')
    elif n%3==0:
        print('Fizz')
    elif n%5==0:
        print('Buzz')
    else:
        print(n)