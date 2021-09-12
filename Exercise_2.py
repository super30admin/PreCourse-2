# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
"""
This is a sorting technique which is very similar to that of merge sort.
Here we select a pivot index, and try to find a perfect place for it to sit.
This we do by using two pointers and by passing those 2 pointers we make
try ti udentify a exact place where all the left side of that position are
smaller than that of the pivot value and right side of that index are greater
to that of pivot value. The iteratively consider right side, left side of the 
index and perform the same values.
"""
def partition(array,start,end):
    pivot_index = start
    print(pivot_index,array)
    pivot = array[pivot_index]
      
    while start < end:
          
        while start < len(array) and array[start] <= pivot:
            start += 1
              
        
        while array[end] > pivot:
            end -= 1
          
        if(start < end):
            array[start], array[end] = array[end], array[start]
      
    array[end], array[pivot_index] = array[pivot_index], array[end]
     
    return end  

def quickSort(array,start,end): 
    
    if (start < end):
        p = partition(array,start, end)
        
        quickSort(array,start, p - 1)
        quickSort(array,p + 1, end)
    return array
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
arr = quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
