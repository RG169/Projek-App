def celsiusTofahrenheit(c):
    return (c * 9/5) + 32

def celsiusTokelvin(c):
    return c + 273.15

def fahrenheitTocelsius(f):
    return (f - 32) * 5/9

def fahrenheitTokelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvinTocelsius(k):
    return k - 273.15

def kelvinTofahrenheit(k):
    return (k - 273.15) * 9/5 + 32

temp = []

while True:
    print("\nTemperature Converter")
    print("1: Celsius to Fahrenheit & Kelvin")
    print("2: Fahrenheit to Celsius & Kelvin")
    print("3: Kelvin to Celsius & Fahrenheit")
    print("4: Exit")
    flChoice = int(input("Choose a conversion option (1-4): "))

    if flChoice == 1:
        c = float(input("Enter temperature in Celsius: "))
        f = celsiusTofahrenheit(c)
        k = celsiusTokelvin(c)
        print(f"{c}°C = {f}°F")
        print(f"{c}°C = {k}K")
        temp.append(f"{c}°C = {f}°F")
        temp.append(f"{c}°C = {k}K")

    elif flChoice == 2:
        f = float(input("Enter temperature in Fahrenheit: "))
        c = fahrenheitTocelsius(f)
        k = fahrenheitTokelvin(f)
        print(f"{f}°F = {c}°C")
        print(f"{f}°F = {k}K")
        temp.append(f"{f}°F = {c}°C")
        temp.append(f"{f}°F = {k}K")

    elif flChoice == 3:
        k = float(input("Enter temperature in Kelvin: "))
        c = kelvinTocelsius(k)
        f = kelvinTofahrenheit(k)
        print(f"{k}K = {c}°C")
        print(f"{k}K = {f}°F")
        temp.append(f"{k}K = {c}°C")
        temp.append(f"{k}K = {f}°F")

    elif flChoice == 4:
        print("Thank you, for using our services.")
        break 
    else:
        print("Please select a number between 1 and 4.")
        
print("\nSummary of your conversions:")
for t in temp:
    print(t)

