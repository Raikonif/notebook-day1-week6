# posibilities = [
#     ('scissors', 'cuts', 'paper'),
#     ('paper', 'covers', 'rock'),
#     ('rock', 'crushes', 'lizard'),
#     ('lizard', 'poison', 'spock'),
#     ('spock', 'smashes', 'scissors'),
#     ('scissors', 'decapitate', 'lizard'),
#     ('lizard', 'eats', 'paper'),
#     ('paper', 'disproves', 'spock'),
#     ('spock', 'vaporizes', 'rock'),
#     ('rock', 'crushes', 'scissors'),
# ]

options = ['rock', 'paper', 'scissors', 'lizard', 'spock']

posibilities = {
    'cuts': ['scissors', 'paper'],
    'covers': ['paper', 'rock'],
    'crushes': ['rock', 'lizard'],
    'poison': ['lizard', 'spock'],
    'smashes': ['spock', 'scissors'],
    'decapitate': ['scissors', 'lizard'],
    'eats': ['lizard', 'paper'],
    'disproves': ['paper', 'spock'],
    'vaporizes': ['spock', 'rock'],
    'crush': ['scissors', 'rock'],
}

v_options = ['cuts', 'covers', 'crushes', 'posion', 'smashes', 'decapitate', 'eats', 'disproves', 'vaporizes',
             'crushes']


def game(player1_input, player2_input):
    valid_p1 = False
    valid_p2 = False
    if player1_input == {} or player2_input == {}:
        print("Please provide valid data")
        return None
    if isinstance(player1_input, dict):
        print("Player 1 is a dict")
        player1_input = player1_input['option']
    if isinstance(player2_input, dict):
        print("Player 2 is a dict")
        player2_input = player2_input['option']

    print("Welcome to the game of Rock, Paper, Scissors, Lizard, Spock!")
    print("""Please select your choice:
    1. Rock
    2. Spock
    3. Paper
    4. Lizard
    5. Scissors""")
    for op in options:
        if player1_input == op:
            valid_p2 = True
        if player2_input == op:
            valid_p1 = True
    print("Player 1 selected: ", player1_input)
    print("Player 2 selected: ", player2_input)
    if valid_p1 and valid_p2:
        for key, value in posibilities.items():
            # print(key, value)
            if player1_input == player2_input:
                print("Player1 and Player2 are even!")
                return 'Player1 and Player2 are even!'
            elif player1_input == value[0] and player2_input == value[1]:
                join_string = f" {key} ".join(value).lower()
                print(join_string, ' Player 1 wins!')
                return join_string
            elif player2_input == value[0] and player1_input == value[1]:
                join_string = f" {key} ".join(value).lower()
                print(join_string, ' Player 2 wins!')
                return join_string
    else:
        print("Invalid input")
        return None


if __name__ == "__main__":
    game({'id': 1, 'option': 'scissors'}, {'id': 2, 'option': 'scissors'})
    # assert game('paper', 'spock') == 'paper disproves spock', 'Expected value is `paper disproves spock`'
    # assert game('spock', 'rock') == 'spock vaporizes rock', 'Expected value is `spock vaporizes rock`'
    # assert game('rock', 'scissors') == 'rock crush scissors', 'Expected value is `rock crush scissors`'
    assert game(
        {'id': 1, 'option': 'scissors'},
        {'id': 2,
         'option': 'scissors'}) == 'Player1 and Player2 are even!', 'Expected value is `Player1 and Player2 are even!`'
    assert game({}, {}) is None, 'Expected value is `None`'