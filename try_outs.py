def find_missing_number(nums):
    n = len(nums)
    expectSum = n*(n+1)/2
    currentSum=0

    for n in nums:
        currentSum += n

    missingNumber=expectSum-currentSum
    return missingNumber

print(find_missing_number([1,3,5,6,8,7]))

# Brute force solution of finding pattern in Text
def find_sub_string(text, sub_string):
    result = []
    i = 0
    while i < (len(text) - len(sub_string) + 1):
        new_sub = text[i:i + len(sub_string)] 
        if new_sub == sub_string:
            result.append(i)
        i += 1
    return result
        
print(find_sub_string("apappleapappleapple", "apple"))


def find_occurrences(text, pattern):
    indexes = []
    for i in range(0, len(text)-len(pattern)+1):
        if text[i: i+len(pattern)] == pattern:
            indexes.append(i)
    return indexes