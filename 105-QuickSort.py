def partition(arr, low, high):
    pivot = arr[high]  # Choosing the last element as pivot
    i = low - 1  # Start with i at -1 (before the first element)

    for j in range(low, high):  # Iterate over the array
        if arr[j] < pivot:  # If current element is smaller than pivot
            i += 1  # Move boundary of smaller elements
            arr[i], arr[j] = arr[j], arr[i]  # Swap arr[i] and arr[j]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Swap pivot to correct position
    print("...............", arr)
    return i + 1  # Return pivot index

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)  # Partitioning index
        quick_sort(arr, low, pi - 1)  # Recursively sort left part
        quick_sort(arr, pi + 1, high)  # Recursively sort right part

# Example Usage
arr = [45, 1, 32, 74, 3]
quick_sort(arr, 0, len(arr) - 1)
print("Sorted Array:", arr)
