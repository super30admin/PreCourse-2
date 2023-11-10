# Time Complexity O(n^2)
#Space COmplexity O(n)

# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr,l,h):
    i = l
    x = arr[h]
    j = h
    while i < j:
        if  arr[j] <= x:
            arr[i],arr[j] = arr[j],arr[i]
            i += 1
        j -= 1
   
    arr[i],arr[h] = arr[h],arr[i]
    
    return i

def quickSortIterative(arr, l, h):
  #write your code here
    if len(arr) == 1:
        return arr
    if l < h:
        pivot = partition(arr, l, h)
        quickSortIterative(arr, l, pivot-1)
        quickSortIterative(arr, pivot, h)


# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
