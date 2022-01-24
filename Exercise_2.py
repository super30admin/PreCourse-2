#Time Complexity : O(n^2)
#Space Complexity : O(n)
#The code runs fine as it supposed to be
#I had to re-read the algorithm since its little bit complex for me to understand

# Python program for implementation of Quicksort Sort
  
# give you explanation for the approach
def partition(arr,low,high):
    pivot = arr[high] #assigning the value at high index as pivot
    i = (low-1) #keeping the smaller element aside from the list
    for j in range(low,high):
        if arr[j] < pivot: #if pivot is greater than the element then
            # reassign the smaller element and swap the smaller element with the current one
            i = i+1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
    #swapping the smaller element pointer with the pivot
    # so that it create a partition in such a way that
    # all the elements smaller than the pivot stays on left side of it
    # and the rest on the right side of it
    temp = arr[i+1]
    arr[i+1] = arr[high]
    arr[high] = temp

    #return the partition index
    return i+1

# Function to do Quick sort 
def quickSort(arr,low,high):
    if low<high:
        part = partition(arr,low,high) #get the partitioning index
        quickSort(arr,low,part-1) #recurssively sort the left hand side of the list
        quickSort(arr,part+1,high) #recurssively sort the right hand side of the list
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
