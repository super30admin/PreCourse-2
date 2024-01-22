# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
#Time Complexity: O(n logn)
#Space Complexity: O(1) + O(n) we are not using any variables but we are using some stack space. 
def partition(arr,low,high):    
    #write your code here
    i,j = low, high
    pivot = arr[low]
    #set pivot, and also set pointer from left(i) and right(j)
    while i < j:
    #Continue till until i and j do not cross each other
        while(arr[i] <= pivot and i<=high - 1):
            #Move i by 1 index to right if element at i is smaller than pivot and i less than high
            i+=1
        while(arr[j] > pivot and j >=low + 1):
            #Move j by 1 index to left if element at j is greater than pivot and j greater than low
            j-=1
        if i < j:
            #Swap the elements at i and j only if i is less than j
            arr[i],arr[j] = arr[j],arr[i]
    #Swap the pivot element with element at index j
    arr[low], arr[j] = arr[j], arr[low]
    # j is the partitioning point we return j
    return j
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here
    if low < high:
        #Get the index at which we can divide the array into two parts.
        partitioningIndex = partition(arr, low, high)
        #Recursively sort the element to left of partitioning index.
        quickSort(arr, low, partitioningIndex - 1)
        #Recursively sort the element to right of partitioning index.
        quickSort(arr, partitioningIndex + 1, high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
