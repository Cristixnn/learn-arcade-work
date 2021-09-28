import random


def main():
    print("Hello cowboy!")
    print(
        "You have stolen a horse and you are on your way to join along with your crew but must cross the Mobi desert.")
    print("The stables want their horseback and have put a bounty on you. Bounty hunters are after you!")
    print("You must go through the Mobi desert and outrun the bounty hunters.\n")

    # defines the variables
    done = False
    miles_traveled = 0
    thirst = 0
    horse_tiredness = 0
    hunters_traveled = -20
    canteen = 3

    while not done:
        print("""A. Drink from your canteen.
B. Ride moderate speed.
C. Ride full speed.
D. rest for the night.
E. Status check.
Q. Quit.\n""")

        user_choice = input("What is your choice? ")

        if user_choice.upper() == "Q":
            print("you have quit the game.")
            done = True

        elif user_choice.upper() == "E":
            print("\nMiles traveled " + str(miles_traveled) + " .")
            print("You have " + str(canteen) + " drinks left.")
            print("The bounty hunters are " + str(miles_traveled - hunters_traveled) + " miles behind you.\n")

        elif user_choice.upper() == "D":
            horse_tiredness = 0
            npc_miles = random.randrange(7, 14)
            hunters_traveled = hunters_traveled + npc_miles
            print("Your horse is rested and healthy!\n")

        elif user_choice.upper() == "C":
            horse_tiredness = horse_tiredness + random.randrange(1, 3)
            miles = random.randrange(10, 20)
            npc_miles = random.randrange(7, 14)
            miles_traveled = miles_traveled + miles
            thirst = thirst + 1
            hunters_traveled = hunters_traveled + npc_miles
            print("\nYour horse breaks into a furious gallop!")
            print("You traveled " + str(miles) + " miles .\n")

        if not done:
            if miles_traveled <= hunters_traveled:
                print("You have been caught! Try again!")
                done = True
            elif miles_traveled - hunters_traveled <= 14:
                print("The hunters are getting close!\n")
        if miles_traveled >= 200:
            print("You made it across the desert! You Won!")
            done = True


main()