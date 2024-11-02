class BMICalculator:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def calculate_bmi(self):
        
        return self.weight / ((self.height)**2 )

    def determine_category(self):
        
        bmi = self.calculate_bmi()
        
        
        if bmi >= 30:
            return "Obesity"
        elif 25 <= bmi < 30:
            return "Overweight"
        elif 18.5 <= bmi < 25:
            return "Normal"
        else:
            return "Underweight"


height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))


bmi_calculator = BMICalculator(height, weight)


bmi = bmi_calculator.calculate_bmi()
category = bmi_calculator.determine_category()


print("BMI:", bmi)
print("Category:", category)
