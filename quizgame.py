
print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("Who is the father of python? ")
if answer.lower() == "guido van rossum":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Python was first released in the year? ")
if answer.lower() == "1991":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("The file extension for a python script is? ")
if answer.lower() == ".py":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("To define a function in python ,we use the keyword? ")
if answer.lower() == "def":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")