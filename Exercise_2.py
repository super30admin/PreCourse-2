# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(low,high):
    #write your code here
    if low < high:
        left = low
        mid = (low + high)//2
        pivot = arr[mid]
        arr[high], arr[mid] = arr[mid], arr[high]

        for i in range(low, high):
            if arr[i] < pivot:
                arr[left], arr[i] = arr[i], arr[left]
                left += 1
        
        arr[left], arr[high] = arr[high], arr[left]
        return left
  

# Function to do Quick sort 
def quickSort(low,high): 
    #write your code here
    item = partition(low, high)

    if item:
        quickSort(low, item-1)
        quickSort(item+1, high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(0,n-1) 
print ("Sorted array is:", arr)

# for i in range(n): 
#     print ("%d" %arr[i]), 
  
 
