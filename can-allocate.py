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