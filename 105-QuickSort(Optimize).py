def partition(arr, low, high):
    pivot = arr[high]  # Choosing the last element as pivot
    i = low - 1  # Index for smaller elements

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap if element is smaller than pivot

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Move pivot to correct position
    return i + 1  # Return pivot index

def quick_sort(arr, low, high):
    while low < high:  # Tail Recursion Optimization (TRO)
        print("i am here------",low,high,arr)

        pi = partition(arr, low, high)
        print("i am here",low,high,arr, pi)


        # Recursively sort the smaller partition to reduce recursion depth
        if pi - low < high - pi:
            print("i am here in low part",low,high,arr, pi, pi-low, high-pi)
            quick_sort(arr, low, pi - 1)  # Sort the left partition

            low = pi + 1  # Continue sorting the right partition (eliminates recursion)

        else:
            print("i am here in high part",low,high,arr, pi, pi-low, high-pi)

            quick_sort(arr, pi + 1, high)  # Sort the right partition
            high = pi - 1  # Continue sorting the left partition (eliminates recursion)

# Example Usage
arr = [45, 1, 74, 32, 3]
quick_sort(arr, 0, len(arr) - 1)
print("Sorted Array:", arr)
