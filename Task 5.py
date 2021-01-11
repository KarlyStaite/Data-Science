x = int(input("Enter the value of x "))
y = int(input("the value of y "))

print("'a' for addition")
print("'b' for subtraction")
print("'c' for multiplication")
print("'d' for division")
print("'e' for to the power of")
print("'f' for x squared")
print("'g' for y squared")
o = input("Enter the operator ")

if o == "a":
    print(x + y)
elif o == "b":
    print(x - y)
elif o == "c":
    print(x * y)
elif o == "d":
    print(x / y)
elif o == "e":
    print(x ** y)
elif o == "f":
    print(x * x)
elif o == "g":
    print(y * y)
else:
    print("invalid opperator")