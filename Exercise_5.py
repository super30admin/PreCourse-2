# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr,low,high):
    pivot = arr[high]
    i = low - 1  # index of smaller element

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            # swap arr[i] and arr[j]
            arr[i], arr[j] = arr[j], arr[i]

    # swap the pivot element with the element at i+1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quickSortIterative(arr, l, h):
    # Create a stack for storing subarray indices
    stack = []

    # Push initial indices
    stack.append((l, h))

    # Process the stack until it's empty
    while stack:
        l, h = stack.pop()

        if l < h:
            pi = partition(arr, l, h)

            # Push right side to stack
            stack.append((pi + 1, h))
            # Push left side to stack
            stack.append((l, pi - 1))


  # Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 

