def merge(arr, l, m, r):
    """
    Merges two sub-arrays of arr[].
    First sub-array is arr[l..m]
    Second sub-array is arr[m+1..r]
    """
    n1 = m - l + 1
    n2 = r - m
    
    # Create temporary arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temporary arrays L[] and R[]
    for i in range(n1):
        L[i] = arr[l + i]
    for j in range(n2):
        R[j] = arr[m + 1 + j]

    # Merge the temporary arrays back into arr[l..r]
    i = 0  # Initial index of first sub-array
    j = 0  # Initial index of second sub-array
    k = l  # Initial index of merged sub-array

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def iterative_merge_sort(arr):
    """
    Performs an iterative merge sort on the given array.
    """
    n = len(arr)
    current_size = 1
    
    # Start with sub-array size 1. In each step, we double it.
    while current_size < n:
        # Pick starting point of different sub-arrays of current size
        left_start = 0
        while left_start < n - 1:
            # Find ending point of first sub-array
            mid = min(left_start + current_size - 1, n - 1)
            
            # Find ending point of second sub-array
            right_end = min(left_start + 2 * current_size - 1, n - 1)
            
            # Merge sub-arrays arr[left_start...mid] & arr[mid+1...right_end]
            merge(arr, left_start, mid, right_end)
            
            # Move to the next pair of sub-arrays
            left_start += 2 * current_size
            
        # Double the sub-array size for the next iteration
        current_size *= 2

# Example Usage
data = [38, 27, 43, 3, 9, 82, 10]
print("Original list:", data)
iterative_merge_sort(data)
print("Sorted list:", data)