from day1.app.solution import parse_rotation, rotate_dial, solve_part_one, count_zeros_in_rotation, solve_part_two

def test_example_from_puzzle():
    example_input = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""
    result = solve_part_one(example_input)
    assert result == 3

def test_parse_rotation():
    direction, distance = parse_rotation("L68")
    assert direction == "L"
    assert distance == 68

    direction, distance = parse_rotation("R48")
    assert direction == "R"
    assert distance == 48

def test_rotate_dial():
    assert rotate_dial(11, "R", 8) == 19
    assert rotate_dial(19, "L", 19) == 0
    assert rotate_dial(5, "L", 10) == 95
    assert rotate_dial(99, "R", 5) == 4

def test_count_zeros_in_rotation():
    assert count_zeros_in_rotation(50, "L", 68) == 1
    assert count_zeros_in_rotation(52, "R", 48) == 1
    assert count_zeros_in_rotation(95, "R", 60) == 1
    assert count_zeros_in_rotation(55, "L", 55) == 1
    assert count_zeros_in_rotation(99, "L", 99) == 1
    assert count_zeros_in_rotation(14, "L", 82) == 1
    assert count_zeros_in_rotation(50, "R", 1000) == 10
    assert count_zeros_in_rotation(10, "R", 5) == 0

def test_example_from_puzzle_part2():
    example_input = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""
    result = solve_part_two(example_input)
    assert result == 6
