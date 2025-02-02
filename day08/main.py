def greatest_common_factor(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def least_common_multiple(number_list):
    if len(number_list) == 2:
        return (number_list[0] * number_list[1]) // greatest_common_factor(number_list[0], number_list[1])
    
    return least_common_multiple([number_list[0], least_common_multiple(number_list[1:])])


def main_a(puzzle_input):
    instructions = puzzle_input.readline().strip()
    puzzle_input.readline()

    node_dict = {}
    for line in puzzle_input:
        node, paths = line.strip().split(' = ')
        node_dict[node] = tuple(paths[1:-1].split(', '))
    
    steps_taken = 0
    current_node = 'AAA'
    goal_node = 'ZZZ'

    while current_node != goal_node:
        instruction = 0 if instructions[steps_taken % len(instructions)] == 'L' else 1
        current_node = node_dict[current_node][instruction]
        steps_taken += 1

    return steps_taken


def main_b(puzzle_input):
    instructions = puzzle_input.readline().strip()
    puzzle_input.readline()

    current_nodes = []
    goal_nodes = []
    node_dict = {}
    for line in puzzle_input:
        node, paths = line.strip().split(' = ')
        node_dict[node] = tuple(paths[1:-1].split(', '))

        if node[-1] == 'A':
            current_nodes.append(node)
        if node[-1] == 'Z':
            goal_nodes.append(node)

    goal_nodes = set(goal_nodes)
    step_counts = []
    
    for node in current_nodes:
        current_node = node
        steps_taken = 0
        while current_node not in goal_nodes:
            instruction = 0 if instructions[steps_taken % len(instructions)] == 'L' else 1
            current_node = node_dict[current_node][instruction]
            steps_taken += 1
        step_counts.append(steps_taken)

    return least_common_multiple(step_counts)


if __name__ == '__main__':
    EXAMPLE_MODE = False
    file_name = 'example.txt' if EXAMPLE_MODE else 'input.txt'

    with open(file_name, 'r') as full_input:
        #print(main_a(full_input))
        full_input.seek(0)
        print(main_b(full_input))