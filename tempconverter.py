x = int(input("Enter temperature: "))
y = input("Enter Units (k or c or f): ")
c = "c"
k = "k"
f = "f"
if y == c:
    k = float(x + 273)
    f = float((x*9/5)+32)
    print(f"Temperature in Kelvin: {k} \nTemperature in Fahrenheit: {f}")
elif y == k:
     c = float(x-273)
     f = float(x*1.8-459.67)
     print(f"Temperature in Celsius: {c} \nTemperature in Fahrenheit: {f}")
elif y == f:
    c = float((x-32)*5/9)
    k = float((x+459.67)*5/9)
    print(f"Temperature in Celsius: {c} \nTemperature in Kelvin: {k}")
else:
      print()