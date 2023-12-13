""" Module with methods to help with generation of Hypercube.
"""


def _check_0s_1s_count(binary: str):
    cont_0 = 0
    cont_1 = 0
    for i in range(len(binary)):
        if binary[i] == '0':
            cont_0 += 1
        elif binary[i] == '1':
            cont_1 += 1

    return {
        'zeros': cont_0,
        'ones': cont_1
    }


def _check_binary_difference(bin1: str, bin2: str):     # NOK Not worked
    """ It doesn't worked properly.
    """
    bin1_count = _check_0s_1s_count(bin1)
    bin2_count = _check_0s_1s_count(bin2)

    if (
        # bin1_count['zeros'] != bin2_count['ones'] and
        # bin1_count['ones'] != bin2_count['zeros'] and
        # bin1_count['ones'] != bin2_count['ones'] and
        # bin1_count['zeros'] != bin2_count['zeros'] and
        (abs(bin1_count['zeros'] - bin2_count['zeros'])) == 1 and
        (abs(bin1_count['ones'] - bin2_count['ones'])) == 1


    ):
        has_difference_in_one_digit = True
    else:
        has_difference_in_one_digit = False

    # has_difference_in_one_digit = (bin1_count != bin2_count)

    print(f'{bin1}: {bin1_count} \n{bin2}: {bin2_count}')
    print(f'Result: {has_difference_in_one_digit}')
    return has_difference_in_one_digit


def _check_binary_difference_v2(bin1: str, bin2: str):  # OK Worked
    """ Checks difference between two binary strings.
        If the strings are different in one digit, returns `True`.
    """

    bin_size = len(bin1) if len(bin1) == len(bin2) else None

    differences = 0
    if bin_size:
        for i in range(bin_size):
            if bin1[i] != bin2[i]:
                differences += 1

    if differences == 1:
        has_difference_in_one_digit = True
    else:
        has_difference_in_one_digit = False

    # print(f'{bin1} | {bin2}: {differences} diff')
    # print(f'Result: {has_difference_in_one_digit}\n')
    return has_difference_in_one_digit
