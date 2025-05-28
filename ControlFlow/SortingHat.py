

gryffindor = ravenclaw = hufflepuff = slytherin = 0

q1 = int(input(
    "Q1) Do you like Dawn or Dusk?\n"
    "    1) Dawn\n"
    "    2) Dusk\n"
    "Tu elección: "
))
if q1 == 1:
    gryffindor += 1
    ravenclaw += 1
elif q1 == 2:
    hufflepuff += 1
    slytherin += 1
else:
    print("Wrong input.")


q2 = int(input(
    "\nQ2) When I'm dead, I want people to remember me as:\n"
    "    1) The Good\n"
    "    2) The Great\n"
    "    3) The Wise\n"
    "    4) The Bold\n"
    "Tu elección: "
))
if q2 == 1:
    hufflepuff += 2
elif q2 == 2:
    slytherin += 2
elif q2 == 3:
    ravenclaw += 2
elif q2 == 4:
    gryffindor += 2
else:
    print("Wrong input.")


q3 = int(input(
    "\nQ3) Which kind of instrument most pleases your ear?\n"
    "    1) The violin\n"
    "    2) The trumpet\n"
    "    3) The piano\n"
    "    4) The drum\n"
    "Tu elección: "
))
if q3 == 1:
    slytherin += 4
elif q3 == 2:
    hufflepuff += 4
elif q3 == 3:
    ravenclaw += 4
elif q3 == 4:
    gryffindor += 4
else:
    print("Wrong input.")
    
print("\n Scores:")
print(f"Gryffindor: {gryffindor}")
print(f"Hufflepuff: {hufflepuff}")
print(f"Ravenclaw: {ravenclaw}")
print(f"Slytherin: {slytherin}")