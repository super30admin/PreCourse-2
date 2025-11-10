# Python program for implementation of Quicksort Sort 
#TC is O(n^2) in the worst case (wrong pivot selection) and o(n log n) in the average of best case
#SC is o(n)
  
# give you explanation for the approach
def partition(arr,low,high):
    p = arr[low]
    i = low + 1
    j = high
    while True:
        while i <= j and arr[i] <= p: #shifts all the elements less than pivot to left
            i += 1
        while i <= j and arr[j] >= p: #shifts all the elements greater than pivot to right
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i] #shifting done here
        else:
            break
    arr[low], arr[j] = arr[j], arr[low] #swaping of pivot and the jth element, point where pivot is correctly placed
    return j
  
# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high:
        pivot = partition(arr, low, high) #calls for the position of pivot
        quickSort(arr, low, pivot - 1) #recusrive call ofor left
        quickSort(arr, pivot + 1, high) #recusrive call on right
     
    #write your code here
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
