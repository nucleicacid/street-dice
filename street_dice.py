import random

money = 50  # User's balance
die = [1, 2, 3, 4, 5, 6]  # Sides of die

playing = False

userInput = input("Play? (y n): ")

if userInput == "y":
    playing = True


while playing:
    print("You have $" + str(money))
    amount = int(input("Amount: $"))  # Bet amount
  
    if 0 < amount <= money:  # Is the bet sufficient?
        rolled = random.choice(die) + random.choice(die)  # Shooter rolls two dice
        print("Shooter rolls the dice >> gets " + str(rolled))

        if rolled in (7, 11):
            money -= amount
            print("Shooter wins $" + str(amount))

        elif rolled in (2, 3, 12):
            money += amount
            print("Shooter loses.")

        elif rolled in (4, 5, 6, 8, 9, 10):
            point = rolled
            print(str(point) + " is the point.")

            while True:  # Runs until shooter rolls point or rolls a 7
                rolled = random.choice(die) + random.choice(die)
                print("Shooter rolls again >> gets " + str(rolled))
                if rolled == point:
                    money -= amount
                    print("Shooter hits the point! Wins $" + str(amount))
                    break
                elif rolled == 7:
                    money += amount
                    print("Shooter rolls a 7! You win!")
                    break
        
        if money > 0:  # Option to play again if player has money
            print("Your balance is: $" + str(money))
            playAgain = input("Play again? (y n): ")
            if playAgain != "y":
                playing = False
        else:
            print("You are broke.")
            playing = False
