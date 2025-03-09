# Time Complexity: O(n log n)
# Space Complexity: O(log n)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No
'''
my output:
komalbhavake$ python3 Exercise_2.py
Sorted array is:
1
5
7
8
9
10
'''
# Your code here along with comments explaining your approach
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
    
    arr[i + 1], arr[high] = arr[high] , arr[i + 1]
    return i + 1

# Function to do Quick sort 
def quickSort(arr,low,high):    
    #write your code here
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
