# Time Complexity :
    #    Best case: O(log n)
    #    worst case: O(n^2)
#  Space Complexity : O(n)


# Python program for implementation of Quicksort Sort 

# I have implemented the quick sort algorithm using recursive approach. 
# I have added code for selecting pivot element as first, last and middle element of the array.

# For the first element as pivot element, 
# I have taken the first element as pivot element and then I have taken two pointers i and j.
# I have checked if the element at i is less than the pivot element then I have incremented i by 1.
# then if the element at j is greater than the pivot element then decremented j by 1.
# If the element at i is greater than the pivot element and the element at j is less than 
# the pivot element then swapped the elements at i and j.
# repeated these steps until i is less than j.
# Finally, swapped the element at low with the element at j and returned j.

# This partition function is called recursively from quicksort function until the 
# low  is less than the high. Once done, the array is sorted. 

  

def partition(arr,low,high):
    
    # Pivot element is the first element of the array
    pivot = arr[low]
    i = low 
    j = high
    while i < j:
        while arr[i] <= pivot and i < high:
            i += 1
        while arr[j] > pivot and j > low:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], arr[low]
    return j

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here
    if low < high:
        p = partition(arr, low, high)
        quickSort(arr, low, p-1)
        quickSort(arr, p+1, high)    
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 


    # **************************  Pivot element is the last element of the array **************************
    # pivot = arr[high]
    # i = low - 1
    # for j in range(low, high):
    #     if arr[j] < pivot:
    #         i += 1
    #         arr[i], arr[j] = arr[j], arr[i]
    # arr[i+1], arr[high] = arr[high], arr[i+1]
    # return i+1
    
    # ************************** Pivot element is the middle element of the array **************************
    # pivot = arr[(low + high) // 2]
    # i = low
    # j = high
    # while i <= j:
    #     while arr[i] < pivot:
    #         i += 1
    #     while arr[j] > pivot:
    #         j -= 1
    #     if i <= j:
    #         arr[i], arr[j] = arr[j], arr[i]
    #         i += 1
    #         j -= 1
    # return i
  
 
