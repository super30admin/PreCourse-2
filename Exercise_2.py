# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach

#I will use the last element in the array as pivot point

#go through all elements and compare to pivot, sort around pivot using helper function (partition)

#keep sorting elements around pivot (each sided sorted separately) until both sides together are sorted
def partition(arr,low,high):
  
    #write your code here
    start = low - 1
    pivot = arr[high]

    for i in range(low,high):

        if arr[i] <= pivot:

            start += 1

            #swap
            temp = arr[start]
            arr[start]= arr[i]
            arr[i] = temp

    swap = arr[start + 1]
    arr[start + 1] = arr[high]
    arr[high] = swap

    return start + 1



  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here
    if len(arr) == 1:
        return arr
    if low < high:
        pivot = partition(arr, low, high)

        quickSort(arr, low, pivot - 1)
        quickSort(arr, pivot + 1, high)

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
#edited