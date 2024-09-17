# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach

def swap(arr,i,j):
    arr[i], arr[j] = arr[j], arr[i]

def partition(arr,low,high):
    pivot = arr[low]
    i = low 
    j = high
    while i < j:
        while  arr[i] <= pivot and i <= high - 1 :
            i += 1
        while arr[j] > pivot and j >= low + 1:
            j -= 1
        if i < j:
            swap(arr,i , j)

    swap(arr, low, j)
    return j
  

  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high:
        partition_index = partition(arr, low, high)
        quickSort(arr,low,partition_index-1)
        quickSort(arr,partition_index + 1, high)
 


    
    
    
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:", arr) 
# for i in range(n): 
#     print ("%d" %arr[i]), 
  
 
#Explaination:
# 1. we find the pivot
# 2. we get the parition element
# 3. then we sort the left side and the right side recursively
# 4. for the partition function we use two pointers i and j and take them i = low and j = high
# 5. we move the left pointer to the right until arr[i] <= pivot
# 6. we move the right pointer to the left until arr[j] > pivot
# 7. we swap the elements
# 8. we return the partition index

