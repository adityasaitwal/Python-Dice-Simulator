import random
import time

roll_again = "yes"

while roll_again == "Yes" or roll_again == "Y" or roll_again == "yes" or roll_again == "y":
    print("\nRolling the dice...")
    time.sleep(1)

    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print("The values are:")
    print("Dice 1=", dice1)
    print("Dice 2=", dice2)

    if dice1 == dice2:
        print("Great, You rolled a double!")
    else:
        print("Sorry, Keep trying!")

    roll_again = input("\nWant to roll it again? (Y/N) ")