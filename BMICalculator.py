##BODY MASS INDEX CALCULATOR

##----BMI=Weight (kg)/hieght*Height (in metere)

Weight = int(input('Enter your weight:-'))
Height=float(input('Enter your Height:-'))
BMI=Weight/Height**2
#BMI=print(F'Your BMI is {BMI}')

if BMI < 18.5:
    print(f"your BMI is {BMI}, and you are underweight")
elif BMI > 18.5 and BMI < 25:
    print(f"your BMI is {BMI}, and you have Normal weight")
elif BMI >= 25 and BMI < 30:
    print(f"your BMI is {BMI}, and you have slightly overweight")
elif BMI >= 30 and BMI < 35:
    print(f"your BMI is {BMI}, and you are obese")
else:
    print(f"your BMI is {BMI}, and you are clinically obese")
