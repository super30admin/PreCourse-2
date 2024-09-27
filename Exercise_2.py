# -*- coding: utf-8 -*-
"""
Python implementation of QuickSort

Time Complexity : O(nlogn) where n is the length of the array
"""


# This function takes last element as pivot, places 
# the pivot element at its correct position in sorted 
# array, and places all smaller (smaller than pivot) 
# to left of pivot and all greater elements to right 
# of pivot 
def partition(arr,low,high): 
    i = (low-1)         # smallest element stored in i 
    pivot = arr[high]     #pivot holds the largest element in the array
  
    for j in range(low,high): # run though the entire array (from low to high)
  
        # If current element is smaller than the pivot 
        if arr[j]<pivot: 
                   
            i = i+1 #move to the next element in the array till pivot position
            arr[i],arr[j] = arr[j],arr[i] #swap the consecutive elements
  
    arr[i+1],arr[high] = arr[high],arr[i+1] #swap the next element in the array with the largest 
    return (i+1) #return the index of partitioned element
  

  
# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high: 
  
        pi = partition(arr,low,high) #store the index of partitioned element
  
        quickSort(arr, low, pi-1) #Sort before pivotted element
        quickSort(arr, pi+1, high) #Sort from pivotted element till the end of array
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5,80,56,100,9] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): print (arr[i]) 