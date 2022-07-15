'''1 Approach'''
# Python program for implementation of Quicksort Sort
# Give your explanation for the approach
'''
Algorithm
    partition(arr, low, high):
        1. Select random pivot index between low and high
        2. Swap the pivot element with the element at index high
        3. Initiailize i and j equal to index at low
        4. Start iterating through the partition by incrementing j. 
           If index at j is equal to index at high - 1 break the loop and go to step 7
        5. If element at j is less than the pivot element swap elemnts at j and i. 
        6. Set j to i and increment i by 1
        7. Swap element at i and pivot element at index high as all values before index i are 
           less than the pivot element and all values at and after i are greater 
           than the pivot element 
        8. Return i as this is the index of the pivot element

    quickSort(arr, low, high):
        1. If low greater than high go to step 4
        2. Get index of pivot element by calling function partition(arr, low, high)
        3. Recursively call quicksort using the new pivot
        4. If low less high repeat step 2 else return arr

quickSort:
    Space Complexity: O(logn) as the nested function calls will create a call stack
    Time Complexity: 
        Average Case:
            O(n log n) as we iterate through all n elements sorting them and split the array after each iteration
        Worst Case:
            O(n ^ 2) as selecting a bad pivot may split the the array unevenly 
            which may result in one of the partions being empty and the other containing all the remaining elements 

'''
# Imports




import random
def partition(arr, low, high):
    # Write your code here
    # To Do implement median-3 method to choose pivot
    # Function to do Quick sort
    random_pivot_index = random.randint(low, high)
    # swap pivot and last element
    arr[random_pivot_index], arr[high] = arr[high], arr[random_pivot_index]
    # initialize i
    i = j = low
    while j < high:
        if arr[j] <= arr[high]:
            arr[i], arr[j] = arr[j], arr[i]
            j = i
            i += 1

        j += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i


def quickSort(arr, low, high):
    if low < high:
        # write your code here
        pivot = partition(arr, low, high)
        quickSort(arr, low, pivot - 1)
        quickSort(arr, pivot + 1, high)
    return arr


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n-1)
print(f"Sorted array is: {arr}")

# ######################Additional Test Cases##########################
# (1) Empty Array
assert quickSort(
    [], 0, 0) == [], f"Expected [] as output but instead got {quickSort([], 0, 0)}"

# (2) Single Element Array
op = quickSort([1], 0, 0)
assert op == [1], f"Expected [1] as output but instead got {op}"

# (3) Minimal Unsorted Array Even
op = quickSort([2, 1], 0, 1)
assert op == [1, 2], f"Expected [1,2] as output but instead got {op}"

# (4) Minimal Unsorted Array Odd
op = quickSort([3, 2, 1], 0, 2)
assert op == [1, 2, 3], f"Expected [1,2,3] as output but instead got {op}"

# (5) Large Unsorted Array
arr = [10, 7, 8, 9, 1, 1, 1, 1, 5, 20, 10, 2, 4, 5, 6, 7, 100, 300]
sorted = [1, 1, 1, 1, 2, 4, 5, 5, 6, 7, 7, 8, 9, 10, 10, 20, 100, 300]
op = quickSort(arr, 0, len(arr)-1)
assert op == sorted, f"Expected {sorted} as output but instead got {op}"

# #######################################################################
