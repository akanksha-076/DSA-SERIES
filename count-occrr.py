arr = [1,2,2,2,3,4]

first = first_occurrence(arr, 2)
last = last_occurrence(arr, 2)

if first == -1:
    print("Element not found")
else:
    print("Count:", last - first + 1)