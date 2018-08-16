
def play():
    #inventory definition
    inventory = ['Dagger', 'Gold(5)', 'Crusty Bread']

    #game start
    print("Escape from Cave Terror!")
    action_input = get_player_command()
    if action_input in ['n', 'N']:
        print("Go North!")
    elif action_input in ['s', 'S']:
        print('Go South!')
    elif action_input in ['e', 'E']:
        print('Go East!')
    elif action_input in ['w', 'W']:
        print('Go West!')
    elif action_input in ['i', 'I']:
        print("Inventory:")
        print(inventory)
    else:
        print("invalid action!")

def get_player_command():
    return raw_input('Action: ')

play()
