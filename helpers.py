__author__ = 'katherineford'

import math

def divide_pattern(floss_num_chart, page_size):

    """
    This function should take the pattern and divide it into smaller, print-friendly patterns

    :param floss_num_chart: see floss_num_chart from floss.py; array of arrays
    :param page_size: tuple of how big each divided chart should be for printing; width, height
    :return: The chart, divided for printing.  Divided should be no larger than 60 x 75
    """
    
    floss_size = (float(len(floss_num_chart[0])), float(len(floss_num_chart)))
    chart_size = (int(math.ceil(floss_size[0]/page_size[0])), int(math.ceil(floss_size[1]/page_size[1])))
    num_patterns = chart_size[0] * chart_size[1]
    divided_patterns = []

    #TEST CODE
    print "chart_size = ", chart_size
    print "num_patterns = ", num_patterns

    for printable_row in range(chart_size[0]):
        for printable_col in range(chart_size[1]):
            end_based_on_page_size = (printable_col + 1) * page_size[0] # - 1
            end_based_on_input_size = int(floss_size[0])
            end = min(end_based_on_input_size, end_based_on_page_size)

            stitch_row_selection = (printable_col * page_size[0], end)

            end_based_on_page_size = (printable_row + 1) * page_size[1] # - 1
            end_based_on_input_size = int(floss_size[1])
            end = min(end_based_on_input_size, end_based_on_page_size)

            stitch_col_selection = (printable_row * page_size[1], end)
            smaller_pattern = []

            for stitch_row in range(*stitch_row_selection):
                templist = []
                for stitch_col in range(*stitch_col_selection):
                    templist.append(floss_num_chart[stitch_row][stitch_col])
                smaller_pattern.append(templist)
            divided_patterns.append(smaller_pattern)
    return divided_patterns, chart_size


""" TEST CODE


def _generate_test_input(w, h):
    return [range(w) for _ in range(h)]


def _assert_divide_chart_length(input_size, output_size, expected_length):
    data = _generate_test_input(*input_size)
    divided = divide_pattern(data, output_size)
    assert len(divided) == expected_length


def test_divide_pattern():
    _assert_divide_chart_length((1, 1), (1, 1), 1)
    _assert_divide_chart_length((10, 10), (10, 10), 1)
    _assert_divide_chart_length((10, 10), (5, 5), 4)
    _assert_divide_chart_length((10, 10), (9, 9), 4)
    _assert_divide_chart_length((10, 10), (1, 1), 100)
    _assert_divide_chart_length((10, 100), (1, 100), 10)

"""

def create_test_chart(width, height):
    test_chart = []
    for row in range(height):
        templist = []
        for col in range(width):
            test_num = row * col
            templist.append(test_num)
        test_chart.append(templist)
    return test_chart

chart_tester = create_test_chart(100, 100)
divided_test = divide_pattern(chart_tester, (40, 60))

