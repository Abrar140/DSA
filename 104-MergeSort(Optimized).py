def merge_sort_inplace(arr, left, right):
    if left >= right:
        return  # Base case: single element

    mid = (left + right) // 2
    print(mid, left, right)

    merge_sort_inplace(arr, left, mid)  # Recursively sort left half
    merge_sort_inplace(arr, mid + 1, right)  # Recursively sort right half
    print("..........................................................")

    merge_inplace(arr, left, mid, right)  # Merge in-place

def merge_inplace(arr, left, mid, right):
    i = left
    j = mid + 1
    print("inside", i, j)

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:  # Already sorted
            i += 1
        else:
            value = arr[j]
            index = j

            # Shift elements to the right
            while index > i:
                arr[index] = arr[index - 1]
                index -= 1

            arr[i] = value  # Place value at correct position
            
            # Update pointers
            i += 1
            mid += 1
            j += 1

# Example Usage
arr = [64, 25, 12, 22, 11]
merge_sort_inplace(arr, 0, len(arr) - 1)
print("Sorted Array:", arr)  # Output: [11, 12, 22, 25, 64]
