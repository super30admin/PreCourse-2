# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(start,end,elements):
    #write your code here
    pivot_index = start
    pivot = elements[pivot_index]
    
    while start < end:
        
        while start < len(elements) and elements[start] <= pivot:
            start += 1
        
        while elements[end] > pivot:
            end -= 1
        
        if start < end:
            elements[start], elements[end] = elements[end], elements[start]
            print("Switch: ", elements)
    
    elements[end], elements[pivot_index] = elements[pivot_index], elements[end]
    print("Step: ", elements)
    return end
  

# Function to do Quick sort 
def quickSort(elements,start,end): 
    #write your code here
    if start < end:
        pi = partition(start, end, elements)
        # Sort elements before and after the partition index
        quickSort(elements, start, pi - 1)
        quickSort(elements, pi + 1, end)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
