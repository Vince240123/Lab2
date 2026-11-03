import Lab2

def test_find_min_max():

    input_list = [1, 2, 4, 5, 7, 9, 10]
    expected = [1, 10]

    result = Lab2.find_min_max(input_list)

    assert (result == expected)

def test_calc_average():

    input_list = [4, 5, 6]
    expcted = 5

    result = Lab2.calc_average(input_list)

    assert (result == expcted)

def test_calc_median_temperature():

    input_list = [1, 2, 4, 5, 7, 9, 10]
    expected = 5

    result = Lab2.calc_median_temperature(input_list)

    assert (result == expected)
