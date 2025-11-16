from Dly_sort import bubble_sort, quick_sort, selection_sort, insertion_sort

a = [5, 6, 45, 99, 10, 8, -9]
b = [-9, 5, 6, 8, 10, 45, 99]

def test_bubble_sort():
    assert bubble_sort(a) == b

def test_selection_sort():
    assert selection_sort(a) == b

def test_quick_sort():
    assert quick_sort(a) == b

def test_insertion_sort():
    assert insertion_sort(a) == b

def factorial(n):
    fact_n = 1
    for i in range(1, n+1):
        fact_n *= i
    return fact_n

def fibonachi(n):
    a = [0] * n
    a[0] = 0
    a[1] = 1
    for i in range(2, n):
        a[i] = a[i-1] + a[i-2]
    return a
def palindrome(s):
    s = str(s).lower().replace(" ", "")
    return s == s[::-1]
def reverse_string(s):
    return s[::-1]

def find_max(a):
    max_val = a[0]
    for num in a[1:]:
        if num > max_val:
            max_val = num
    return max_val

def test_factorial():
    assert factorial(5) == 120
def test_fibonachi():
    assert fibonachi(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
def test_palindrome():
    assert palindrome('А роза упала на лапу Азора') == True
def test_reverse_string():
    assert reverse_string('Привет, Алекс!') == '!скелА ,тевирП'
def test_find_max():
    assert find_max(a) == 99



