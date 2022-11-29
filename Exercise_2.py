# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
# from socket import J1939_NLA_BYTES_ACKED


def partition(arr,low,high):
    #write your code here
    pivot = arr[low] #Choose the first element as pivot
    i = low #i will initially point to the low index
    j = high #j will initially point to the high index
    while i<j: #While i pointer does not become greater than the low pointer
        while(arr[i] <= pivot) and (i < len(arr)-1): #Keep incrementing i until an element greater than the pivot is found and as long as i is within the array indices
            i += 1
        while(arr[j] > pivot) and (j > 0): #Keep decrementing j until an element less than the pivot is found and as long as j is within the array indices
            j -= 1
        if i<j: #Swap the elements at indices i and j if i < j so that the greater element is moved towards the right and smaller element towards the left
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
    temp = arr[low] #Swap the element at the jth index with the pivot as this will be the sorted position for the pivot. The input array will now be divided into 2
    arr[low] = arr[j]
    arr[j] = temp
    return j #Return the paritioning index

# Function to do Quick sort 
# Quick Sort uses the concept of a pivot. Say the first element is the pivot. In every iteration, all the elements less than the pivot are moved towards its left and the elements greater than the pivot are moved towards its right. Two pointers i and j are used. In every iteration, i is incremented until an element greater than the pivot is found, j is decremented until an element less than the pivot is found. Element at i and j are swapped. In the element, pivot is swapped with the element at the jth index.
def quickSort(arr,low,high):
    
    #write your code here
    if low < high: #If it is a valid array
        j = partition(arr, low, high) #Partition the array by using a pivot. All the elements towards its left should be less than the pivot and all the elements towards its right should be greater than the pivot. The array will be partitioned into two separate portions to conquer.
        quickSort(arr, low, j) #Run quick sort on the left side of the array
        quickSort(arr, j+1, high) #Run quick sort on the right side of the array
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
