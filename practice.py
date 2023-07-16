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
        # print("F")
        return False
    else :
        # print("T")
        return True
is_anagram_of_palindrome("abcbs")
is_anagram_of_palindrome("abcbc")

"""Given two strings s and t, return true if t is an anagram of s
and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters
of a different word or phrase, typically using all the original letters exactly once.
"""
# inputs: 2 strings
# outputs: T / F

def is_Anagram(s, t):
    sorted_s = sorted(s)
    sorted_t = sorted(t)
    if sorted_s == sorted_t:
        print("T")
        return True
    else:
        print("False")
        return False

is_Anagram("abcd","dcab")


import random
def get_username(first, last):
    s = f"{first}.{last}"
    return s.lower()

def main():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    username = get_username(first_name, last_name)
    print(f"Your username is: {username}")
  
n = random.randint(0,2)
print(n)

def add_item(list, food):
    food = "apple pie"
    list.append(food)

def main():
    lunch = ["sandwich", "chips", "pickle"]
    food = "banana"
    add_item(lunch, food)
    print(lunch)

main()


    

    
