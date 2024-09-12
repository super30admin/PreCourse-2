#  Time Complexity : O(NlogN)
#  Space Complexity : O(N)
#  Did this code successfully run on Leetcode : yes
#  Any problem you faced while coding this : No

# Python code to implement iterative Binary  
# Search. 


# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    i = low - 1 
    pivot = arr[high]  # 10, 7, 8, 9, 1, 5 
    for j in range(low,high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1], arr[high] = arr[high],arr[i +1]
    return (i+1) 

  
 
# Function to do Quick sort 
def quickSort(arr,low,high): 
    if len(arr) == 1:
        return arr
    if low < high:
        p = partition(arr,low,high)
        quickSort(arr,low,p-1)
        quickSort(arr,p+1,high)

  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
'''
approch : recursive 
'''