def convert_to_miles(kilometers):
    miles = kilometers * 0.621371
    return round(miles, 4)

print(convert_to_miles(1))
print(convert_to_miles(5))
print(convert_to_miles(10))