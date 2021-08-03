""" Challenges"""
""" 1- Is the word an anagram of a palindrome?

    >>> is_anagram_of_palindrome("a")
    True
    >>> is_anagram_of_palindrome("ab")
    False
    >>> is_anagram_of_palindrome("aab")
    True
    >>> is_anagram_of_palindrome("arceace")
    True
    >>> is_anagram_of_palindrome("arceaceb")
    False
    """
def is_anagram_of_palindrome(word):

    # create a dictionary where 
    # keys: character in given word
    # values: occurences of each character
    # if there is more than one char whos value == 1
    # return false

    word_dict = {}
    for char in word:
        if char not in word_dict:
            word_dict[char] = 1 
        else: 
            word_dict[char] += 1

    print(word_dict)
    odd_counts = 0
    for count in word_dict.values():
        if count % 2 != 0:
            odd_counts += 1
    if odd_counts > 1 :
        return False
    else :
        return True

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""" 2- Using binary search, find val in range 1-100. Return # of guesses.
    
    >>> binary_search(50)
    1
    >>> binary_search(25)
    2
    >>> binary_search(75)
    2
    >>> binary_search(31) <= 7
    True    
    >>> max([binary_search(i) for i in range(1, 101)])
    7
"""

def binary_search(val):
  
    assert 0 < val < 101, "Val must be between 1-100"

    num_guesses = 0


    min = 1
    max = 100
    mid = None
    while mid != val:
        num_guesses += 1
        mid = (max + min) // 2

        if val < mid:
            max = mid 
                 
        elif val > mid:
            min = mid      
    return num_guesses

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""" 3- Write a function that takes in a list of strings. 
    Return the longest string in the list.

    >>> find_longest(["a", "abc", "abcd"])
    "abcd"
    >>> find_longest([])
    []
    >>> find_longest(["hi", "bi"])
    "hi"
"""
# assume first string ==> longest
# iterate over the list of strings
# compare next element to longest 
# if current is longer than longest ==> reassign longest 


def find_longest(str_list):
    
    longest = str_list[0]
    for string in str_list:
        if len(string) > len(longest):
            longest = string
             
    return longest

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""" 4- Write a function that takes in an item and a list
    Return the number of times the given item appears in the list
>>> find_occurrence([1,2,3,4,3,4,6,2,4], 4)
3
>>> find_occurrence([1,2,3,4,3,4,6,2,4], 9)
0
"""
# declare empty dict
# iterate over the list
# construct a dictionary {key : value} ==> {element : number of accurences}
# return the value for the targeted element

def find_occurrence(items_list, target_item):
    items_dict = {}
    for item in items_list:
        if item not in items_dict:
            items_dict[item] = 1
        else:
            items_dict[item] += 1
    if target_item not in items_dict:
        return 0
        
    return items_dict[target_item] 

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""" 5- Write a function that takes in a string and returns
    a string with all vowels replaced with *

>>> replace_vowels1("string") 
"str*ng"
>>> replace_vowels1("Hello") 
"H*ll*"

"""
def replace_vowels1(string):
    vowels = "aeiou"
    new_string = []
    for char in string:
        if char in vowels:
            new_string.append("*")
        else:
            new_string.append(char)
    return "".join(new_string)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""" 6- Write a function that takes in two strings and 
    returns True if the strings are anagrams of one another.

>>> is_anagram('moon', 'noom')
True
>>> is_anagram('bat', 'snack')
False
>>> is_anagram('', '')
True

"""
def is_anagram(string1, string2):
    if sorted(string1) == sorted(string2):
        return True
    return False

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""" 7- Write a function that takes in two arguments: 
    a list of numbers and a number, It should return the largest number
    in the list that is smaller than the given number
    [1, 300, 3, 5, 70], 100 => 70

>>> largest_smaller([1, 300, 3, 5, 70], 100)
70

"""

def largest_smaller(nums, target_num):
    
    while nums:
        less_than_target = []
        for num in nums:
            if num < target_num:
                less_than_target.append(num)
        result = sorted(less_than_target).pop()
        return result
    else:
        print ("list is Empty")

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""" 8- Write a function that takes in a list of numbers.
    It should return True if any two numbers in the list add to 0

"""
def add_to_zero(nums):
    nums_set = set(nums)
    print(nums_set)
    for num in nums:
        if -num in nums_set:
            return True
    return False

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""" 9- Write a function that takes in a number. Return a number
    with the digits of the given number, but in reverse order.

>>> reverse_digits(123)
321
>>> reverse_digits(789)
987

"""
def reverse_digits(n):
    string_n = str(n)
    reversed_n = reversed(string_n)
    rev_string = "".join(reversed_n)
    return int(rev_string)
    
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""" 10- Given an integer array nums, return true if any value appears
    at least twice in the array, and return false if every element is distinct.

[1,2,3,1] ==> true
[1,2,3,4] ==> false
"""

def containsDuplicate(nums):
    nums_set = set(nums)
    if len(nums) == len(nums_set): 
        return False
    return True

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""
11 - Write a function that, given an array Arr of N integers, 
returns the smallest positive integer (greater than 0) that does not occur in A.
For example:
Given A = [1, 3, 6, 4, 1, 2], the function should return 5.
Given A = [1, 2, 3], the function should return 4.
Given A = [−1, −3], the function should return 1.
"""

def solution(Arr):
    start = 1
    result = []
    while start > 0:
        if start in A:
            start += 1
        else:
            return start
"""A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps. The number 32 has binary representation 100000 and has no binary gaps.

Write a function:

def solution(N)

that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.

For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps."""


def solution(N):
    # find the binary representation of the number
    # declare a counter  
    # loop over the 0s and 1s 
    # check if char is 1 
    # check if 1 / 0 comes after it
    # if 1 == > continue 
    #  if 0 continue counter + 1

    binN = list(bin(N)[2:])
    # print(binN, type(binN))
    dictN = {}
    for index in range(len(binN) - 1):
        if index == len(binN) - 1:
            return
            # print(index, binN[index])
        else:
            if binN[index] == "1":
                dictN[index] = []
                for i in range(index + 1):
                    if binN[i] == "0":
                        dictN[index].append("0")
    # print(dictN)
    length = 0
    for value in dictN.values():
        if len(value) > length:
            length = len(value)
    return length



