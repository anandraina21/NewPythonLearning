import math

print('Hello World!' + ' I am concatenating 2 string values.')
print(3 - 2, "Hello!" + " I am entering different data types in print.", 5 * 4.3, "\n")
print("Add 3+4:", 3 + 4);  # We can put semicolon, but not required.
print("Subtract 8-2.5:", 8 - 2.5)
print("Multiply 4*3:", 4 * 3)
print("Divide 9/4:", 9 / 4)
print("To get whole numbers after division of 9//4:", 9 // 4)
print("Divide 2/2:", 2 / 2)
print("To get whole numbers after division of 2//2:", 2 // 2)
print("To get remainder - modulus operation of 3%2:", 3 % 2)
print("Python uses PEMDAS for operator precedence:")
x = 10 + 3 / 3 * (5 * 2)
print("x =", x)
y = 10 + 3 * 3 ** 3
print("y =", y)
z = (10 + 3) * 3 ** 3
print("z =", z)
print()

print("9 to the power of 2:", 9 ** 2)
print("Natural log (base e) for log(14):", math.log(14))
print("Log with base 5 for log(14,5):", math.log(14, 5))
print("Rounds off to nearest ten as per the given decimal precision for 2.456:", round(2.456, 2))
print("Truncates all decimal for 2.456:", math.trunc(2.456))
print("Rounds of to 2 decimal places using float for 2.456:", '%.2f' % 2.456)
print()

print("abs or Absolute always returns positive number, for 2.9 or -2.9:")
print(abs(2.9))
print(abs(-2.9))
print("math.pi upto 3 decimal places:", round(math.pi, 3))
print("Ceiling value for 2.9:", math.ceil(2.9))
print("Floor value for 2.9:", math.floor(2.9))
print("Factorial value for 5:", math.factorial(5))
print("Sin value for 1.571 radians:", round(math.sin(1.571)))
print("Degree value for 1.571 radians:", round(math.degrees(1.571)))

#################################################
print("\nTruncate upto n decimal places for 2.456:")


def truncate(decimalnumber, decimalplacestotruncate):
    multiplier = 10 ** decimalplacestotruncate
    return math.floor(decimalnumber * multiplier) / multiplier


print(truncate(2.456, 2))
print(truncate(2.456, 1))
