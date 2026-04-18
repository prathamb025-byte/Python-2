from temperature.celsius import f_to_c
from temperature.fahrenheit import c_to_f
from temperature.kelvin import c_to_k

print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")

choise=int(input("Enter your choise: "))
if choise==1:
    celsius=float(input("Enter the temperature in Celsius: "))
    fahrenheit=c_to_f(celsius)
    print(f"{celsius}°C is equal to {fahrenheit}°F")
elif choise==2:
    fahrenheit=float(input("Enter the temperature in Fahrenheit: "))
    celsius=f_to_c(fahrenheit)
    print(f"{fahrenheit}°F is equal to {celsius}°C")
elif choise==3:
    celsius=float(input("Enter the temperature in Celsius: "))
    kelvin=c_to_k(celsius)
    print(f"{celsius}°C is equal to {kelvin}K")
else:

    print("Invalid choice. Please select a valid option.")  
