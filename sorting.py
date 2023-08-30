# Bubble sort 
# O(n^2)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Merge sort
# O(n logn)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    left = merge_sort(left)
    right = merge_sort(right)
    # print("here",left, right)
    return merge(left, right)
    
def merge(l, r):
    print("lef and right",l, r)
    res = []
    i, j = 0, 0
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            res.append(l[i])
            i += 1
        else:
            res.append(r[j])
            j += 1
        # print("result",res)
    res.extend(l[i:])
    res.extend(r[j:])
    return res
    
print(merge_sort([5,7,1,3,4,2,6]))