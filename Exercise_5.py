# Python program for implementation of Quicksort

# Time Complexity: O(n logn) - we splits the list every time near middle we iterate and O(n) for the going over the stack for best case and worst case O(n^2)
# Space Complexity: O(log n) - for stack overhead and O(n) - worst case

# This function is same in both iterative and recursive
def partition(arr, low, high):
    slot = low
    pivot = arr[high-1]
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[j], arr[slot] = arr[slot], arr[j]
            slot += 1

    return slot -1

def quickSortIterative(arr, l, h):
    stk = [(l, h)]

    while stk:
        low, high = stk.pop()
        if low >= high:
            continue
        pivot_idx = partition(arr, low, high)
        stk.append((low, pivot_idx))
        stk.append((pivot_idx+1, high))


# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
        
