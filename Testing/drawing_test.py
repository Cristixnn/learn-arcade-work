done = False
while not done:
    quit = input("Do you want to quit? ")
    if quit == "y":
        done = True

    attack = input("Does your elf attack the dragon? ")
    if attack == "y":
        print("Bad choice, you died.")
    elif attack == "n":
        print(" good bro")
        done = True
