# Python program for implementation of Quicksort Sort 

# // Time Complexity : O(lg n) where n is the number of elements in the array
  # // Space Complexity : O(lg n) where n is the number of elements in the array 
  # for which recursive calls were made
  # // Did this code successfully run on Leetcode : yes
  # // Any problem you faced while coding this : a little when writing the 'terminating condition'
  # if l > r:
  #       return -1

  # // Your code here along with comments explaining your approach

# give you explanation for the approach
def partition(arr,low,high):
    #write your code here
    pivot = arr[high]
    p_index = low
    for i in range(low,high):
        if arr[i] <= pivot:
            arr[i],arr[p_index] = arr[p_index],arr[i]
            p_index += 1
    arr[high],arr[p_index] = arr[p_index],arr[high]
    return p_index


# Function to do Quick sort 
def quickSort(arr,low,high): 
    #write your code here
    if low < high:

        p_index = partition(arr,low,high)
        quickSort(arr,low,p_index-1)
        quickSort(arr,p_index+1,high)

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
print ("Array is:",arr) 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i],end=', '), 
  
 
