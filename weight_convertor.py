
weight = float(input("Enter the weight: "))
unit = input("Kilograms (kg) or Pounds (lb)? (K/L): ")

if unit.upper() == "K":
    weight = weight * 2.205
    print(f"The weight in pounds is: {weight:.2f} lb")
elif unit.upper() == "L":
    weight = weight / 2.205
    print(f"The weight in kilograms is: {weight:.2f} kg")
else:
    print(f"{unit} is not valid.")
    