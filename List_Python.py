#List is a data strcture tyoe where a datatype can hold multiple values
#syntacx Listtype =[1,2,'a','b','c']
#list having index numbers starts with '0'

#Lists and getting values from index values
Family_Names = ['Satyavathi','Venkatesh','Supriya','Sai Prasad reddy','Mounica','Laasya','Veera','Kush']
print(type(Family_Names))
Family_Names[7]='Kush Baby' #
Family_Names.append('Reddy"s')
print(Family_Names[-2])

#fectching random values
import random
names_string    = input()
names   = names_string.split(",")
print(names)
num_items=len(names)
print(num_items)
random_choice = random.randint(0,num_items-1)
print(random_choice)
print(names[random_choice])



#Nested LISTS

Family_Names = ['Satyavathi','Venkatesh','Supriya','Sai Prasad reddy','Mounica']
Kids_Names=['Laasya','Veera','Kush']
Total_Family_Mambers=[Family_Names,Kids_Names]
print (Total_Family_Mambers)
