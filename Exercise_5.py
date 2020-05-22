# Time Complexity : O(n log n) where n is the number of nodes
# Space Complexity : O(h) = O(log n)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : Yes a little bit, I got confused about how to imitate pre order 
  # traversal iteratively, and how to account for low,high. But eventually after a little bit of effort I was able to figure out



# Python program for implementation of Quicksort

# This function is same in both iterative and recursive

'''
I have use the Pre-order tree traversal using Stack to achieve the iterative quicksort.
Then accounting for right part and pusging it to the satck and then left part.
The left part is pushed after right so that left one popped first

'''
def partition(arr, l, h):
    pivot_element = arr[h]
    pIndex = l
    for i in range(l, h):
        if arr[i] < pivot_element:
            temp = arr[i]
            arr[i] = arr[pIndex]
            arr[pIndex] = temp
            pIndex += 1
    
    temp = arr[pIndex]
    arr[pIndex] = arr[h]
    arr[h] = temp

    return pIndex


def quickSortIterative(arr, l, h):
    
    stack = []
    current = (l,h)
    stack.append(current)

    while(len(stack) > 0):
        
        current = stack.pop()
        low, high = current[0], current[1]

        p = partition(arr, low, high)

        if p+1 < high: 
            stack.append((p+1,high))
        if p-1 > low:
            stack.append((low, p-1))
    
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i])




