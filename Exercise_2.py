# Python program for implementation of Quicksort Sort 
#  average time complexity: O(log n)
#  worst case time complexity: O(n^2)

# approach:
# initially, low is at index 0, high is at len(arr)-1
# set pivot as the first element, if element at low is lesser than pivot, increment low. if element at high is gretaer than pivot, decrement high
# when the element at low > pivot, or element at high < pivot, exit loop and swap both. when low becomes > high, end the outer loop and swap pivot and high
# high is partition index
# at this point, pivot would be at the sorted place. 
# all the elements before pivot would be less than pivot and at right would be greater than pivot

# recursively run the above while low < high.
# left array would be from low to partiton index-1 and right array would be partition index+1 to high

def partition(arr,low,high):
    pivot_index = low
    pivot = arr[pivot_index]
    while(low<high):
        while low < len(arr) and arr[low]<= pivot:
            low += 1
        while arr[high]> pivot:
            high -= 1
        if low < high:
            arr[low], arr[high] = arr[high], arr[low]
    arr[high], arr[pivot_index] = arr[pivot_index], arr[high]
    return high
    
  
  
    #write your code here
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high:
        partition_index = partition(arr, low, high) #get the partition index to partition the array
        quickSort(arr, low, partition_index-1) # sort the left partition array
        quickSort(arr,partition_index+1, high) # sort the right partition array
        
    
    #write your code here
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
