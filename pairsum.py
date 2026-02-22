arr = [1, 2, 4, 6, 8]
target = 10

left = 0
right = len(arr) - 1

while left < right:
    current_sum = arr[left] + arr[right]

    if current_sum == target:
        print("Pair Found")
        break
    elif current_sum < target:
        left += 1
    else:
        right -= 1
