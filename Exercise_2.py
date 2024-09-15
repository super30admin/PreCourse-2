# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    pivot = arr[high]
    index = low-1
    for i in range(low,high):
        if arr[i]<pivot:
            index +=1
            # Swapping the large with small values
            temp = arr[index]
            arr[index]=arr[i]
            arr[i] = temp
    temp = arr[index+1]
    arr[index+1] = arr[high]
    arr[high] = temp
    return index+1

  


# Function to do Quick sort 
def quickSort(arr,low,high):
    if low<high:
        partition_index = partition(arr,low,high)

        quickSort(arr,low,partition_index-1)
        quickSort(arr,partition_index+1,high)

    

# Driver code to test above 
arr = [ 7,10, 8, 9, 1, 5]
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]),

# Complexity

# Time Complexity -   nlog(n) worst case o(n^2) if the array is already sorted
# Space Complexity - o(1) as iam  not using the extra space
