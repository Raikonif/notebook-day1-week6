def masked_less(arr, number):
    for i in range(len(arr)):
        if arr[i] < number:
            arr[i] = '--'
    print(arr)
    return arr


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    ma_arr = masked_less(arr, 4)

    assert len(ma_arr) == len(arr), f"Expected len is {len(arr)}"

    expected_data = ['--', '--', '--', 4, 5, 6, 7, 8]
    assert ma_arr == expected_data, f"Expected list is {expected_data}"

    expected_sum = 30
    assert sum([e for e in ma_arr if type(e) is int]) == expected_sum, f'Expected sum is {expected_sum}'
