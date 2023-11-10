'''
Time Complexity: O(nlog(n))
Space Complexity: O(n)
Problem: to partition array in place
'''
# Python program for implementation of Quicksort Sort 
  
# Partioning elements in place
# last element is pivot
# used 2 pointers marking less and bigger
# values as compared to pivot
# swapped pivot with a valued from 
# greater values
def partition(arr,low,high):
    pivot = arr[high]
    i = low-1
    j = low
    while j<high:
        if arr[j] <= pivot:
            i += 1
            arr[i],arr[j]=arr[j],arr[i]
        j += 1
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1

  

# Function to do Quick sort 
def quickSort(arr,low,high):
    if low < high:
        mid = partition(arr,low,high)
        quickSort(arr,low,mid-1)
        quickSort(arr,mid+1,high)
    #write your code here
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
