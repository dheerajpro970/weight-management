from logic import BMI
print("this is in the new file")

#enter the user input weight in kgs
weight = float(input("Enter the weight in kgs:"))

#enter user input height in cms
height = float(input("Enter the height in cms:"))


print(f"your weight is {weight}kgs and your height is {height}cms")

bmi = BMI(weight,height)
print(f"Your BMI value {bmi}")