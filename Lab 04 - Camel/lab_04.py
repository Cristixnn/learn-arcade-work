# allows computer to roll dice
import random


# main function.
def main():
    print("Hello cowboy!")
    print(
        "You have stolen a horse and you are on your way to join along with your crew but must cross the Mobi desert.")
    print("The stables want their horseback and have put a bounty on you. Bounty hunters are after you!")
    print("You must go through the Mobi desert and outrun the bounty hunters.\n")

    # defines the variables.
    done = False
    miles_traveled = 0
    thirst = 0
    horse_tiredness = 0
    hunters_traveled = -20
    canteen = 3

    # user options.
    while not done:
        print("""A. Drink from your canteen.
B. Ride moderate speed.
C. Ride full speed.
D. Rest for the night.
E. Status check.
Q. Quit.""")

        # users input.
        user_choice = input("What is your choice? ")

        # quits the game with "Q".
        if user_choice.upper() == "Q":
            print("you have quit the game.")
            done = True

        # lets user check status with "E".
        elif user_choice.upper() == "E":
            print("\nMiles traveled " + str(miles_traveled) + ".")
            print("You have " + str(canteen) + " drinks left.")
            print("The bounty hunters are " + str(miles_traveled - hunters_traveled) + " miles behind you.\n")

        # restarts horse_tiredness to 0 with "D".
        elif user_choice.upper() == "D":
            horse_tiredness = 0
            npc_miles = random.randrange(7, 14)
            hunters_traveled = hunters_traveled + npc_miles
            print("\nYour horse is rested and healthy!\n")

        # allows user to go full speed with "C".
        elif user_choice.upper() == "C":
            thirst = thirst + 1
            full_speed = random.randrange(10, 20)
            npc_miles = random.randrange(7, 14)
            miles_traveled = miles_traveled + full_speed
            hunters_traveled = hunters_traveled + npc_miles
            horse_tiredness = horse_tiredness + random.randrange(1, 3)

            # chance of finding an oasis while moving with "B".
            if random.randrange(21) == 0:
                print("\nYou found an oasis!")
                canteen = 3
                thirst = 0
                horse_tiredness = 0

            # amount of miles you traveled that specific turn.
            print("\nYou traveled " + str(full_speed) + " miles.\n")

        # user moves moderate speed with "B"
        elif user_choice.upper() == "B":
            thirst = thirst + 1
            horse_tiredness = horse_tiredness + 1
            moderate_speed = random.randrange(5, 12)
            npc_miles = random.randrange(7, 14)
            miles_traveled = miles_traveled + moderate_speed
            hunters_traveled = hunters_traveled + npc_miles

            # chance of finding an oasis while moving with "B".
            if random.randrange(21) == 0:
                print("\nYou found an oasis!")
                canteen = 3
                thirst = 0
                horse_tiredness = 0

            # amount of miles you traveled that specific turn
            print("\nYou traveled " + str(moderate_speed) + " miles.\n")

        # lets user drink water if they have water in canteen with "A"
        elif user_choice.upper() == "A":
            npc_miles = random.randrange(7, 14)
            hunters_traveled = hunters_traveled + npc_miles
            # if canteen is not 0 user can drink.
            if canteen > 0:
                canteen = canteen - 1
                thirst = 0
                print("\nYou are hydrated!\n")
            # if user has 0 drinks user cannot drink.
            else:
                print("\nYou have no drinks left!\n")

        # if game is ongoing, loop will continue
        if not done:

            # win game once hitting more or equal to 200.
            if miles_traveled >= 200:
                print("You made it across the desert! You Won!")
                done = True

        if not done:
            # lose game once hunter caught up to you.
            if miles_traveled <= hunters_traveled:
                print("You have been caught! You lose!")
                done = True

        if not done:
            # once user gets too thirsty they lose.
            if thirst >= 6:
                print("You have died of thirst!\n")
                done = True
        if not done:
            # gives user warning about thirst.
            if thirst >= 4:
                print("You are thirsty!\n")

        if not done:
            # horse dies once it reaches 8 tiredness.
            if horse_tiredness >= 8:
                print("Your horse is dead! You lost!\n")
                done = True
        if not done:
            # gives user warning about horse tiredness.
            if horse_tiredness >= 5:
                print("Your horse is tired!\n")

        if not done:
            # gives user warning hunters are close.
            if miles_traveled - hunters_traveled <= 15:
                print("The hunters are getting close!\n")


main()
