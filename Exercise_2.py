# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
#   pivot=r+l/2
#   i=0
#   j=high-1
#   while (i<j):
#       for i in range(low,high):
#           for j in range(high, low):
#             if arr[i]>pivot & arr[j]< pivot:
#                 temp=arr[j]
#                 arr[j]=arr[i]
#                 arr[i]=temp

  # choose the rightmost element as pivot
    pivot = arr[high]

  # pointer for greater element
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1

        # swapping element at i with element at j
        (arr[i], arr[j]) = (arr[j], arr[i])
    (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])

    # return the position from where partition is done
    return i + 1

          

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    if low < high:


        pi = partition(arr, low, high)

        quickSort(arr, low, pi - 1)

        quickSort(arr, pi + 1, high)

  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
