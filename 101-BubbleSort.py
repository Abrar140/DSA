def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        print(n, i, n-1)
        swapped = False  # Track if any swap happens
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:  # Compare adjacent elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap
                swapped = True
            print(arr[j],arr[j+1], arr)


        print("...............")
        if not swapped:  # If no swaps occur, the array is already sorted
            break
    return arr

# Example Usage
arr = [45,1,32,74,3]
print("Sorted Array:", bubble_sort(arr))  # Output: [11, 12, 22, 25, 64]
