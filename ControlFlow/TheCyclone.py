

# height requirement is 137 and the cost is 10 credits
print("Welcome to the Cyclone Height Calculator!")
height = int(input("Enter the height of the cyclone: "))
credits = int(input("Enter the number of credits you have: "))

if height >= 137 and credits >= 10:
    print("Enjoy the ride!")
elif height < 137 and credits >= 10:
    print("You are not tall enough to ride.")
elif height >= 137 and credits < 10:
    print("You dont have enough credits.")
else:
    print("You do not meet the height or credit requirements for the ride.")