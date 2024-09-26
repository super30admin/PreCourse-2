# Time Complexity :O(nLog(n))
# Space Complexity :O(Log(n))
# Did this code successfully run on Leetcode : yes
# Any problem you faced while coding this : no


# Your code here along with comments explaining your approach
# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    myP = arr[high]
    PartitionIndex = low
    for i in range(low,high):
        if arr[i] <= myP:
            temp = arr[i]
            arr[i] = arr[PartitionIndex]
            arr[PartitionIndex] = temp
            PartitionIndex +=1
    temp = arr[high]
    arr[high] = arr[PartitionIndex]
    arr[PartitionIndex] = temp
    return PartitionIndex
  

# Function to do Quick sort 
def quickSort(arr,low,high):
    if low>=high:
        return
    PartitionIndex = partition(arr,low,high)
    quickSort(arr,low,PartitionIndex-1)
    quickSort(arr,PartitionIndex+1,high)

  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
