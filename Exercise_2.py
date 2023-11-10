#  Quicksort time complexity is Best Case: O(nlog n), worst case: O(n^2)
#  Quicksort space complexity is Best Case: O(log n)
#  Python program for implementation of Quicksort Sort 
# give you explanation for the approach
def partition(arr,low,high):
    #write your code here
    #setting the pivot element 
    pivot=high
    high=high-1 
    while low<high: 
        #shifting the elements which are less than pivot element to the left 
        if arr[low]<arr[pivot]:
            low+=1
        #shifting all the elements greater than pivot to the right 
        elif arr[high]>arr[pivot]:
            high-=1
        elif arr[low]>arr[pivot]:
            arr[low],arr[high]=arr[high],arr[low]  
    #swaping the element which is less than pivot with the pivot element
    if low>=high:
        arr[low],arr[pivot]=arr[pivot],arr[low]
    return low

# Function to do Quick sort 
def quickSort(arr,low,high): 
    #write your code here
    if low<high:
        partition_pos=partition(arr,low,high)
        #left list
        quickSort(arr,low,partition_pos-1)
        #right list
        quickSort(arr,partition_pos+1,high)

  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
