# made a simpler version that works with 2 people hope its okay
# But the sacrifice of 1 sentence
import time
player1 = input("What is your name Player 1? ")
player2 = input("What is your name Player 2? ")

print("Hello, " + player1, "You get to go first!")
print("Hello, " + player2, "Wait for your turn!")

print("\n")
time.sleep(1)
print("Start guessing...Sorry, I'm case sensitive")
time.sleep(0.5)
word = "Python is fun sorta"
guesses = ''
turns = 10
while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char),
        else:
            print("_"),
            failed += 1
    if failed == 0:
        print("\nYou won")
        break
    print("\n")
    guess = input("guess a character: ")
    guesses += guess
    if guess not in word:
        turns -= 1
        print("Wrong\n")
        print("You have", + turns, 'guesses left')
        if turns == 0:
            print("You Lose\n")