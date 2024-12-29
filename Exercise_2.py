# Python program for implementation of Quicksort Sort 
  
# using the first element as the pivot partion the array and move the elements smaller to the 
# left of the array and the elements bigger than the pivot to the right. Repeat for the newly 
# created left and right sub arrays.

def partition(arr,low,high):
    pivot = arr[low]
    i,j = low + 1, low + 1
    while j <= high and j >= low + 1:
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i+=1
        j+=1
    
    arr[low], arr[i-1]= arr[i-1], arr[low]
    return i - 1
  

# Function to do Quick sort 
def quickSort(arr,low,high):
    if low <= high:
        pivot_index = partition(arr,low,high)
        quickSort(arr,low,pivot_index-1)
        quickSort(arr,pivot_index+1,high)
    return arr
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
