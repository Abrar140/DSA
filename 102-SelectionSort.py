def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i  # Assume the current index has the minimum value
        for j in range(i + 1, n):
            print(arr[j],min_index ,arr[min_index], arr)
            if arr[j] < arr[min_index]:  # Find the actual minimum
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]  # Swap
        print("...............")
    return arr

# Example Usage
arr = [45,1,32,74,3]
print("Sorted Array:", selection_sort(arr))  # Output: [11, 12, 22, 25, 64]
