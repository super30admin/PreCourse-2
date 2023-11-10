'''1 Approach'''
# Python program for implementation of Quicksort
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
        1. Check if length of array is less than 2 if so simply return the arr
        2. Initialize empty stack and push the low and high index to the stack 
        2. Iterate through the stack until it is empty than go to step 7
        3. Pop 2 elements from the stack as new low and high
        4. Store the pivot after calling partition(arr, low, high) using these 2 new values
        5. If low is less than pivot - 1, we push both of them to the stack 
        6. If high is greater than pivot + 1, we push both of them to the stack
        7. If stack is empty we return arr else we repeat from step 2

quickSort:
    Space Complexity: O(log n) Since we need to store partition indexes in stack  
    Time Complexity: 
        Average Case:
            O(n log n) as we iterate through all n elements sorting them and split the array after each iteration
        Worst Case:
            O(n ^ 2) as selecting a bad pivot may split the the array unevenly 
            which may result in one of the partions being empty and the other containing all the remaining elements 

'''
# Imports

# This function is same in both iterative and recursive




import random
def partition(arr, low, high):
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


def quickSortIterative(arr, low, high):
    # Base Case
    if len(arr) < 2:
        return arr
  # write your code here
    stack = []
    stack.append(low)
    stack.append(high)

    while stack:
        low = stack.pop(0)
        high = stack.pop(0)
        pivot = partition(arr, low, high)
        if low < pivot - 1:
            stack.append(low)
            stack.append(pivot - 1)
        if high > pivot + 1:
            stack.append(pivot + 1)
            stack.append(high)
    return arr


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSortIterative(arr, 0, n-1)
print(f"Sorted array is: {arr}")

# ######################Additional Test Cases##########################
# (1) Empty Array
assert quickSortIterative(
    [], 0, 0) == [], f"Expected[] as output but instead got {quickSortIterative([], 0, 0)}"

# (2) Single Element Array
op = quickSortIterative([1], 0, 0)
assert op == [1], f"Expected [1] as output but instead got {op}"

# (3) Minimal Unsorted Array Even
op = quickSortIterative([2, 1], 0, 1)
assert op == [1, 2], f"Expected [1,2] as output but instead got {op}"

# (4) Minimal Unsorted Array Odd
op = quickSortIterative([3, 2, 1], 0, 2)
assert op == [1, 2, 3], f"Expected [1,2,3] as output but instead got {op}"

# (5) Large Unsorted Array
arr = [10, 7, 8, 9, 1, 1, 1, 1, 5, 20, 10, 2, 4, 5, 6, 7, 100, 300]
sorted = [1, 1, 1, 1, 2, 4, 5, 5, 6, 7, 7, 8, 9, 10, 10, 20, 100, 300]
op = quickSortIterative(arr, 0, len(arr)-1)
assert op == sorted, f"Expected {sorted} as output but instead got {op}"

# #######################################################################
