# O(logN) Algorithm

# Binary Search Algorithm:

# Initialize a 'low' variable pointing to the first index of the array.

# Initialize a 'high' variable pointing to the last index of the array.

# Repeat the following steps while 'low' is less than or equal to 'high':
# a. Calculate the 'mid' point as (low + high) // 2 (integer division).
# b. Compare the target value with the value at the 'mid' index:
#  - If the target value equals the value at the 'mid' point, return 'mid'.
#  - If the target value is larger than the value at the 'mid' point, update 'low' to be 'mid + 1'.
#  - If the target value is less than the value at the 'mid' point, update 'high' to be 'mid - 1'.
# If the loop ends without finding target value, return -1.

def binary_search(array, target):
  low, high = 0, len(array) - 1  
  while low <= high:
    mid = (low + high) // 2
    if target == array[mid]:
      return mid
    elif target > array[mid]:
      low = mid + 1
    else: 
      high = mid - 1
  return -1 

binary_search([1,2,3,4,5,6,7,8], 2)

# Analysis of Binary Search Algorithm:

# 2 + (n/2 * 1/2 * 1/2 * 1/2...) + 1 =
# 3 + n / 2^k =
# we can omit the constants so that leaves us with
# n = 2^k
# log2 n = log2 2^k
# log2 n = K log2 2
# k = log2 n ==> O(log2 N)


# O(N logN) Algorithm
# Merge Sort Algorithm:
# If the array's length is 0 or 1, return the array as is.
# Calculate the midpoint of the array.
# Slice the array into two sub-arrays, left & right around midpoint.
# Recursively call Merge Sort function on both left & right sub-arrays.
# Invoke the Merge function with left & right arrays as arguments.
# Merge Function:
# Declare a new empty array.
# Declare two counters, initialized to 0.
# Iterate while both counters are less than the lengths of the left and right arrays:
# a. Compare the elements of left and right arrays at the same position.
# b. Append the smaller value to the new array.
# c. Increment the counter of the array that the element was appended from.
# After the loop, extend the new array with the remaining elements from both arrays.
# Return the new array.


def merge_sort(array):
  if len(array) <= 1:
    return array
  mid = len(array) // 2
  right_array = array[mid:]
  left_array = array[:mid]
  left = merge_sort(left_array)
  right = merge_sort(right_array)

  return merge(left, right)

def merge(left, right):
  new_array = []
  i, j = 0, 0
  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      new_array.append(left[i])
      i += 1
    else:
      new_array.append(right[j])
      j += 1
  new_array.extend(left[i:])
  new_array.extend(right[j:])
  return new_array

# Analysis of Merge Sort Algorithm:

# T(n) = { 1  , n = 1 }
#        { n * (T(n/2) + T(n/2))  , n > 1} 

#        T(n)
#        / \
# n*T(n/2)  n*T(n/2)
#      /      \
# n*T(n/4)   n*T(n/4)
#     /         \
# n*T(n/8)   n*T(n/8)

# n * T(n/2^k) = 
# n * T(k * log2 n) =
# n * T(log2 n)



