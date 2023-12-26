import numpy as np 


def calculate_weather(a, b, c):
    #we use x and y for representing time and temparature
    x = np.linspace(-10, 10, 100)  
    y = wind * x**2 + pressure * x + humidity     #quadratic equation written in terms of whether report  

    return x, y


wind = float(input("Enter coefficient of wind: "))
pressure = float(input("Enter coefficient of pressure: "))
humidity = float(input("Enter coefficient of humidity: "))

x_values, y_values = calculate_weather(wind, pressure, humidity)


print("Generated Weather Data for a Single Set of Inputs:")
for i in range(len(x_values)):
    print(f"x={x_values[i]}, y={y_values[i]}")
