unit = input("Celsius (C) or Fahrenheit (F)? (C/F): ")
temp = float(input("Enter the temperature: "))

if unit.upper() == "C":
    temp = (temp * 9/5) + 32
    print(f"The temperature in Fahrenheit is: {temp:.2f} F")
elif unit.upper() == "F":
    temp = (temp - 32) * 5/9
    print(f"The temperature in Celsius is: {temp:.2f} C")
else:
    print(f"{unit} is not valid.")
    