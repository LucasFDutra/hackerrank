from hackerrank.Save_The_Prisioner import main


def test_chair_number_between_one_and_number_or_prisoners():
    # 1 < chair_number_to_begin < number_of_prisoners

    # number_of_prisoners = number_of_sweets
    number_of_prisoners = 4
    number_of_sweets = 4
    chair_number_to_begin = 2
    assert main.main(number_of_prisoners, number_of_sweets, chair_number_to_begin) == 1

    # number_of_prisoners > number_of_sweets
    number_of_prisoners = 5
    number_of_sweets = 4
    chair_number_to_begin = 2
    assert main.main(number_of_prisoners, number_of_sweets, chair_number_to_begin) == 5

    # number_of_prisoners < number_of_sweets
    number_of_prisoners = 3
    number_of_sweets = 4
    chair_number_to_begin = 2
    assert main.main(number_of_prisoners, number_of_sweets, chair_number_to_begin) == 2

    # number_of_prisoners = 1/n*number_of_sweets
    number_of_prisoners = 4
    number_of_sweets = 8
    chair_number_to_begin = 2
    assert main.main(number_of_prisoners, number_of_sweets, chair_number_to_begin) == 1


def test_chair_number_begin_in_one():
    # chair_number_to_begin = 1

    # number_of_prisoners = number_of_sweets
    number_of_prisoners = 4
    number_of_sweets = 4
    chair_number_to_begin = 1
    assert main.main(number_of_prisoners, number_of_sweets, chair_number_to_begin) == 4

    # number_of_prisoners > number_of_sweets
    number_of_prisoners = 5
    number_of_sweets = 4
    chair_number_to_begin = 1
    assert main.main(number_of_prisoners, number_of_sweets, chair_number_to_begin) == 4

    # number_of_prisoners < number_of_sweets
    number_of_prisoners = 3
    number_of_sweets = 4
    chair_number_to_begin = 1
    assert main.main(number_of_prisoners, number_of_sweets, chair_number_to_begin) == 1

    # number_of_prisoners = 1/n*number_of_sweets
    number_of_prisoners = 4
    number_of_sweets = 8
    chair_number_to_begin = 1
    assert main.main(number_of_prisoners, number_of_sweets, chair_number_to_begin) == 4


def test_chair_number_is_equal_to_the_prisoners_number():
    # chair_number_to_begin = number_of_prisoners

    # number_of_prisoners = number_of_sweets
    number_of_prisoners = 4
    number_of_sweets = 4
    chair_number_to_begin = 4
    assert main.main(number_of_prisoners, number_of_sweets, chair_number_to_begin) == 3

    # number_of_prisoners > number_of_sweets
    number_of_prisoners = 5
    number_of_sweets = 4
    chair_number_to_begin = 5
    assert main.main(number_of_prisoners, number_of_sweets, chair_number_to_begin) == 3

    # number_of_prisoners < number_of_sweets
    number_of_prisoners = 3
    number_of_sweets = 4
    chair_number_to_begin = 3
    assert main.main(number_of_prisoners, number_of_sweets, chair_number_to_begin) == 3

    # number_of_prisoners = 1/n*number_of_sweets
    number_of_prisoners = 4
    number_of_sweets = 8
    chair_number_to_begin = 4
    assert main.main(number_of_prisoners, number_of_sweets, chair_number_to_begin) == 3