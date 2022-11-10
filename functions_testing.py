# Given a list of **N** numbers, use a single list comprehension to produce a new list that only contains those
# values that are:
#
# (a) even numbers, and
#
# (b) from elements in the original list that had even indices
#
# For example, if `list[2]` contains a value that is even, that value should be included in the new list, since it is
# also at an even index (i.e., 2) in the original list.
#
# However, if `list[3]` contains an even number, that number should not be included in the new list since it is at an
# odd index (i.e., 3) in the original list.
numbers = [1, 3, 5, 8, 10, 13, 18, 36, 78]
expected_result = [10, 18, 78]


def get_even_numbers():
    return [number for i, number in enumerate(numbers) if number % 2 == 0 and i % 2 == 0]


if __name__ == "__main__":
    get_even_numbers()
    print(get_even_numbers())
    assert get_even_numbers() == expected_result
