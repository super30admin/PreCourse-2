# Time Complexity : 
#     Average case: O(nlogn)
#     Worst case: O(n^2)
# Space Complexity :
#     Average case: O(logn)
#     Worst case: O(n)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : 
#                     I watched youtube video to understand the algorithm, made a psuedo code.
#                     Found the leetcode post helpful http://leetcode.com/discuss/post/1083445/how-quick-sort-works-and-the-problems-th-1h5f/
#                     Wrote down the notes for it so I do not forget it again, and memorized the word pivot with quick sort.

# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    '''
    We choose the first element as a pivot.
    We start a wall as second element where all the elements left 
    of it are always smaller than pivot.
    We iterate thought the array and find elements smaller than pivot, swap it with the current position of wall
    and move the wall to the right.
    Finally we will have the first element as pivot and all the elements smaller than the pivot will be on the 
    left of the wall. So now we swap the pivot with the element closest to the wall which is exactly the correct
    placement of the pivot. 
    Now all the elements to the left of it are smaller and all the elements to the right are bigger than the pivot.
    '''
  
    #write your code here
    pivot = arr[low]
    leftwall = low + 1

    for j in range(low+1, high+1):
        if arr[j] <= pivot:
            arr[leftwall], arr[j] = arr[j], arr[leftwall]
            leftwall += 1
    
    arr[leftwall - 1], arr[low] = arr[low], arr[leftwall - 1]
    return leftwall - 1
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    '''
    First we find the correct position of a pivot, then we sort the left half of the pivot
    and the right half of the pivot which will eventually sort the entire array as the recurssion reaches to all
    the elements of the array.
    '''
    #write your code here
    if low < high:
        p = partition(arr, low, high)
        quickSort(arr, low, p-1)
        quickSort(arr, p+1, high)
    return arr

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
