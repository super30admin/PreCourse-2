# Time Complexity : O(logn) , but O(n^2) in worst case
# Space Complexity : O(1) 
# Did this code successfully run on Leetcode : LC 704 yes
# Any problem you faced while coding this : yeah, 
# made some mistakes, 1. j = low, 2. for loop until high - 1, 3.after loop, swapped pivot with arr[j] , 
# 4 in the 'if', wrote < , 5.swapped before j +=1, 6.forgot to rturn from partition func:(

# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    #write your code here

    #can pick any element as pivot 
    # I picked last one
    pivot = arr[high]

    # pointer to keep trck of the element greater than pivot
    j = low - 1

    # compare each one with pivot
    for i in range(low, high):

        # swap element less than pivot with greater tracked by j 
        if arr[i] <= pivot:
            j += 1
            arr[i], arr[j] = arr[j], arr[i]

    # finally swap  pivot with greater than pivot tracked by j      
    arr[j + 1], pivot = pivot, arr[j+ 1]

    # return the partition point
    return j + 1
  

# Function to do Quick sort 
def quickSort(arr,low,high): 

    # after this call, elements less than pivot are on left
    # element greater than pivot are on right
    found_pivot = quickSort(arr,0,n-1) 

    # so do same for left of pivot
    quickSort(arr,0,found_pivot - 1) 

    # so do same for right of pivot
    quickSort(arr,found_pivot + 1,n-1) 

  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
