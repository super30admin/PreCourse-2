# Python program for implementation of Quicksort Sort 
#   // Time Complexity : O(N^2) because parition is n and recursion is 1
# // Space Complexity : O(N)
# // Did this code successfully run on Leetcode :yes
# // Any problem you faced while coding this : I was first confused how exactly quicksort worked, so i looked it up and understood how it worked, then it was straight forward


# give you explanation for the approach
def partition(arr,low,high):
    pivot = arr[high]       # we are using the last element as the pivot
    index=low               # we always start at low
    while low <high:
        if(arr[low]<=pivot):        # if the number is less than the pivot, then swap it with the first greater number in the array
            arr[low], arr[index] = arr[index] , arr[low]
            index+=1
        low+=1
    arr[high], arr[index] = arr[index], arr[high]       #at the end, swap the pivot next to the last number smaller than it
    return index

  
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low<high:

        parti = partition(arr, low, high)               # first partition the element by using the last element as the pivot
        quickSort(arr, low, parti-1)                    # quicksort the left part of the array after partition
        quickSort(arr, parti+1, high)                   # quicksort the right part of the array after partition
    
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
