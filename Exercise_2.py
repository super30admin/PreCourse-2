# Python program for implementation of Quicksort Sort 

# give you explanation for the approach
# Selection of Pivot  element is very important  in quicksort.
# I selected the last element as  pivot and I assigned partition pointer to divid the array into 2  halves 
# One half wil contain elements less than pivot and other more than pivot
# At first the pivot is at end  of array and then when we  comapre if current element is less  than pivot it should exist before the partition and prtition moves by one.
# If the element is greeater then it should exist  on the other side  of partition.
# At the end wee  need  to  the same  procedure for left  and right arrays that are formed recursively to sort the array.
# Time Complexity : O(nlog(n))
# Any problem you faced while coding this : No
def partition(arr,low,high):

    #write your code here
    pivot = arr[high]
    partition = low
    for i in range(low,high):
        if (arr[i] <= pivot):
            temp =  arr[i]
            arr[i] = arr[partition]
            arr[partition] = temp
            partition = partition + 1
    temp = arr[high]
    arr[high] = arr[partition]
    arr[partition] = temp
    return partition

# Function to do Quick sort 
def quickSort(arr,low,high): 
    #write your code here
    #teermination condition for recursion
    if (low >= high):
        return
    pivPos = partition(arr,low,high)
    quickSort(arr,low,pivPos-1)
    quickSort(arr,pivPos+1,high)


# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i])

