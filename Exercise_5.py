# Python program for implementation of Quicksort
#time complexity: O(nlogn) 
#space complexity: O(n)
#passed all cases on LeetCode:
#difficulty faced: iterative is much harder to implement using a stack
# comments: choosing the last elemet of the arr as pivot.
# elements less than pivot are to the left and gt pivot are on right
# This function is same in both iterative and recursive
def partition(arr, low, high):
  #write your code here
    pivot = arr[high]

    #this is pointer to greater element used to swap with later
    i = low - 1

    for j in range(low,high):
        if arr[j] <= pivot:
            i = i+1
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp

    #after the loop is done, swap pivot and greater element
    arr[i+1], arr[high] = arr[high], arr[i+1]
    #we need to return the position of partition element
    return i+1
  

def quickSortIterative(arr, l, h):
  #write your code here

    stacksize = h - l + 1
    stack = [0] * stacksize

    #initialize top of stack
    top = -1

    #push l and h in the stack
    top += 1
    stack[top] = l
    top += 1
    stack[top] = h

    while top > 0:
        h = stack[top]
        top -= 1
        l = stack[top]
        top -= 1

        pe = partition(arr,l,h)

        #need to continue if there are elements on left of partition
        if pe -1 > l:
            top += 1
            stack[top] = l
            top += 1
            stack[top] =  pe-1

        #similarly for right of partition
        if pe+1 < h:
            top += 1
            stack[top] = pe+1
            top += 1
            stack[top] =  h

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 