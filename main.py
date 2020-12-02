from random import choice
again = 1
total_guesses = 0
correct_guesses = 0
while int(again) > 0:
    inpt = input("Input H for Heads and T for Tails\n")
    otpt = choice(['Heads', 'Tails'])
    print(otpt)
    if (inpt == "T"):
        inpt = "Tails"
    else:
        inpt = "Heads"
    if (inpt == otpt):
        print("You Guessed it Correctly")
        total_guesses += 1
        correct_guesses += 1
    else:
        print("You Guessed it Wrong")
        total_guesses += 1
    print("Total Guesses are " + str(total_guesses) +
          " and correct guesses are " + str(correct_guesses))
    again = input("Input 1 to play again and 0 to stop\n")
