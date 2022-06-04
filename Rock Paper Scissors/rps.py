import random

def play():
    user = input("Use 'r' for rock, 'p' for paper and 's' for scissors.\n") #Linebreak added
    computer = random.choice(['r', 'p', 's']) #List, computer's choice

    if user == computer:
        return "It's a tie!" #Tie initialized
    if is_win(user, computer):
        return "You won!"
    return "You lost!" #Based on W/L




def is_win(player, opponent): #Returns True if player wins
    if(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

print(play()) #Output