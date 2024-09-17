# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
  
  
    #write your code here
    pivot = arr[low]
    left = low + 1
    right = high

    while True:
        while left<=right and arr[left]>= pivot:
            left = left + 1
        while left<=right and arr[right]<= pivot:
            right = right - 1
        if right < left:
            break
        else:
            arr[left],arr[right] = arr[right],arr[left] 
    arr[low],arr[right] = arr[right],arr[low]
    return right
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here
    if low < high:
        p = partition(arr,low,high)
        quickSort(arr,low,p-1)
        quickSort(arr,p+1,high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print (arr[i]) 
  
 
