def merge(array, p, q, r):
    # Create subarrays A[p:q] and A[q+1:r]
    left_array = array[p:q + 1]
    right_array = array[q + 1:r + 1]

    i = 0  # Index for left_array
    j = 0  # Index for right_array
    k = p  # Index for main array

    # Merge the two subarrays back into array[p:r]
    while i < len(left_array) and j < len(right_array):
        if left_array[i] <= right_array[j]:
            array[k] = left_array[i]
            i += 1
        else:
            array[k] = right_array[j]
            j += 1
        k += 1

    # Copy remaining elements of left_array
    while i < len(left_array):
        array[k] = left_array[i]
        i += 1
        k += 1

    # Copy remaining elements of right_array
    while j < len(right_array):
        array[k] = right_array[j]
        j += 1
        k += 1


def merge_sort(array, p, r):
    # Base case: zero or one element
    if p >= r:
        return

    # Midpoint of array[p:r]
    q = (p + r) // 2

    # Recursively sort A[p:q]
    merge_sort(array, p, q)

    # Recursively sort A[q+1:r]
    merge_sort(array, q + 1, r)

    # Merge A[p:q] and A[q+1:r] into A[p:r]
    merge(array, p, q, r)


if _name_ == "_main_":
    array = [2, 4, 5, 7, 1, 2, 3, 6]

    print("Initial array:", array)

    merge_sort(array, 0, len(array) - 1)

    print("Sorted array:", array)