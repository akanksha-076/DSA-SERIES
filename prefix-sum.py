# Original array
arr = [2, 4, 6, 8]

# Create prefix array of same size
prefix = [0] * len(arr)

# First element same as original array
prefix[0] = arr[0]

# Calculate prefix sum
for i in range(1, len(arr)):
    prefix[i] = prefix[i-1] + arr[i]

# Print result
print("Original array:", arr)
print("Prefix sum array:", prefix)
