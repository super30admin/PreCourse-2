# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach

#Time Complexity : O(n log n)
# Space Complexity : O(log n)
# Did this code successfully run on Leetcode : yes
# Any problem you faced while coding this :
        
# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here

    if low < high:
    	# Find a pivot element and put it in right place where left elements are less than pivot 
        # and right elements are greater than pivot
	    pi = partition(arr,low,high)
	    quickSort(arr,low,pi-1)  # apply quick sort to the left set of elements to pivot
	    quickSort(arr,pi+1,high) # apply quick sort to the right set of elements to pivot
          


def partition(arr,low,high):
  
  
    #write your code here
    pivot_index = low
    pivot = arr[pivot_index]

    while low < high: # do this only until low and high cross
            # compare low with pivot and increment until low is greater than pivot
            while low < len(arr) and arr[low] <= pivot:
                  low += 1
            # compare high with pivot and decrement until high is less than pivot
            while arr[high] > pivot:  
                  high -= 1
            # swap low and high until they cross
            if low < high:
               swap(arr,low,high)

    # swap pivot and high once low and high crosses 
    swap(arr,pivot_index,high)       

    return high 


def swap(arr,pivot_index,high):

    if pivot_index!=high:
	    temp = arr[pivot_index]
	    arr[pivot_index] = arr[high]
	    arr[high] = temp  

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 

