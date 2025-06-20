def selection_sort(arr):
    # TODO: Implement selection sort
    n = len(arr)
    for i in range(n):
        # Assume the i-th element is the minimum
        min_index = i
        # Check for a smaller element in the unsorted part
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the smallest found element with the i-th element
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Test it
numbers = [64, 25, 12, 22, 11]
selection_sort(numbers)
print("Sorted list:", numbers)

