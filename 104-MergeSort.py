def merge_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case: single element is already sorted

    mid = len(arr) // 2  # Find the middle index
    print(mid,  arr[:mid], arr[mid:])
    left_half = merge_sort(arr[:mid])  # Recursively sort left half
    print("..........................................................")
    right_half = merge_sort(arr[mid:])  # Recursively sort right half

    return merge(left_half, right_half)  # Merge the sorted halves

def merge(left, right):

    print("inside",left, right)
    sorted_arr = []
    i = j = 0

    while i < len(left) and j < len(right):  # Merge step
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    sorted_arr.extend(left[i:])  # Copy remaining elements from left
    sorted_arr.extend(right[j:])  # Copy remaining elements from right
    print("..............." ,sorted_arr)

    return sorted_arr

# Example Usage
arr = [45,1,32,74,3]
print("Sorted Array:", merge_sort(arr))  # Output: [11, 12, 22, 25, 64]
