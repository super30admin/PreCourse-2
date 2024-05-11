"""  
 
 Time Complexity : worst case is O(n^2) Average cases is O(nlogn)
 Space Complexity : worst case is O(n) Average cases is O(nlogn) (space is calculated on call stack size)
 Did this code successfully run on Leetcode : Yes
 Any problem you faced while coding this : No


 Your code here along with comments explaining your approach :
 First we're checking the left and right boundaries and if they fall in between them then we're taking pivot as high index element
 and we're checking if any element is smaller or equal to pivot if yes then we're incrementing i which is nothing but the least index where
 we previously left i.e. initially low and swapping the ith index to jth index. We're repeating this process from low to high and after that we're swapping
 the high with the i+1 index and return i+1 as the partion done based on this. Now in the next subsequent calls we'll split the left array before partition and
 right array after partition and repeat the same process of finding the pivot until we reach the end. 
 
 """
 
 # Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    #write your code here
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i+1], arr[high] = arr[high], arr[i+1]
    
    return i+1
    


# Function to do Quick sort 
def quickSort(arr,low,high): 
    #write your code here
    if low < high:
        pivot = partition(arr, low, high)

        quickSort(arr, low, pivot-1)
        quickSort(arr, pivot+1, high)


  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
