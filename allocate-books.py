def can_allocate(arr, m, max_pages):
    students = 1
    current_sum = 0

    for pages in arr:
        if current_sum + pages <= max_pages:
            current_sum += pages
        else:
            students += 1
            current_sum = pages
            if students > m:
                return False
    return True
def allocate_books(arr, m):
    low = max(arr)
    high = sum(arr)
    answer = high

    while low <= high:
        mid = (low + high) // 2

        if can_allocate(arr, m, mid):
            answer = mid
            high = mid - 1
        else:
            low = mid + 1
    return answer

arr = [12, 34, 67, 90]
m = 2
print("Minimum possible maximum pages:", allocate_books(arr, m))