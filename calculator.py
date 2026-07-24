num1 = int(input("enter a value"))
num2 = int(input("enter b value"))
addition = num1+num2
subtraction = num1-num2
multiplication = num1*num2
division = num1/num2

operation = input()
if operation == "addition":
    print(f"addition is:{addition}")
elif operation == "subtraction":
        print(f"subtraction is:{subtraction}")
elif operation == "multiplication":
          print(f"mul is:{multiplication}")
elif operation == "division":
    print(f"div is:{division}")
else:
    print("not a valid operation")