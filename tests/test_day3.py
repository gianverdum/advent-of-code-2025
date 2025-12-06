from day3.app.solution import find_max_joltage, solve_part_one, find_max_joltage_12, solve_part_two

def test_find_max_joltage_single_bank():
    assert find_max_joltage("987654321111111") == 98
    assert find_max_joltage("811111111111119") == 89
    assert find_max_joltage("234234234234278") == 78
    assert find_max_joltage("818181911112111") == 92
    
    assert find_max_joltage("12345") == 45
    assert find_max_joltage("91234") == 94

def test_solve_part_one():
    example_input = """987654321111111
811111111111119
234234234234278
818181911112111"""

    result = solve_part_one(example_input)
    assert result == 357

def test_find_max_joltage_12_batteries():
    assert find_max_joltage_12("987654321111111") == 987654321111
    assert find_max_joltage_12("811111111111119") == 811111111119
    assert find_max_joltage_12("234234234234278") == 434234234278
    assert find_max_joltage_12("818181911112111") == 888911112111

def test_solve_part_two():
    example_input = """987654321111111
811111111111119
234234234234278
818181911112111"""
    
    result = solve_part_two(example_input)
    assert result == 3121910778619