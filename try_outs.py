def find_missing_number(nums):
    n = len(nums)
    expectSum = n*(n+1)/2
    currentSum=0

    for n in nums:
        currentSum += n

    missingNumber=expectSum-currentSum
    return missingNumber

print(find_missing_number([1,3,5,6,8,7]))