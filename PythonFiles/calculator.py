import math

print("Basic Calculator Using Arithmetic Operators")
Num1 = float(input("Enter a number: "))
Operator = input("Enter an operator: ")
Num2 = float(input("Enter second number: "))

if (Operator == "+"):
    print("Answer: ", Num1 + Num2)

elif (Operator == "-"):

    print("Answer: ", Num1 - Num2)

elif (Operator == "*"):

    print("Answer: ", Num1 * Num2)

elif (Operator == "/"):
    if Num2 != 0:
        print("Answer: ", Num1 / Num2)
    else:
        print("Error: Zero cannot be used to divide!")

elif (Operator == "%"):

    print("Answer: ", Num1 % Num2)
elif (Operator == "//"):

    print("Answer: ", Num1 // Num2)
elif (Operator == "sqrt()"):

    print("Answer: ", math.sqrt(Num1))
elif (Operator == "pow()"):

    print("Answer: ", math.pow(Num1, Num2))

else:
    print("Invalid Operator")