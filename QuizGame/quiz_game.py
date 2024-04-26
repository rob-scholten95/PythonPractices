print("Welcome to my computer quiz!")

playing = input("Would you like to start playing? ").lower()

if playing != "yes":
    quit()

    
print("Okay! Lets play!")
score = 0

answer = input("What does CPU stand for? ").lower()

if answer == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

    
answer = input("What does GPU stand for? ").lower()

if answer == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")



answer = input("What does PSU stand for? ").lower()

if answer == "power supply unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("What does RAM stand for? ").lower()

if answer == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("you got " + str((score/4) * 100) +"% of questions correct.")
