# Python program for implementation of Quicksort Sort
# give you explanation for the approach
def partition(arr,low,high):
    #write your code here
    '''
    :param arr: a list or segment of list
    :param low: start index
    :param high: end index
    :return: pivot
    '''
    ptr=low
    pivot=high
    for i in range(low,high):
        if arr[i]<arr[pivot]:
            arr[i], arr[ptr] = arr[ptr],arr[i] # swap
            ptr += 1
    arr[ptr] , arr[pivot] = arr[pivot], arr[ptr]
    return ptr
# Function to do Quick sort 
def quickSort(arr,low,high):
    #write your code here
    if low < high:
        p=partition(arr,low,high)
        quickSort(arr,low,p-1)
        quickSort(arr,p+1,high)

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1)
print ("Sorted array is:")
for i in range(n): 
    print ("%d" %arr[i])
  
 
