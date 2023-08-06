# Problem 1: Find the Missing Number
# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n,
# find the one missing number in the array.
# Example: Input: [3, 0, 1] Output: 2

# sort the array
# loop through the array
# compare current number with next number
# if next is not equal to current + 1 
# return next - 1 

def find_missing(arr):
    arr = sorted(arr)
    for i in range(len(arr) - 1): 
        current_num = arr[i]
        next_num = arr[i + 1]
        if next_num != current_num + 1:
            return next_num - 1
    return "all good!"
        
print("find_missing", find_missing([1,3,5,6,8,7])) # output: 2
        
# Problem 2: Product of Array Except Self
# Given an array nums of n integers, return an array output
# such that output[i] is equal to the product of all the elements of nums except nums[i].
# Example:
# Input: [1, 2, 3, 4] Output: [24, 12, 8, 6]

# declare a results array
# loop through the input array
# declare a product variable initialized to 1
# at each index loop through the array again
# update product
# push to the results the product divided by the current
# return the results array

def product_list(arr):
    results = []
    for i in range(len(arr)):
        product = 1
        for j in range(len(arr)):
            product = (product * arr[j])
            # print(i, j, product)
        if product == 0:
            return 0
        results.append(product // arr[i])
    return results
print("product_list", product_list([2,5,10])) # output: [50, 20, 10]
print("product_list", product_list([0,0,0])) # output: 0
print("product_list", product_list([1,1,1])) # output: [1, 1, 1]

# Problem 3: Sort Array by Parity
# Given an array of integers, rearrange the elements in such a way that all even numbers appear before the odd numbers. The rela.ve order of even and odd elements should remain the same.
# Example:
# Input: [3, 1, 2, 4] Output: [2, 4, 3, 1]

# Assuming that odds and evens are going to be
# # create 2 lists odd nums/even nums
# loop through the input array
# check if number is even or odd
# append it the odd/even list
# extend even list with odd one

def parity_sort(arr):
    even_nums = []
    odd_nums = [] 
    for num in arr:
        if num % 2 == 0:
            even_nums.append(num)
        else:
            odd_nums.append(num)
    return even_nums + odd_nums

print("parity_sort", parity_sort([3,1,2,4])) #output: [2, 4, 3, 1]

# Problem 4: Search in Rotated Sorted Array
# You are given a sorted array that has been rotated at an unknown pivot
# Write a func.on to determine if a target element exists in the array.
# If the target is found in the array, return its index; otherwise, return -1.
# Example:
# Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 0 Output: 4

# loop through the input array
# compare current elemenet with target
# return index of current element if equal to target
# in case loop is finished without returning any value
# return -1

def search_target(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

print("search_target", search_target([4,5,6,7,0,1,2], 0)) # output: 4

# Problem 5: Maximum Subarray Sum
# Given an integer array nums, find the con.guous subarray
# (containing at least one element) with the largest sum and return its sum.
# Example:
# Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

# declare largest sum and initialize it to 0
# declare a start and end pointers
# loop through the array starting from first
# declare current sum to 0
# start an inner loop through the elements again
# in reference to the outer loop
# add current element to the current sum
# compare current sum with largest sum
# update largest sum and index of start and end

def largest_array_sum(arr):
    largest_sum = 0
    start, end = 0, 0
    for i in range(len(arr)):
        current_sum = 0
        for j in range(i, len(arr)):
            current_sum += arr[j]
            if current_sum > largest_sum:
                largest_sum = current_sum
                start = i
                end = j
    return arr[start: end+1]

print("largest_array_sum", largest_array_sum([-2,1,-3,4,-1,2,1,-5,4])) # output: [4, -1, 2, 1]

# Problem 6: Remove Duplicates from Sorted Array
# Given a sorted array nums, remove the duplicates in-place
# such that each element appears only once, and return the new length.
# Example:
# Input: nums = [1, 1, 2, 2, 3, 4, 4]
# Output: 4 (Explana.on: The first four elements of nums [1, 2, 3, 4] are unique.)

# decalre variable i, initialized to 0
# while i value is less than the last elments index
# check each element and the one after it
# if equal, remove the element that's duplicated
# if not equal, increment i 
def remove_duplicates(arr):
    i = 0
    while i < len(arr) - 1:
        if arr[i] == arr[i + 1]:
            arr.remove(arr[i + 1])
        else:
            i += 1
    print(arr)
    return len(arr)

print("remove_duplicates", remove_duplicates([1,1,2,3,3,4,4]))       
print("remove_duplicates", remove_duplicates([1,1,2,2,3,3,4,4,5,6,6]))

# Problem 7: Array Partition I
# Given an array of 2n integers
# group these integers into n pairs of two elements
# such that the sum of the minimum of each pair is maximized. Return the maximum sum.
# Example:
# Input: [1, 4, 3, 2]
# Output: 4 (Explanation: The pairs are (1, 2) and (3, 4).
# The minimum of each pair is 1 and 3, and the maximum sum is 4.)

# sort the array
# partition each 2 elements into a sub array
# add the first element of each subarray to sum
# return sum
def min_sum(arr):
    arr.sort()
    current = 0
    sum = 0
    while current < len(arr):
        sub = arr[current : current+2]
        sum += sub[0]
        current += 2
    return sum
print("min_sum", min_sum([3, 1, 6, 2, 4, 5])) # output: 9
print("min_sum", min_sum([6, 2, 9, 3, 7, 5])) # output: 14

# Problem 8: Find All Duplicates in an Array
# Given an array of integers, 1 ≤ a[i] ≤ n (n is the size of the array)
# some elements appear twice, and others appear once
# Find all the elements that appear twice in the array.
# Example:
# Input: [4, 3, 2, 7, 8, 2, 1, 3] Output: [2, 3]

# declare an empty dictionary and results list
# loop through the given array
# for each number in array check if the number exist as a dict key
# if it's not a key, add it to the dict with value 1if it's already in the dict increment it's value by 1
# loop through the dict items 
# append the kay that has value more than 1 to the results list
# return the results list

def find_duplicate(arr):
    dict = {}
    results = []
    for num in arr:
        if num in dict.keys():
            dict[num] += 1
        if num not in dict.keys():
            dict[num] = 1
    for key, value in dict.items():
        if value > 1:
            results.append(key)
    return results

print("find_duplicate", find_duplicate([4, 3, 2, 7, 8, 2, 1, 3])) #output: [3, 2]
print("find_duplicate", find_duplicate([1,2,4])) #output: []