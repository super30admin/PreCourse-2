# Time Complexity :O(N^2) is the worst case 
# Space Complexity : O(logN) the array
# Did this code successfully run on Leetcode : I tried in VS code 
# Any problem you faced while coding this :No

# give you explanation for the approach
# In the quick sort function I am check if the low index is less than the high index then calling the partition function. 
# In the partition function I am running a for loop from the low index to the high index and checking if the current element is less than the pivot.
# then swapping the elements and returing the elements
# then recursing on the left and right subarrays 
def partition(arr,low,high):
    pivot = arr[high]
    i = low - 1
    for j in range(low,high):
        if arr[j] < pivot:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1

def quickSort(arr,low,high): 
    if low < high:
        part = partition(arr, low, high)
        quickSort(arr, low, part - 1)
        quickSort(arr, part + 1, high)

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print (arr[i]), 
  
 