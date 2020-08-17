# Python program for implementation of Quicksort Sort 
  
# Similar to merge sort.
# Partition the arrays into two halves, and sort them.
# Avg. Time oomplexity - O(nlogn) -> worst case - O(n^2)
# Space cmplexity - O(1)
def partition(arr,low,high):
    #write your code here
    pivot = arr[high] # initialize pivot element to the last element in the array.
    j = low-1 		  # second pointer which will be incremented only if the element value is less than the pivot. will help shift elements greater than pivot to the right.
   
    for i in range(low, high):
    	if arr[i] <= pivot:
    		j+=1
    		#swap
    		arr[i], arr[j] = arr[j], arr[i]

    # swap pivot element with the jth element.
    # this puts the pivot element to the correct location.
    arr[j+1], arr[high] = arr[high], arr[j+1]
    return j+1

# Function to do Quick sort 
def quickSort(arr,low,high): 
	if low<high:
		#write your code here
		pivotloc = partition(arr,low,high)
		quickSort(arr,low,pivotloc-1)
		quickSort(arr,pivotloc+1,high)

  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
print ("Original array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
