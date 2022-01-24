# Python program for implementation of Quicksort Sort 
  
# Approach taken to solve quick sort
"""
This program assumes the last element as pivot element
There are 2 variables initialized as i and j.
As i crosses j or j crosses i we need to stop the iteration
It compares whether i greater than pivot and j less than pivot. If this is the scenario, then swap them.
Till that time increment i and decrement j.
At some moment i (index) and j (index) will cross each other.
As soon as they cross each other check for i less than pivot or not? if i greater than pivot then swap them.
This will give the index position of sorted element. This is the process of "partition".
(which is all smaller element to the left of sorted element and all greater element to the right of sorted element.)
Do it recursively for the left side of array and right side of array.

space complexity:----> average case --> O(logn)
                        worst case--> O(n)

time complexity :-----> best case ----> O(nlogn)
                        average case --> O(nlogn)
                        worst case--> O(n^2)
"""
def partition(arr,low,high):
    pivot = arr[high]
    i = low
    j = high - 1
    while(i < j):
        while(i < high and arr[i] < pivot):
            i = i+1
        while (j > low and arr[j] > pivot):
            j = j-1
        if (i <j):
            arr[i],arr[j] = arr[j],arr[i]
    if arr[i] > pivot :
        arr[i],arr[high] = arr [high], arr[i]
    return i


    #write your code here
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if (low < high):
        p = partition (arr,low, high)
        quickSort(arr,low,p-1)
        quickSort(arr,p+1,high)
    #write your code here
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
