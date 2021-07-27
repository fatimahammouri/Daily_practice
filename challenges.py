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
    index = 0
    longest = str_list[index]
    for each_string in str_list:
        if str_list[index + 1] > longest:
            longest = str_list[index + 1]
             
    return longest

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""" Write a function that takes in an item and a list
    Return the number of times the given item appears in the list
>>> find_occurrence([1,2,3,4,3,4,6,2,4], 4)
3
>>> find_occurrence([1,2,3,4,3,4,6,2,4], 9)
0
"""


