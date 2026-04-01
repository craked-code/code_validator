BENCHMARK_FUNCTIONS = {}

# Function 1: Arithmetic with zero-check guard
# Bug: checks b == 1 instead of b == 0
BENCHMARK_FUNCTIONS["safe_divide"] = """
def safe_divide(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return None
    if b == 1:
        return 0
    return a / b
"""

# Function 2: Nested conditionals on three sides
# Bug: equilateral checks a == b instead of a == b == c
BENCHMARK_FUNCTIONS["classify_triangle"] = """
def classify_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "invalid"
    if a + b <= c or a + c <= b or b + c <= a:
        return "invalid"
    if a == b:
        return "equilateral"
    elif a == b or b == c or a == c:
        return "isosceles"
    else:
        return "scalene"
"""

# Function 3: Modular arithmetic with multiple conditions
# Bug: uses % 12 instead of % 15 for fizzbuzz case
BENCHMARK_FUNCTIONS["fizzbuzz"] = """
def fizzbuzz(n):
    if not isinstance(n, int):
        return None
    if n <= 0:
        return "invalid"
    if n % 12 == 0:
        return "fizzbuzz"
    elif n % 3 == 0:
        return "fizz"
    elif n % 5 == 0:
        return "buzz"
    else:
        return str(n)
"""

# Function 4: List traversal with type guard
# Bug: checks len == 1 instead of len == 0 for empty list
BENCHMARK_FUNCTIONS["find_max"] = """
def find_max(lst):
    if not isinstance(lst, list):
        return None
    if len(lst) == 1:
        return None
    result = lst[0]
    for item in lst:
        if item > result:
            result = item
    return result
"""

# Function 5: Boundary conditions with multiple thresholds
# Bug: B grade starts at 79 instead of 80
BENCHMARK_FUNCTIONS["letter_grade"] = """
def letter_grade(score):
    if not isinstance(score, (int, float)):
        return None
    if score < 0 or score > 100:
        return "invalid"
    if score >= 90:
        return "A"
    elif score >= 79:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
"""

# Function 6: Nested modular arithmetic
# Bug: uses % 200 instead of % 400 for century leap year exception
BENCHMARK_FUNCTIONS["is_leap_year"] = """
def is_leap_year(year):
    if not isinstance(year, int):
        return None
    if year <= 0:
        return None
    if year % 200 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
"""

# Function 7: String iteration with membership check
# Bug: vowel set is missing 'u'
BENCHMARK_FUNCTIONS["count_vowels"] = """
def count_vowels(s):
    if not isinstance(s, str):
        return None
    if len(s) == 0:
        return 0
    count = 0
    for char in s.lower():
        if char in "aeio":
            count += 1
    return count
"""

# Function 8: Boundary clamping
# Bug: uses > instead of >= for upper bound check
BENCHMARK_FUNCTIONS["clamp_value"] = """
def clamp_value(value, low, high):
    if not isinstance(value, (int, float)):
        return None
    if low > high:
        return None
    if value < low:
        return low
    elif value > high:
        return high
    else:
        return value
"""

# Function 9: Absolute value with sign check and type guard
# Bug: returns negative for positive numbers (swapped sign logic)
BENCHMARK_FUNCTIONS["absolute_value"] = """
def absolute_value(n):
    if not isinstance(n, (int, float)):
        return None
    if n > 0:
        return -n
    elif n < 0:
        return -n
    else:
        return 0
"""

# Function 10: Temperature converter with mode selection
# Bug: Fahrenheit to Celsius uses + 32 instead of - 32
BENCHMARK_FUNCTIONS["temp_convert"] = """
def temp_convert(temp, mode):
    if not isinstance(temp, (int, float)):
        return None
    if mode == "c_to_f":
        return temp * 9 / 5 + 32
    elif mode == "f_to_c":
        return (temp + 32) * 5 / 9
    else:
        return None
"""