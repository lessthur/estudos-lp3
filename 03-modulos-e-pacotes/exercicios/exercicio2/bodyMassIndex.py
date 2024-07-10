import usableBmi

weight = float(input("Enter with your weight, in kg: "))
height = float(input("Enter with your height, in meters: "))

bmi = usableBmi.calculate_bmi(weight, height)

classification = usableBmi.classification(bmi)

print(f"\nYour Body Mass Index (BMI) is: {bmi:.2f}.")
print(f"Your classification is: {classification}.")
usableBmi.calculate_change_to_normal_weight(bmi)