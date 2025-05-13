# Python program for implementation of Quicksort Sort 

""" 
Time Complexity:
partition : O(n)

quicksort : This function evenly divides the array into two parts and hence the recursive depth of the binary tree formed is log(n) 

Total Complexity: O(nlogn)

Worst Case: When the pivotal element is the lowest element or the highest element, then the quickSort function divides the array unevenly and the recursive depth might exceed until O(n),
which makes the worst case time complexity to be O(n^2)


Space: 

sort_using_arrays: Is the implementation of the quickSort using an auxiallary array(s) hence it makes the space complexity to be O(n)

parition: Is an in-place implementation so it makes the space complexity to be O(1)

quickSort: O(logn) as it divides the arrays in the recursive call 
"""
  
# give you explanation for the approach
def sort_using_arrays(arr, low, high):
    if low>=high or len(arr)==1:
        return arr
    pivot = arr[high]
    lessThanPivot = [ x for x in arr if x<pivot]
    greaterThanPivot = [x for x in arr if x>pivot]
    equalToPivot = [x for x in arr if x==pivot]
            
    return perform_sort(lessThanPivot, low, len(lessThanPivot)-1) + equalToPivot + perform_sort(greaterThanPivot, 0, len(greaterThanPivot)-1)

def partition(arr, low, high):
    if low == high:
        return arr 
    if low > high: 
        return 

    i = low-1 
    j = low 
    pivot = arr[high]
    while j <= high - 1:
        if arr[j] < pivot:
            i+=1
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp 
        j+=1
        
    temp = arr[i+1]
    arr[i+1] = arr[high] 
    arr[high] = temp 
    
    return i+1
            
# Function to do Quick sort 
def quickSort(arr, low, high):
    if low<high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
    

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
