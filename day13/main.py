def main_a(puzzle_input):
    total = 0

    for pattern in puzzle_input.read().split('\n\n'):
        p = pattern.splitlines()
        # Check for horizontal reflections
        potential_axes = find_potential_reflection_axes(p)
            
        if potential_axes:
            total += potential_axes[0]
        else:
            tp = []
            for i in range(len(p[0])):
                tp.append([row[i] for row in p])

            potential_axes = find_potential_reflection_axes(tp)
            total += 100 * potential_axes[0]

    return total


def find_potential_reflection_axes(p):
    # Check for horizontal reflections
    potential_axes = list(range(1, len(p[0])))

    for row in p:
        new_axes = []
        for ax in potential_axes:
            l, r = row[0:ax], row[ax:]
            length = min(len(l), len(r))
            cl, cr = l[(len(l) - length):], r[0:length]
            if cl == cr[::-1]:
                new_axes.append(ax)
        potential_axes = new_axes
    
    return potential_axes


def main_b(puzzle_input):
    total = 0

    return 0


if __name__ == '__main__':
    EXAMPLE_MODE = False
    file_name = 'example.txt' if EXAMPLE_MODE else 'input.txt'

    with open(file_name, 'r') as full_input:
        print(main_a(full_input))
        full_input.seek(0)
        print(main_b(full_input))