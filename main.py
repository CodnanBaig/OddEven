import random

print("Let's play a game of Odd Even!\nRules are simple. If you either choose 'Odd' or 'Even'\n"
      "and the sum of yours and the computer's turns is either of them, you win or you lose."
      "For Example: If you chose 'Odd' and your number of choice is\n"
      "9 and the computer chooses 2, you win!\n")


def game():
    your_choice = input("ODD or EVEN? ").lower()

    your_turn = input("Enter a number from 0 - 9: ")

    your_int = int(your_turn)

    computer_turn = random.randint(0, 9)

    total = your_int + computer_turn

    even = False
    odd = False
    if total % 2 == 0:
        even = True
    else:
        odd = True

    if odd == True and your_choice == "odd":
        print(f"You win! computer chose: {computer_turn} and you chose {your_int} and {total} is an odd number")
    elif even == True and your_choice == "even":
        print(f"You win! computer chose: {computer_turn} and you chose {your_int} and {total} is an even number")
    else:
        print(f"You lose! The computer chose: {computer_turn} making the total: {total}")

    play_again = input("Wish to play again? y/n: ").lower()

    if play_again == "y":
        game()
    else:
        print("Thank you")


game()
