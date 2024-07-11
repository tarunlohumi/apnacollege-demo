number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))

if(number1>=number2 and number1>=number3):
    print("First number is the biggest", number1)
elif(number2>=number1 and number2>=number3):
    print("Second number is the biggest",number2)
else:
    print("Third number is the biggest",number3)

