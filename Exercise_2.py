"""
Exercise_2 : Quick sort.
Time Complexity : 
    Best case: O(nlogn)
    Worst Case: O(N^2)

Space Complexity : O(1) 


@name: Rahul Govindkumar_RN27JUL2022
"""

# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    
    #write your code here
    
    #Pivot as First element
    pivot = arr[low]
    
    i=low
    j= high
    
    #loop untill the pointers cross each other 
    while i < j :
        
        #to find the ith position untill the value is less than the pivot
        while  i <= j and (arr[i] <= pivot)  :
            i +=1
        
        #to find the ith position untill the value is greater than the pivot
        while i <= j and (arr[j] > pivot) :
            j -=1
        
        #Swap ith position and jth position value  if they havent crossed each other   
        if (i < j):
            arr[i], arr[j] = arr[j], arr[i]
            
        else:
            break
    
            #Swap the pivot value with the jth value
    arr[low], arr[j] = arr[j], arr[low]
    
    return j

        
  

# Function to do Quick sort 
def quickSort(arr,low,high):
    
    #write your code here
    
    if(low < high):
        
        j = partition(arr, low, high)
        
        quickSort(arr, low, j)
        quickSort(arr, j+1, high)
    
    
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
