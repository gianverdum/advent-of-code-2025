from shared.utils import read_input

# ===>>> Part one <<<===

def parse_rotation(line):
    direction = line[0]
    distance = int(line[1:])
    return direction, distance

def rotate_dial(position, direction, distance):
    if direction == "R":
        new_position = (position + distance) % 100
    else:
        new_position = (position - distance) % 100
    return new_position

def solve_part_one(input_text):
    position = 50
    count = 0

    for line in input_text.strip().split('\n'):
        direction, distance = parse_rotation(line)
        position = rotate_dial(position, direction, distance)
        if position == 0:
            count += 1
    
    return count

# ===>>> Part two <<<===

def count_zeros_in_rotation(position, direction, distance):
    full_rotations = distance // 100
    remaining = distance % 100

    if direction == "R":
        if remaining > 0 and position + remaining >= 100:
            if position == 0 and position + remaining == 100:
                partial_zeros = 0
            else:
                partial_zeros = 1
        else:
            partial_zeros = 0
    else:
        if remaining > 0 and position - remaining <= 0:
            if position == 0:
                partial_zeros = 0
            else:
                partial_zeros = 1
        else:
            partial_zeros = 0
    
    return full_rotations + partial_zeros

def solve_part_two(input_text):
    position = 50
    count = 0

    for line in input_text.strip().split('\n'):
        direction, distance = parse_rotation(line)
        zeros_in_this_rotation = count_zeros_in_rotation(position, direction, distance)
        count += zeros_in_this_rotation
        position = rotate_dial(position, direction, distance)
    
    return count

def main():
    input_text = read_input(day=1, part=1)
    
    result = solve_part_one(input_text)

    print(f"Part1 Password: {result}")

    input_text = read_input(day=1, part=2)

    result = solve_part_two(input_text)

    print(f"Part2 Password: {result}")

if __name__ == "__main__":
    main()
