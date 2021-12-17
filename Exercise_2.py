# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    '''Always pass valid index positions in low and high'''


    pivot = arr[low] #Since, we use first element as pivot. The placement position will be dictated by right.
                     #This is because right will end on an element smaller than pivot. Hence, we can swap that element
                     #to the beginning and maintain the orderedness of the left sub array and the right subarray.
    left = low + 1
    right = high

    while left <= right:

        while left <= high and arr[left] < pivot:
            left += 1
        while right > low and arr[right] >= pivot:  # Any implications of the equality in this condition?
            right -= 1                              # Not really. If pivot is 5. 5 can be on the right or left of the pivot.
                                                    # This equality in the incr of left or right will only decide 
                                                    # which subproblem to add this equal element to. Outcome is the same.
            
        
        if left < right: #perform swap
            arr[left], arr[right] = arr[right], arr[left]

    
    arr[low], arr[right] = arr[right], arr[low]

    return right
  
    #write your code here
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    if low >= high: # if low > high, invalid sub problem. if low == high, already solved sub problem.
        return
    idx = partition(arr, low, high)
    quickSort(arr, low, idx - 1)
    quickSort(arr, idx + 1, high)
    
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5]
print("Original Array: {}".format(arr))
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is: {}".format(arr)) 

arr = [-1,2,3,1,2,3]
print("Original Array: {}".format(arr))
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is: {}".format(arr)) 
  
 
