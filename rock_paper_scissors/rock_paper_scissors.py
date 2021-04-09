import random

def play():
    user = input("Choose one: 'r' for rock, 'p' for paper, 's' for scissors\nYour choice: ")
    computer = random.choice(['r', 'p', 's'])
    print(f"Computer's choice: {computer}")

    if user == computer:
        return "It's a tie!\n" 

    if is_win(user, computer):
        return "You won!\n"

    return "You lost!\n"


# r > s, s > p, p > r  
def is_win(player, opponent):

    # return true if player wins
    if (player == 'r' and opponent == 'scissor') or (player == 's' and opponent == 'p') or \
    (player == 'p' and  opponent == 'r'):
        return True

count = int(input("How many times do you want to play? "))
while count != 0: 
    print(play())
    count -= 1
