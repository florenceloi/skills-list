"""Skills Assessment: Lists

Edit the function bodies until all of the doctests pass when you run this file.
"""


def all_odd(number_list):
    """Return a list of only the odd numbers in the input list.

        >>> all_odd([1, 2, 7, -5])
        [1, 7, -5]

        >>> all_odd([2, -6, 8])
        []

    """

    odd_numbers = [number for number in number_list if number % 2 == 1]

    return odd_numbers


def all_even(number_list):
    """Return a list of only the even numbers in the input list.

        >>> all_even([2, 6, -1, -2])
        [2, 6, -2]

        >>> all_even([-1, 3, 5])
        []

    """

    even_numbers = [number for number in number_list if number % 2 == 0]

    return even_numbers


def print_indexes(my_list):
    """Print the index of each item in the input_list, followed by the item itself.

    Do this without using a counting variable---that is, don't do something
    like this:

        count = 0
        for item in list:
            print count
            count = count + 1

    Output should look like this:

        >>> print_indexes(["Toyota", "Jeep", "Volvo"])
        0 Toyota
        1 Jeep
        2 Volvo

    """

    for i in range(len(my_list)):
        print i, my_list[i]


def long_words(word_list):
    """Return all words in input list that are longer than 4 characters.

        >>> long_words(["hello", "hey", "spam", "spam", "bacon", "bacon"])
        ['hello', 'bacon', 'bacon']

        >>> long_words(["all", "are", "tiny"])
        []

    """

    long_words = []

    for item in word_list:
        length = 0

        for character in item:
            length += 1

        if length > 4:
            long_words.append(item)

    return long_words


def smallest_int(number_list):
    """Find the smallest integer in a list of integers and return it.

    DO NOT USE the built-in function `min`!

        >>> smallest_int([-5, 2, -5, 7])
        -5


        >>> smallest_int([3, 7, 2, 8, 4])
        2

    If the input list is empty, return None:


        >>> smallest_int([]) is None
        True

    """

    if not number_list:
        return None

    else:
        min_integer = number_list[0]

        for number in number_list:
            if number < min_integer:
                min_integer = number

        return min_integer


def largest_int(number_list):
    """Find the largest integer in a list of integers and return it.

    DO NOT USE the built-in function `max`!

        >>> largest_int([-5, 2, -5, 7])
        7

        >>> largest_int([3, 7, 2, 8, 4])
        8

    If the input list is empty, return None:

        >>> largest_int([]) is None
        True

    """

    if not number_list:
        return None

    max_integer = number_list[0]

    for number in number_list:
        if number > max_integer:
            max_integer = number

    return max_integer


def halvesies(number_list):
    """Return list of numbers from input list, each divided by two.

        >>> halvesies([2, 6, -2])
        [1.0, 3.0, -1.0]

    If any of the numbers are odd, make sure you don't round off the half:

        >>> halvesies([1, 5])
        [0.5, 2.5]

    """

    halvesies = []

    for number in number_list:
        number_halved = number / 2.0
        halvesies.append(number_halved)

    return halvesies


def word_lengths(word_list):
    """Return the length of words in the input list.

        >>> word_lengths(["hello", "hey", "hello", "spam"])
        [5, 3, 5, 4]

    """

    word_lengths = []

    for item in word_list:
        length = 0

        for character in item:
            length += 1

        word_lengths.append(length)

    return word_lengths


def sum_numbers(number_list):
    """Return the sum of all of the numbers in the list.

    Python has a built-in function, `sum()`, which already does this -- but for
    this exercise, you should not use it.

        >>> sum_numbers([1, 2, 3, 10])
        16

    Any empty list should return the sum of zero:

        >>> sum_numbers([])
        0

    """

    if not number_list:
        return 0

    else:
        summing = number_list[0]

        if number_list[1]:
            for number in number_list[1:]:
                summing += number

        return summing


def mult_numbers(number_list):
    """Return product (result of multiplication) of the numbers in the list.

        >>> mult_numbers([1, 2, 3])
        6

    Obviously, if there is a zero in the input, the product will be zero:

        >>> mult_numbers([10, 20, 0, 50])
        0

    As explained at http://en.wikipedia.org/wiki/Empty_product, if the list is
    empty, the product should be 1:

        >>> mult_numbers([])
        1

    """

    if not number_list:
        return 1

    else:
        multiplying = number_list[0]

        if number_list[1]:
            for number in number_list[1:]:
                multiplying *= number

        return multiplying


def join_strings(word_list):
    """Return a string of all input strings joined together.

    Python has a built-in method on lists, `join`---but for this exercise, you
    should not use it.

        >>> join_strings(["spam", "spam", "bacon", "balloonicorn"])
        'spamspambaconballoonicorn'

    For an empty list, you should return an empty string:

        >>> join_strings([])
        ''

    """

    if not word_list:
        return ""

    else:
        joined_strings = word_list[0]

        if word_list[1]:
            for item in word_list[1:]:
                joined_strings += item

        return joined_strings


def average(number_list):
    """Return the average (mean) of the list of numbers given.

        >>> average([2, 12, 3])
        5.666666666666667

    There is no defined answer if the list given is empty. It's fine if
    this raises an error when given an empty list.
    """

    sum_list = 0.0
    length_list = 0.0

    for number in number_list:
        sum_list += number
        length_list += 1.0

    average = sum_list / length_list

    return average


def join_strings_with_comma(list_of_words):
    """Return ['list', 'of', 'words'] like "list, of, words".

        >>> join_strings_with_comma(["Labrador", "Poodle", "French Bulldog"])
        'Labrador, Poodle, French Bulldog'

    If there's only one thing in the list, it should return just that
    thing, of course:

        >>> join_strings_with_comma(["Pretzel"])
        'Pretzel'

    """

    try:
        joined_strings_with_comma = list_of_words[0]

        for item in list_of_words[1:]:
            joined_strings_with_comma += ", "
            joined_strings_with_comma += item

        return joined_strings_with_comma

    except IndexError:
        return list_of_words[0]


#############################################################################
# END OF ASSIGNMENT: You can ignore everything below

if __name__ == "__main__":
    import doctest
    print
    result = doctest.testmod()
    if not result.failed:
        print "*** %s TESTS PASSED. GOOD WORK!" % result.attempted
    print
