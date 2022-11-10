"""
This project is aimed at solving problems
"""
import string


def get_number():
    """
    This function is individual and means tasks to be performed
    """
    number = 70
    return number

# Complete all of the following functions. Currently they all just
# 'pass' rather than explicitly return value, which means that they
# implicitly return None. They all include doctest, which you can
# test by running this file.

# The doctest are just examples. Feel free to add your own doctest.

# ****************************************
# Problem 1
# ****************************************
def get_position(c_h):
    """
    str -> int
    Return position of letter in alphabet. If argument is not a letter function
    should return None.
    >>> get_position('A')
    1
    >>> get_position('z')
    26
    >>> get_position("1")
    >>> get_position('Dj')
    """
    if len(list(c_h)) != 1 :
        return None

    if str(c_h).lower() in [*string.ascii_lowercase] :
        return [*string.ascii_lowercase].index(c_h.lower()) + 1

# ****************************************
# Problem 7
# ****************************************
def convert_to_column(s_convert):
    """
    str -> str
    Convert string to a column of words.
    If argument is not a string function should return None.
    >>> convert_to_column("Revenge is a dish that tastes best when served cold.")
    revenge
    is
    a
    dish
    that
    tastes
    best
    when
    served
    cold
    >>> convert_to_column("Never hate your enemies. It affects your judgment.")
    never
    hate
    your
    enemies
    it
    affects
    your
    judgment
    >>> convert_to_column(2015)
    """
    if isinstance(s_convert, int) :
        return None
    arr = s_convert.split(' ')
    for i in arr :
        if i[-1] in string.ascii_lowercase :
            print(i.lower())
        else :
            buf=[*i]
            buf.pop()
            print("".join(buf).lower())

# ****************************************
# Problem 9
# ****************************************
def replace_with_stars(s_replace):
    """
    str -> str
    Replace symbols in string with stars. If argument is not a string function should
    return None.
    >>> replace_with_stars("Revenge is a dish that tastes best when served cold.")
    '****************************************************'
    >>> replace_with_stars("Never hate your enemies. It affects your judgment.")
    '**************************************************'
    >>> replace_with_stars(2015)
    """
    space = ''
    if isinstance(s_replace, int) :
        return None

    space = len(list(s_replace)) * "*"

    return space

# ****************************************
# Problem 10
# ****************************************
def encrypt_message(s_encrypt):
    """
    str -> str
    Replace all letters in string with next letters in alphabet. If argument is not a string
    function should return None.
    >>> encrypt_message("Revenge is a dish that tastes best when served cold.")
    'Sfwfohf jt b ejti uibu ubtuft cftu xifo tfswfe dpme.'
    >>> encrypt_message("Never hate your enemies. It affects your judgment.")
    'Ofwfs ibuf zpvs fofnjft. Ju bggfdut zpvs kvehnfou.'
    >>> encrypt_message(2015)
    """
    if isinstance(s_encrypt, int or float) :
        return None
    letter = list(string.ascii_letters)
    words = str()
    for i in s_encrypt:
        if i.isalpha():
            words += letter[letter.index(i) + 1]
        elif i == ' ':
            words += ' '
        else:
            words += '.'
    return words

# ****************************************
# Problem 14
# ****************************************
def get_letters(n_get):
    """
    int -> str
    Create and return string of first n letters of an alphabet. If arguments isn't
    positive integer number function should return None.
    >>> get_letters(0)
    >>> get_letters(1)
    'a'
    >>> get_letters(-2015)
    >>> get_letters(5)
    'f'
    """
    arr = string.ascii_lowercase

    if n_get <= 0 and isinstance(n_get, str) :
        return None
    if 2 <= n_get <= 25 :
        return arr[n_get]
    if n_get == 1 :
        return arr[n_get - 1]
    if n_get > 25:
        return None

# ****************************************
# Problem 15
# ****************************************
def find_intersection(s_1_find, s_2_find):
    """
    (str, str) -> str
    Find and returns string of all letters in alphabetic order that
    are present in both strings. If arguments aren't strings function
    should return None.
    >>> find_intersection("ab", "bc")
    'b'
    >>> find_intersection("az", "zb")
    'z'
    >>> find_intersection("sp", 2015)
    >>> find_intersection(2015, "sp")
    """
    if (isinstance(s_1_find, str) and isinstance(s_2_find, int)) or \
    (isinstance(s_1_find, int) and isinstance(s_2_find, str)) :
        return None
    if (isinstance(s_1_find, str) and (isinstance(s_2_find, str))) :
        alphabet = string.ascii_letters

        spell = ''

        for i in alphabet :
            if i in s_1_find and i in s_2_find :
                spell += i
        return spell

# ****************************************
# Problem 16
# ****************************************
def find_union(s_1_find, s_2_find):
    """
    (str, str) -> str
    Find and return string of all letters in alphabetic order that
    are present in either strings. If arguments aren't strings function should
    return None.
    >>> find_union("aaabb", "bbbbccc")
    'abc'
    >>> find_union("aZAbc", "zzYYxp")
    'AYZabcpxz'
    >>> find_union("s", 2015)
    >>> find_union("s", 2015)
    """
    if (isinstance(s_1_find, int) and isinstance(s_2_find, str)) or \
    (isinstance(s_1_find, str) and isinstance(s_2_find, int)) :
        return None

    s_3_find = list(s_1_find) + list(s_2_find)

    s_4_find = []

    for i in s_3_find :
        if i in s_4_find :
            continue
        if i != s_4_find :
            s_4_find += i

    return ''.join(sorted(s_4_find))

# ****************************************
# Problem 18
# ****************************************
def number_of_capital_letters(s_number):
    """
    str -> str
    Find and return number of capital letters in string. If argument isn't string
    function should return None.
    >>> number_of_capital_letters("ArithmeticError")
    2
    >>> number_of_capital_letters("EOFError")
    4
    >>> number_of_capital_letters(1)
    """
    if isinstance(s_number, int):
        return None

    value = 0

    for i in s_number:
        if i in string.ascii_uppercase:
            value += 1
    return value

# ****************************************
# Problem 20
# ****************************************
def polynomial_eval(coefficients, value):
    """
    This function works out polynomials and as a result
    substitutes (int) values and finds (int) answer.
    # f(x) = 2x^3 + 3x^2 + 4, f(4) = 180
    >>> polynomial_eval([2,3,0,4], 4)
    180
    # f(x) = 6, f(42) = 6
    >>> polynomial_eval([6], 42)
    6
    # f(x) = 6x^2 -2x - 20, f(-1) = -12
    >>> polynomial_eval([6,-2,-20], -1)
    -12
    # f(x) = 6x^5-8x^3-8x, f(2) = 112, f(1) = -10, f(0) = 0
    >>> polynomial_eval([6,0,-8,0,-8,0], 2)
    112
    >>> polynomial_eval([6,0,-8,0,-8,0], 1)
    -10
    >>> polynomial_eval([6,0,-8,0,-8,0], 0)
    0
    """
    value_results = 0

    next_kroc = 1

    for i in range(len(coefficients) - 2, -1, -1):
        value_results += coefficients[i] * (value ** next_kroc)
        next_kroc += 1
        value_results += coefficients[-1]

    return value_results

# ****************************************
# Problem 21
# ****************************************
# def polynomials_multiply(polynom_1, polynom_2):
#     """
#     # (2x)*(3x) == 6
#     >>> polynomials_multiply([2], [3])
#     [6]
#     # (2x-4)*(3x+5) == 6x^2 -2x - 20
#     >>> polynomials_multiply([2,-4],[3,5])
#     [6,-2,-20]
#     # (2x^2-4)*(3x^3+2x) == (6x^5-8x^3-8x)
#     >>> polynomials_multiply([2,0,-4],[3,0,2,0])
#     [6,0,-8,0,-8,0]

#     """

# ****************************************
# Problem 25
# ****************************************
# def happy_number(n_happy):
#     """
#     >>> happy_number(32)
#     True
#     >>> happy_number(33)
#     False
#     """
    # n = str(n)
    # arr = [*str(n)]

    # result = 0

    # for i in len(arr) :


# ****************************************
# Problem 27
# ****************************************
def turn_over(n_1, lst):
    """
    Reverse first n items of the list and return it. If n <= 0, return
    the empty list. Do not consume MORE than n items of iterable.
    >>> turn_over(4, ['f', 'o', 'o', 't', 'b', 'a', 'l', 'l'])
    ['t', 'o', 'o', 'f', 'b', 'a', 'l', 'l']
    >>> turn_over(5, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    [5, 4, 3, 2, 1, 6, 7, 8, 9, 10]
    >>> turn_over(10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    >>> turn_over(-5, [])
    []
    >>> turn_over("app", ['f', 'o', 'o', 't', 'b', 'a', 'l', 'l'])
    """

    arr_1 = []
    arr_2 = []

    if isinstance(n_1, str) :
        return None
    if n_1 <= 0 :
        return []
    if n_1 == len(lst) :
        lst = list(lst[::-1])
        return lst
    if n_1 > len(lst) :
        return None
    if isinstance(n_1, str) :
        return None
    if n_1 > len(list(lst)) :
        arr_1 = lst[0:n_1]
        arr_1 = arr_1[::-1]
        arr_2 = lst[n_1:]
        arr_1.extend(arr_2)

    return arr_2

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
