def calculate_bmi(weight, height):
    return weight / height ** 2

def classification(bmi):
    if bmi > 0 and bmi < 18.5:
        return "Underweight"
    elif bmi > 18.5 and bmi < 24.9:
        return "Normal weight"
    elif bmi > 24.9 and bmi < 29.9:
        return "Overweight"
    elif bmi > 30.0 and bmi < 34.9:
        return "Class 1 Obesity"
    elif bmi > 34.9 and bmi < 39.9:
        return "Class 2 Obesity"
    elif bmi == 40.0:
        return "Class 3 Obesity"
    else: 
        return "You may have entered invalid values... please try again."
    
def calculate_change_to_normal_weight(bmi):
    if bmi < 18.5:
        print(f"For you to reach a normal weight, you need to gain {(24.9 - bmi):.2f} kg.")
    elif bmi > 24.9:
        print(f"For you to reach a normal weight, you need to lose {(bmi - 24.9):.2f} kg.")
