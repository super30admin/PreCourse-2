# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
"""
I have chosen to use the lowest index for assigning the pivot
1. Find the partition index by using the lowest index element as the pivot.
2. The partition index should be such that the elements on left side should be less than pivot
and elements on right side should be greater than pivot. for this we use 2 pointers i and j.
3. once the partion index is found the pivot element is swapped witht he partition index.
4. The array is partitioned into two and quicksory is called recursively on both parts.
"""

def partition(arr,low,high):
    i = low
    j = high
    pivot = arr[low]

    while i<j:
        #print(i,j,arr[i])
        while pivot >= arr[i] and i != len(arr) - 1 :
            #print(arr[i])
            i = i + 1
        while pivot <= arr[j] and j != 0 :
            j = j - 1
        if(i<j):
            arr[i],arr[j] = arr[j],arr[i]

    arr[low],arr[j] = arr[j],arr[low]

    return j
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    if len(arr[low:high]) == 1:
        return arr
    if low < high:
        partition_index = partition(arr,low,high)
        quickSort(arr,low,partition_index)
        quickSort(arr,partition_index+1,high)

  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
