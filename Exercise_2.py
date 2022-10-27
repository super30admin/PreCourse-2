# Python program for implementation of Quicksort Sort 
# give you explanation for the approach

#Time Complexity: O(n^2)
#Space Complexity: O(1)

def partition(arr,low,high):
    #last element is the pivot elem by default
    pElem = arr[high]
    pIndex = low
    for curIndex in range(low,high):
        curElem = arr[curIndex]
        if curElem <= pElem:
            swap(arr, pIndex, curIndex)
            pIndex += 1
    swap(arr, pIndex, high)

    return pIndex

def swap(arr, i1, i2):
    temp = arr[i1]
    arr[i1] = arr[i2]
    arr[i2] = temp

# Function to do Quick sort 
def quickSort(arr,low,high):
    if low < high:
        pIndex = partition(arr, low, high)  
        quickSort(arr, low, pIndex - 1)
        quickSort(arr, pIndex + 1, high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i], end=" "), 
  
 
