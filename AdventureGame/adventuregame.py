name = input("Type youre name: ")
print(f"Welcome {name} to this adventure!")

answer = input("You are stranded in a strange place at night. You are walking along a dirt road, with only the moon illuminating a small sliver of the path beyond. The dirt road suddenly ends in an T-junction where you can go right or left. On the left you see something in the distance that looks like a light or a fire, and on the right the road bends away immediately into an open field, which way do you go? (left) (right) : ").lower()

if answer == "left":
    answer == input("You turn left, towards the supposed light. When you get closer, you hear chanting voices which become louder the closer you get. After getting even closer, you see a campfire with shadowy figures dancing around it. Do you approach them to ask for help or do you wait to see what happens? (ask) (wait) : ").lower()
elif answer == "right":
    print("you chose right")
else:
    print("please provide a valid answer!")