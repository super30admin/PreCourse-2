#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Python program for implementation of Quicksort Sort 

# Code taken from https://www.youtube.com/watch?v=CB_NCoxzQnk
  
# give you explanation for the approach
def get_pivot(arr,low, high):
    middle = (high + low)// 2
    pivot = high
    if arr[low] < arr[middle]:
        if arr[middle] < arr[high]:
            pivot = middle
    elif arr[low] < arr[high]:
        pivot = low
    return pivot   

def partition(arr,low,high):  
    #write your code here
    # Partition is the base of Quick Sort algorithm.
    # It basically puts the pivot element in such a position, where the elements to the left are smaller and elements
    # to the right are larger than the pivot element
    # We will choose the median of the low, hight and the middle element as the pivot element of the array
    pivot_index = get_pivot(arr,low,high)
    pivot_value = arr[pivot_index]
    arr[pivot_index] , arr[low] = arr[low], arr[pivot_index]
    border = low
    
    for i in range(low, high +1):
        if arr[i] < pivot_value:
            border += 1
            arr[i], arr[border] = arr[border] , arr[i]
            
    arr[low], arr[border] = arr[border], arr[low]
    return border
        
    
  
# Function to do Quick sort 

def quickSort(arr,low,high):  
    #write your code here
    if low < high:

        p = partition(arr, low, high)
        quickSort(arr, low, p-1)
        quickSort(arr, p +1, high)
    
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 


# In[3]:


# Another approach

# I will take the last element as the pivot element for this approach

# Quick sort algo outperforms other sorting algos. Time complexity is O(nlogn)

# Code taken from https://www.youtube.com/watch?v=kFeXwkgnQ9U&list=PLqIUIdZ4YsSLWdAJnCLiBS9j89M1jaz09&index=1

def quick_sort(arr):
    length = len(arr)
    if length <= 1:
        return arr
    else:
        pivot = arr.pop()
        
    items_greater = []
    items_small = []
    for item in arr:
        if item >= pivot:
            items_greater.append(item)
        else:
            items_small.append(item)
    return quick_sort(items_small) + [pivot] + quick_sort(items_greater)


arr = [9,8,7,18,11,0,78,45,11,1,1,1]
print(quick_sort(arr))
            

