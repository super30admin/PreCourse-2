# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
#time complexity: O(nlogn)
#space complexity: O(n)
def partition(arr,low,high):
    '''make a pivot element, compare it with low and high values and swap array 
      such that elements smaller than or equal to the pivot are placed to its left,
      and elements greater than the pivot are placed to its right.
      and returns the partitioning inde
    '''
  
    #write your code here
    pivot = arr[low]  # Choosing the pivot as the first element
    i = low + 1 
    
    for j in range(low + 1, high + 1):
        if arr[j] <= pivot:
            # Swap arr[i] and arr[j]
            arr[i], arr[j] = arr[j], arr[i]
            # Increment index of smaller element
            i += 1
    
    # Swap pivot with the last element smaller than or equal to it
    arr[low], arr[i - 1] = arr[i - 1], arr[low]
    #returning the partitioning array 
    return i - 1
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    #get the partition index from partition and sort array
    #write your code here
    if low < high:
        # pi is partitioning index
        pi = partition(arr, low, high)
        
        # recursive call to sort elements 
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  

  #did not solve on leet code
  #due to indentation error i was not able to swap pivot elements with low

 
