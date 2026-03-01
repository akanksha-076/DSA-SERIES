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


def last_occurrence(arr, target):
    low = 0
    high = len(arr) - 1
    ans = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            ans = mid
            low = mid + 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return ans


arr = [1,2,2,2,3,4]

first = first_occurrence(arr, 2)
last = last_occurrence(arr, 2)

if first == -1:
    print("Element not found")
else:
    print("Count:", last - first + 1)