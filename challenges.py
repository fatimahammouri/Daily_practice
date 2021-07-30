""" Challenges"""

def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome?

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
def binary_search(val):
    """Using binary search, find val in range 1-100. Return # of guesses.
    
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
""" Write a function that takes in a list of strings. 
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
""" Write a function that takes in an item and a list
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

""" Write a function that takes in a string and returns
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
""" Write a function that takes in two strings and 
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
""" Write a function that takes in two arguments: 
    a list of numbers and a number, It should return the largest number
    in the list that is smaller than the given number
    [1, 300, 3, 5, 70], 100 => 70

>>> largest_smaller([1, 300, 3, 5, 70], 100)
70

"""