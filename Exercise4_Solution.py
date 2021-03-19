#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Python program for implementation of MergeSort 

# Its also a divide and conquer, recursive approach algorrithm


def mergeSort(arr):
  
  #write your code here
    
    if len(arr) > 1:
        mid = len(arr)//2
        
        L = arr[:mid]
        R = arr[mid:]

#       Lets keep dividing the array till we have just one element in the each list
        mergeSort(L)
        mergeSort(R)
        
        # Setting up pointers for each of the list
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1 
            k+= 1
        while i < len(L):
            arr[k] = L[i]
            i+= 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            
        
  

# Code to print the list 
def printList(arr): 
    
    #write your code here
    for i in range(len(arr)):
        print(arr[i],end=" ")
    print ()
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 

