# Python program for implementation of Quicksort Sort 
  
# Time complexity - O(nlogn) - Average running time
#                  - O(n) worst case running time
# Space complexity - O(1)
# give you explanation for the approach
# Quicksort follows divide and conquer approach
# Partition using pivot and recurse

def partition(arr,low,high):
  
    pivot = arr[high]
    i = low


    for m in range(low, high):
        if arr[m] <= pivot:
            arr[i], arr[m] = arr[m], arr[i]
            i += 1
            

    arr[i] , arr[high] = arr[high], arr[i]
    return arr, i
    #write your code here
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here
    if low<high:
        arr, index = partition(arr, low, high)

        
        quickSort(arr,low,index-1)
        quickSort(arr,index+1,high)

  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
