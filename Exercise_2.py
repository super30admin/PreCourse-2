def quicksort(arr):
    """
    Perform Quicksort on the input array.
    :param arr: List of elements to be sorted.
    :return: A new sorted list.
    """
    if len(arr) <= 1:
        return arr  
    
    pivot = arr[len(arr) // 2]  
    left = [x for x in arr if x < pivot] 
    middle = [x for x in arr if x == pivot]  
    right = [x for x in arr if x > pivot]  
    
    return quicksort(left) + middle + quicksort(right)


# Example usage
if __name__ == "__main__":
    unsorted_list = [10, 7, 8, 9, 1, 5]
    print("Unsorted List:", unsorted_list)
    sorted_list = quicksort(unsorted_list)
    print("Sorted List:", sorted_list)
