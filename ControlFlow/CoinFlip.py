
import random

num = random.randint(0, 1)
print(f"Generated number: {num}")

if num > 0.5:
    print("Heads")
else:
    print("Tails")