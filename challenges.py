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
        if start in Arr:
            start += 1
        else:
            return start



""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""
12- Ratiorg got statues of different sizes as a present, each statue
having an non-negative integer size. Since he likes to make things perfect,
he wants to arrange them from smallest to largest so that each statue will be
bigger than the previous one exactly by 1. He may need some additional statues
to be able to accomplish that. Help him figure out the minimum number of 
additional statues needed.
Example
For statues = [6, 2, 3, 8], the output should be
makeArrayConsecutive2(statues) = 3.

Ratiorg needs statues of sizes 4, 5 and 7.
"""
def makeArrayConsecutive2(statues):
    # declare a counter
    # sort the array
    # iterate over the array
    # el[i+1] - el[i] = difference 
    # if diff >1
    # counter + (difference -1)
    # return counter
    
    counter = 0
    sorted_list = list(sorted(statues))
    for i in range(len(sorted_list) - 1):
        diff = sorted_list[i + 1] - sorted_list[i]
        if diff > 1:
            counter += diff - 1
    return counter
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""
13 --- Given a sequence of integers as an array, determine whether
it is possible to obtain a strictly increasing sequence by removing 
no more than one element from the array.
Note:
sequence a0, a1, ..., an is considered to be a strictly increasing if a0 < a1 < ... < an.
Sequence containing only one element is also considered to be strictly increasing.
Example
    For sequence = [1, 3, 2, 1], the output should be
    almostIncreasingSequence(sequence) = false.

    There is no one element in this array that can be removed in order to get a strictly
    increasing sequence.
    For sequence = [1, 3, 2], the output should be
    almostIncreasingSequence(sequence) = true.

You can remove 3 from the array to get the strictly increasing sequence [1, 2]
Alternately, you can remove 2 to get the strictly increasing sequence [1, 3].
"""

def almostIncreasingSequence(sequence):
    copy = sequence 
    
    print("original",copy)
    for i in range(len(sequence)):
        print(i)
        element = copy[i]
        copy.pop(i)
        print(copy)
        if copy == list((sorted(set(copy)))): 
            return True
        else:
            copy.insert(i, element)
            print(sequence)
    return False

""""
14-- Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as
forward. For example, 121 is palindrome while 123 is not.
"""
def isPalindrome(x:int) -> bool:
        if x < 0:
            return False
        string_version = str(x)
        start = 0
        end = len(string_version) - 1
        mid = (end + start) // 2
        while start <= end:
            if string_version[start] == string_version[end]:
                start = start + 1
                end = end - 1
            else:
                return False
        return True

""""
15--Implement an algorithm to determine if a string has all unique
    characters 
"""
def unique_string(givenString:str) -> bool:
    if len(list(givenString)) == len(list(set(givenString))):
        return True
    return False



"""16--. Given the following string:

  "I want to be a part of it New York New York"

Find the most common pair of consecutive words.
Output: ("New", "York")

input: string of words
outpot: tuple of the 2 words the repeated the most"""

# iterate over the string
# take tow consecutive words
# map into a dictionary {pair of words: occurance}
# return the kay with the largest value
def get_consecutive_words(input):
    dict_words = {}
    input = input.split(" ")
    print(input)
    
    for i in range(len(input) - 1):
        
        pair = input[i] +","+ input[i + 1] 
       
        if pair not in dict_words:
            dict_words[pair] = 0
        if pair in dict_words:
            dict_words[pair] += 1
    print(dict_words)
    sorted_values = sorted(dict_words.values())
    print (sorted_values[-1])
    
    for key, value in dict_words.items():
        if dict_words[key] == sorted_values[-1]:
            print(dict_words[key], key.split(","))
            result =  tuple(key.split(","))
            print(result)
            return result
get_consecutive_words("I want to be a part of it New York New York")



"""17-- Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, 
and you may not use the same element twice.You can return the answer in any order."""

# input: array of integers, target integer
# output: array of indices for the 2 numbers that sums == target 

# declare an empty results array
# iterate over the array
# declare a placeholder for the current value 
# iterate over the rest of the elements
# check if any value when added to the current sums to target 
# if yes push the indeces for current and the element to results array

def twoSum(nums, target):
    hash_nums = {}
    for i, num in enumerate(nums):
        if (target - num) not in hash_nums: 
            hash_nums[num] = i
        else:
            return [hash_nums[target - num], i]


"""Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j"""

# inputs: Array of integers
# output: integer (number of good pairs)

# declare results array
# step1: iterate over the values in the array
# step2: take first value and iterate comparing the rest of the values to it 
# step3: if the number[i] == number [j] 
# step4: push the pair(i,j) to the results
# step5: reurn reults length


def numIdenticalPairs(nums):
    results = []
    for i in range(len(nums)):
        for j in range(i+ 1, len(nums)):
            if nums[i] == nums[j]:
                results.append((i,j))
    return len(results)
                

"""You're given strings jewels representing the types of stones that are jewels,
and stones representing the stones you have. Each character in stones
is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive,
so "a" is considered a different type of stone from "A"""

# inputs: 2 strings of letters
# output: integer (number of letters in string-2 that also in string-1)

# step1: declare a counter
# step2: iterate over the string-2:
# step3: if the current letter exists in string-1
#        increase the counter
# step4: return the counter


def numJewelsInStones(jewels: str, stones: str) -> int:
    counter = 0
    for letter in stones:
        if letter in jewels:
            counter += 1
            
    return counter

# Optimized Solution:

# inputs: 2 strings of letters
# output: integer (number of letters in string-2 that also in string-1)

# declare a counter
# step1: build a hashmap for string-1
# step2: iterate over the string-2:
# step3: if the current letter exists in Hashmap
#        increase the counter
# step4: return the counter


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = 0
        
        hashmap = {}
        
        for letter in jewels:
            if letter not in hashmap:
                hashmap[letter] = letter 
                
        for letter in stones:
            if letter in hashmap:
                counter += 1
                
        return counter


""" Given the array nums, for each nums[i] find out how many numbers
in the array are smaller than it. That is, for each nums[i] you have to
count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array."""

# inputs: array of integers
# output: array of integers(counters for the number of integers less than the current integer)


# declare results array
# step1: iterate over the nums array _i
# step2: declare a counter 
# step3: iterate over the rest of the nums _j
# step4: if nums[j] < nums[i]
#        increase the counter
# push the counter to the results


def smallerNumbersThanCurrent(nums):
    results = []
    for i in range(len(nums)):
        
        counterForCurrent = 0
        
        for j in range(len(nums)):
            if nums[j] < nums[i]:
                counterForCurrent += 1
        results.append(counterForCurrent)
    return results


"""Given a list of the scores of different students, items,
where items[i] = [IDi, scorei] represents one score from a student with IDi,
calculate each student's top five average.

Return the answer as an array of pairs result, where result[j] = [IDj, topFiveAveragej]
represents the student with IDj and their top five average.
Sort result by IDj in increasing order.

A student's top five average is calculated by taking the sum of their top five scores
and dividing it by 5 using integer division."""

# inputs: array of arrays -pairs of (id, score)
# output: array of arrays -pairs of (id, AvarageScore)

# step1: declare a results array
# step2: declare an empty hashmap 
# step3: iterate over the arrays in the given array
# step4: map the id as key and the score as part of the value(value array of scores)
#       { id1 : [score1, score2, ...],
#         id2 : [score1, score2, ...], }
# step5: calculate avarage of each value 
#        1. sort the value array 
#        2. slice it and take the highest 5 values
#        3. divide the sum of the values over 5
# step6: append (id, average) to the results array
# step7: return results array



def highFive(items):
    
    results = []
    hashmap = {}
    
    for item in items:
        keyID = item[0]
        score = item[1]
        if keyID not in hashmap:
            hashmap[keyID] = []
        if keyID in hashmap:
            hashmap[keyID].append(score)        
    print(hashmap)
    
    for key, value in hashmap.items():
        value = sorted(value)
        print(value)
        value = value[-5:]
        print(value)
        value = sum(value) // 5
        print(value)
        results.append([key, value])
    return sorted(results)


'''
You are given an integer array nums. 
The unique elements of an array are the elements that appear exactly once in the array.
Return the sum of all the unique elements of nums
'''

# inputs: array of integers
# output: integer numbers
#        (sum of the elements that wasn't repeated in the inputs array)


# step1: iterate over the array
# step2: Build a hashmap of elements as keys and their accurance as value
# step3: iterate over the key, value pairs 
# step4: if the value == 1 => add it to the counter
# step5: return the counter

def sumOfUnique(nums):
    
    hashmap = {}
    counter = 0
    for num in nums:
        if num in hashmap:
            hashmap[num] += 1
        if num not in hashmap:
            hashmap[num] = 1
    print(hashmap)

    for key,value in hashmap.items():
        if value == 1:
            counter += key
    return counter

# Solution with a Counter dict
from collections import Counter

def sumOfUnique(nums):
    
    hashmap = Counter(nums)
    counter = 0
    
    for key,value in hashmap.items():
        if value == 1:
            counter += key
    return counter