# Python program for implementation of Quicksort Sort 

#Time Complexity :BestCase,AverageCase- O(n log n) the array is divided in half each time.
#                 WorstCase-O(n^2) Happens when Partitions are unbalanced.

#Space Complexity : BestCase,AverageCase-O(log n)  - Recursive calls are balanced and shallow.
#                   WorstCase  - O(n) Happens when recursion goes deep due to unbalanced partitions.
#Did this code successfully run on Leetcode :  Yes
# give you explanation for the approach
def partition(arr,low,high):
#write your code here
    pivot=arr[high] #last element is pivot
    i=low-1  #smaller element index

    for j in range(low,high):
        if arr[j]<pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i] #if the element is smaller than pivot,swap
    arr[i+1],arr[high]=arr[high],arr[i+1] #placing the pivot at correct position
    return i+1 #pivot index

# Function to do Quick sort 
def quickSort(arr,low,high):
    #write your code here
  if low<high:
        p=partition(arr,low,high)

        quickSort(arr,low,p-1) #sort left half
        quickSort(arr,p+1,high) #sort right half
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
print(*arr)
  
 
