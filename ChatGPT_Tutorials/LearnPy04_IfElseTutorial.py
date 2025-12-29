import random

age = random.randint(1, 100)
if age >= 18:
    print("You are old enough to vote as you are", age, "years old!\n")
else:
    print("You are NOT old enough to vote as you are", age, "years old!\n")

# Else if tutorial
marks = random.randint(1, 100)
if marks >= 80:
    print("You are pass with distinction as you have", marks, "marks out of 100!")
elif marks >= 40:
    print("You are pass as you have", marks, "marks out of 100!")
else:
    print("You are NOT pass as you have", marks, "marks out of 100!")
