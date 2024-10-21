# // Time Complexity : O(nlog(n)) best case(equal diviision) and O(n^2) worst case in unbalanced partitions(pivot = extremes)
# // Space Complexity : O(log(n)) due to all recusive calls
# // Did this code successfully run on Leetcode :NA
# // Any problem you faced while coding this :Faced an issue for base case since pivot can be anything.
# Found out solution in quicksort function.


# Python program for implementation of Quicksort Sort 

# give you explanation for the approach
def partition(arr,low,high):                    
    #write your code here
    i = low
    j = high - 1
    pivot = arr[high]

    while i < j:
        while i < high and arr[i] <pivot:    # i moves from left to right
            i +=1

        while j > low and arr[j] >= pivot:   # j moves from right to left
            j -= 1

        if i < j:                            # after j crosses i 
            arr[i],arr[j] = arr[j],arr[i]    # swap

    if arr[i] > pivot:                       # after i crosses pivot
        arr[i],arr[high] = arr[high],arr[i]  # swap pivot location
    
    return i

    

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here
    if low < high:                                  #recursion base case 
        pivot = partition(arr,low,high)             #return new pivot  
        quickSort(arr,low,pivot-1)                  #sort left subarray of pivot
        quickSort(arr,pivot+1,high)                 #sort right subarray of pivot

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i])
  
 
