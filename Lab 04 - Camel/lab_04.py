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
            thirst = thirst + 1
            full_speed = random.randrange(10, 20)
            npc_miles = random.randrange(7, 14)
            miles_traveled = miles_traveled + full_speed
            hunters_traveled = hunters_traveled + npc_miles
            horse_tiredness = horse_tiredness + random.randrange(1, 3)
            print("\nYou traveled " + str(full_speed) + " miles.\n")

        elif user_choice.upper() == "B":
            thirst = thirst + 1
            horse_tiredness = horse_tiredness + 1
            moderate_speed = random.randrange(5, 12)
            npc_miles = random.randrange(7, 14)
            miles_traveled = miles_traveled + moderate_speed
            hunters_traveled = hunters_traveled + npc_miles
            print("You traveled " + str(moderate_speed) + " miles.\n")

        elif user_choice.upper() == "A":
            if canteen > 0:
                canteen = canteen - 1
                thirst = 0
                print("You are hydrated!\n")
            else:
                print("You have no drinks left!\n")

        if not done:
            if miles_traveled <= hunters_traveled:
                print("You have been caught! You lose!")
                done = True
            elif miles_traveled - hunters_traveled <= 15:
                print("The hunters are getting close!\n")
        if miles_traveled >= 200:
            print("You made it across the desert! You Won!")
            done = True
        if thirst >= 6:
            print("You have died of thirst!\n")
            done = True
        elif thirst >= 4:
            print("You are thirsty!")
        if horse_tiredness >= 8:
            print("Your horse is dead! You lost!\n")
        elif horse_tiredness >= 5:
            print("Your horse is tired!")



main()
