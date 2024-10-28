# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    #write your code here
    # i, j = low - 1, low

    # while j < high:
    #     if arr[j] < arr[high]:
    #         i+=1
    #         arr[i], arr[j] = arr[j], arr[i]
    #     j+=1

    # arr[i + 1], arr[high] = arr[high], arr[i + 1]
    # return i
    pivot = arr[high]
    i, j = low, high
    while i < j:
        while arr[i]<= pivot and i < high:
            i += 1
        
        while arr[j]>= pivot and j > -1:
            j -= 1
        
        if i<j: arr[i], arr[j] = arr[j], arr[i]

    arr[high], arr[i] = arr[i], arr[high]
    return i

# Function to do Quick sort 
def quickSort(arr,low,high): 
    #write your code here
    if low < high:
        parti = partition(arr,low,high)
        quickSort(arr, low, parti-1)
        quickSort(arr, parti + 1, high)

  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
