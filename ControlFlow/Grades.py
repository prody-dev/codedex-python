
import random

grade = random.randint(0, 100)
print(f"Generated grade: {grade}")

if grade >= 55:
    print("You passed")
else:
    print("You failed")