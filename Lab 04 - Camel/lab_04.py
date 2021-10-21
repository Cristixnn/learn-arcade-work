import random

done = False
thirst = 0


def main():
    print("Hello cowboy!")
    print("You have stolen a horse and you are on your way to join along your crew but must cross the Mobi desert."
          "\nThe stables wants there horse back and have put a bounty on you. Bounty hunters are after you!"
          "\nYou must go through the Mobi desert and outrun the bounty hunters.")

    if not done:
        print("A. Drink water from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead of full speed")
    print("D. Stop and rest.")
    print("E. Status check.")
    print("Q. Quit")

    Answer = input("What is your choice?")
    if Answer < "A":
        print(" You are hydrated!")


main()
