# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach:
# i goes through the whole array and it stops when arr[j] > pivot
# so it pointes the larger than pi value and waiting to be swapped 
# with arr[j] when arr[j] is <= pi, eventually will put pivot
# at the right postion in the array so that 
#left tp pi is less than pi, pi to right is greater than pi 

#time complexity:O(n*logn)
def partition(arr,low,high):
 pivot = arr[high]
 i = low  - 1 #-1
#[1,3,15,9]
#low = 0 high = 3
 for j in range(low, high):
    # meaning arr[j] is at right position in the array
    #so we increase i to find next greater than pi value
    if arr[j] <= pivot:
        i = i + 1 # i = 1 arr[j] = 1
        (arr[i], arr[j]) = (arr[j], arr[i]) 
        # i = 0, j = 0 (1,1) = (1,1)
        #second pass: j = 1, i = 1, (3,3) = (3,3)
        #third pass: j =2, i = 1
        
        # loop ends

 (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])
 # (arr[1+1], arr[3]) = arr[3], arr[2]
 #(15,9) = (9,15) -> [1,3,9,15]
 return i + 1
    
        
  
  
# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here
    if low < high:
        pivot = partition(arr,low, high)
        quickSort(arr, low, pivot -1)
        quickSort(arr,pivot + 1, high )

  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
