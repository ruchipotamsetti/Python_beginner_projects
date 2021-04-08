import random

#you guess the number 
def guess(x): 
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, guess again. Too low.")
        elif guess > random_number:
            print("Sorry, guess again. Too high.")

    print(f'Yay, congrats. You have guessed the number {random_number} correctly!!')


#computer gusses your number
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # could also be high because low = high
        feedback = input(f'Is {guess} too high(H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Yay! The computer guessed your number, {guess}, correctly!') 

again = 'y'
while again == 'y':
    print('Choose one option: (1) Guess the number (2) Computer guesses your number ')
    choice = int(input('Your choice: '))
    print()
    if choice == 1:
        guess(100)
    else: 
        computer_guess(100)
    print()
    again = input('Do you want to play again? Yes(Y) or No(N): ').lower()
