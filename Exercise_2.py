# Python program for implementation of Quicksort Sort 
# Time complexity: O(nlogn)
# give you explanation for the approach
def partition(arr,l,h):
    #write your code here
    # i is variable which defines accurate position of pivot
    i = l-1
    # pivot is last element
    pivot = arr[h]
    # loop from low to high and swap element is smaller ( basic concept: el before pivot -> small.. el after pivot -> larger)
    for j in range(l,h):
       if arr[j]<= pivot:
           i += 1
           arr[i],arr[j] = arr[j] , arr[i]

    arr[i+1],arr[h] = arr[h],arr[i+1]
    return i+1

# Function to do Quick sort 
def quickSort(arr,low,high): 
    #write your code here
    if len(arr) == 1:
        return arr
    if low<high:
        j = partition(arr,low,high)
        quickSort(arr,low,j-1)
        quickSort(arr,j+1,high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
