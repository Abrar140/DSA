def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]  # Pick the current element
        j = i - 1

        while j >= 0 and arr[j] > key:  # Shift larger elements to the right
            print("i am here", arr[j], key)
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  # Insert the key at its correct position
        print("...............", arr)
    return arr

# Example Usage
arr = [45,1,32,74,3]
print("Sorted Array:", insertion_sort(arr))  # Output: [11, 12, 22, 25, 64]
