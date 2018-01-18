# Input
name = raw_input("Your Name? ") #raw_input output String
age = input("How old are you? ") # input output integer
print "%s is %d year's old" % (name,age)
print("Half of your age is %d" % (age / 2))

# Calculating BMI
height = float(raw_input("What is your height? (inches or meters) "))
weight = float(raw_input("What is your weight? (punds or kilograms) "))
unit   = raw_input("Are your measurements in metric or imperial units? ").lower().strip()

if unit.startswith("i"):
    bmi = 703 * (weight / (height ** 2 ))
elif unit.startswith("m"):
    bmi = (weight / (height ** 2 ))

print("your BMI is %s" % bmi)
