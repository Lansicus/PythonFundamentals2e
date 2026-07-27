from enum import Enum
import random as r


'''Casino Game called Craps. Part 2'''
def roll_dice():
    '''Roll two dice and return their face values as a tuple.'''
    die1 = r.randint(1,6)
    die2 = r.randint(1,6)
    return (die1, die2) # Pack die face values into a tuple.

def display_dice(dice):
    '''Display one roll of the two dice.'''
    die1, die2 = dice #Unpack the tuple into variables die1 and die2.
    print(f"Player rolled {die1} + {die2} = {sum(dice)}")

#Emum type with constraints WON, LOST, AND CONTINUE representing game status.
GameStatus = Enum('GameStatus', ['WON', 'LOST', 'CONTINUE'])
die_values = roll_dice() # First Roll.
display_dice(die_values)

# Determine game status and point, base on first roll.
sum_of_dice = sum(die_values)

match sum_of_dice:
    case 7 | 11: # Win.
        game_status = GameStatus.WON
    case 2 | 3 | 12: # Lose.
        game_status = GameStatus.LOST
    case _: # Default case: remember winning roll.
        game_status = GameStatus.CONTINUE
        my_point = sum_of_dice
        print('Winning point is', my_point)

# Continue rolling until player wins or loses.
while game_status == GameStatus.CONTINUE:
    die_values = roll_dice()
    display_dice(die_values)
    sum_of_dice = sum(die_values)

    if sum_of_dice == my_point: # Win by rolling point.
        game_status = GameStatus.WON
    elif sum_of_dice == 7: # Lose by rolling 7
        game_status = GameStatus.LOST

# Display "wins" or "loses" message
print('Player wins' if game_status == GameStatus.WON else 'Player loses')