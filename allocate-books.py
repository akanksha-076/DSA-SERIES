
def allocate_books(arr, m):
    low = max(arr)
    high = sum(arr)
    answer = high

    while low <= high:
        mid = (low + high) // 2

        if can_allocate(arr, m, mid):
            answer = mid
            high = mid - 1   # try smaller
        else:
            low = mid + 1

    return answer


arr = [12, 34, 67, 90]
m = 2

print("Minimum possible maximum pages:", allocate_books(arr, m))