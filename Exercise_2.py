'''
Time Complexity : O(n^2) when elements are already sorted(worst/rare cases) other than that O(nlogn).
Space Complexity : O(n) during worst case or O(logn) during average cases.
Did this code successfully run on Leetcode : I can only find #912 - sort an array. but this problem cannot be solved with quick sort - recursion. This sol results in TLE.
Any problem you faced while coding this : went thought youtube video/blog on quick sort algo for once prior to coding it out to recall.
'''
# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    i = low-1
    #choosing pivot -> here i'm choosing last.
    pivot = arr[high]

    for j in range(low,high):
        if arr[j] <= pivot:
            i+=1
            arr[j], arr[i] = arr[i], arr[j]
    
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if len(arr) == 1:
        return arr
    if low < high:
        partitionFound = partition(arr,low,high)
        quickSort(arr,low,partitionFound-1)
        quickSort(arr,partitionFound+1,high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print("%d" %arr[i])