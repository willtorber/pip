import random

# Define constants for the options
ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'
LIZARD = 'lizard'
SPOCK = 'spock'
OPTIONS = (ROCK, PAPER, SCISSORS, LIZARD, SPOCK)
WIN_CONDITION = 2

# Define the winning rules in a dictionary for cleaner access
WIN_RULES = {
    SCISSORS: [PAPER, LIZARD],
    PAPER: [ROCK, SPOCK],
    ROCK: [LIZARD, SCISSORS],
    LIZARD: [SPOCK, PAPER],
    SPOCK: [SCISSORS, ROCK]
}

def choose_options():
    """
    Prompts the user for their choice and validates the input.
    The computer's choice is selected randomly.
    """
    user_option = input(f'{", ".join(OPTIONS)} => ').lower()

    if user_option not in OPTIONS:
        print('That is not a valid option.')
        return None, None

    computer_option = random.choice(OPTIONS)
    print(f'User option => {user_option}')
    print(f'Computer option => {computer_option}')
    return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
    """
    Determines the winner of the round based on the new rules and updates the win counters.
    """
    if user_option == computer_option:
        print("It's a tie!")
    elif computer_option in WIN_RULES[user_option]:
        print(f'{user_option.capitalize()} wins against {computer_option}. User wins!')
        user_wins += 1
    else:
        print(f'{computer_option.capitalize()} wins against {user_option}. Computer wins!')
        computer_wins += 1
    return user_wins, computer_wins

def run_game():
    """
    Executes the main game loop.
    """
    computer_wins = 0
    user_wins = 0
    rounds = 1

    while True:
        print('\n' + '*' * 10)
        print('ROUND', rounds)
        print('*' * 10)
        print(f'Computer wins: {computer_wins}')
        print(f'User wins: {user_wins}')

        user_option, computer_option = choose_options()
        if user_option is None:
            continue

        user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)
        
        rounds += 1

        if computer_wins == WIN_CONDITION:
            print('\n' + '*' * 15)
            print('The final winner is the computer!')
            print('*' * 15)
            break

        if user_wins == WIN_CONDITION:
            print('\n' + '*' * 15)
            print('The final winner is the user!')
            print('*' * 15)
            break

if __name__ == '__main__':
    run_game()