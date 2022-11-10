def mask_array(data, mask, mask_value='*', fill_value=-999999):
    counter = 0
    if len(data) < len(mask):
        diff = len(mask) - len(data)
        for i in range(diff):
            data.append(fill_value)
    for m in mask:
        if m and data[counter] != fill_value:
            data[counter] = mask_value
        counter += 1
    print(data)
    return data


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6, 7, 8]
    mask = [False, False, False, True, True, True, False, False, True, True]
    expected = [1, 2, 3, '--', '--', '--', 7, 8, 9999999, 9999999]
    ma_arr = mask_array(data, mask, mask_value='--', fill_value=9999999)
    assert expected == ma_arr, f'Expected mask array is {expected}'