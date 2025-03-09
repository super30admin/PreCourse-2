# Time Complexity: O(n log n)
# Space Complexity: O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No
'''
komalbhavake$ python3 Exercise_4.py
Given array is
12
11
13
5
6
7
Sorted array is: 
5
6
7
11
12
13

'''
# Your code here along with comments explaining your approach

# Python program for implementation of MergeSort 
def mergeSort(arr):
  #write your code here
  if len(arr) > 1:
     mid = len(arr) // 2
     left_half = arr[:mid]
     right_half = arr[mid:]
     
     mergeSort(left_half)
     mergeSort(right_half)
     
     i = j = k = 0
     
     while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
           arr[k] = left_half[i]
           i += 1
           k += 1
        
        else:
           arr[k] = right_half[j]
           j += 1
           k += 1
     while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1

     while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1
  
# Code to print the list 
def printList(arr): 
   
    #write your code here
   for i in range(len(arr)):
      print(arr[i], end ="\n")   
      print()
       
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
