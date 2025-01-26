def main_a(puzzle_input):
    ID_total = 0
    max_per_color = {
        'red': 12,
        'green': 13,
        'blue': 14
    }

    for game in puzzle_input:
        game_text, cube_sets_text = game.split(':')
        game_ID = int(game_text.split(' ')[1])
        
        valid_game = True
        for cube_set in cube_sets_text.split(';'):
            for cube_color in cube_set.split(','):
                amount, color = cube_color.strip().split(' ')
                if int(amount) > max_per_color[color]:
                    valid_game = False

        if valid_game:
            ID_total += game_ID

    return ID_total


def main_b(puzzle_input):
    power_total = 0
    
    for game in puzzle_input:
        min_per_color = {
            'red': 0,
            'green': 0,
            'blue': 0
        }
        game_text, cube_sets_text = game.split(':')
        
        for cube_set in cube_sets_text.split(';'):
            for cube_color in cube_set.split(','):
                amount, color = cube_color.strip().split(' ')
                if int(amount) > min_per_color[color]:
                    min_per_color[color] = int(amount)

        power = 1
        for m in min_per_color.values():
            power *= m
        
        power_total += power

    return power_total


if __name__ == '__main__':
    EXAMPLE_MODE = False
    file_name = 'example.txt' if EXAMPLE_MODE else 'input.txt'

    with open(file_name, 'r') as full_input:
        print(main_a(full_input))
        full_input.seek(0)
        print(main_b(full_input))