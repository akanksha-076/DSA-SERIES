def first_occurrence(arr, target):
    low = 0
    high = len(arr) - 1
    ans = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            ans = mid
            high = mid - 1  
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return ans

arr = [1,2,2,2,3,4]
print(first_occurrence(arr, 2))