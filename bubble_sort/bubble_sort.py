def bubble_sort(unsorted_list):
    n = len(unsorted_list)#Stores the length of the list in variable n.

    for i in range(n):
        swapped = False  # To track if any swap happened in this pass

        for j in range(0, n - i - 1):
            if unsorted_list[j] > unsorted_list[j + 1]:
                # Swap the elements
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]
                swapped = True

        # If no swaps happened, the list is already sorted
        if not swapped:
            break

    return unsorted_list


my_list = list(map(int, input().split()))
sorted_list = bubble_sort(my_list)
print("Sorted list:", sorted_list)

