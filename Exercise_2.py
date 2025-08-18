# Python program for implementation of Quicksort Sort
"""
TC: O(N^2) for worst-case
    O(NlogN) for average case
SC: O(N) (if we consider recrusion stack as a memory in worst-case)
""" 
  
# give you explanation for the approach
"""
I keep the leftmost (element @ low index) as my pivot and try to find the leftmost element which is greater than pivot
and rightmost element smaller than pivot. And when I find those, I swap those until i and j cross themselves, i.e i >= j.
This gives us the exact position (j) where the pivot element should be placed if the array is sorted.
"""
def partition(arr,low,high):
    #write your code here
    pivot = arr[low]
    i, j = low, high
    while True:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]
        i+=1
        j-=1
        
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    #write your code here
    if low < high:
        j = partition(arr, low, high) #getting the sorted index for pivot (in this case the element @ left)
        quickSort(arr, low, j)
        quickSort(arr, j+1, high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print(arr[i]) 
  
 
