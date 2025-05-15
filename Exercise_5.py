# Time Complexity: Best and Avg: n log(n), Worst: O(n^2) (very likely for o(n^2) as we are doing median of three pivot), n is the no.of elements in the list, 
# Space Complexity: log(n)

# Python program for implementation of Quicksort

def get_median_index(arr, low, high):
    mid = (low + high) // 2
    
    number_1, number_2, number_3 = arr[low], arr[mid], arr[high]
    
    if (number_1 - number_2) * (number_3 - number_1) >= 0:
        return low
    elif (number_2 - number_1) * (number_3 - number_2) >= 0:
        return mid
    else:
        return high

def partition(arr,low,high):
  
  
    #write your code here
    median_index = get_median_index(arr, low, high)
    
    # move median_index to first
    arr[median_index], arr[low] = arr[low], arr[median_index]
    
    i = low + 1
    j = high
    pivot = arr[low]
    
    while i <= j:
        
        while i <= j and arr[i] <= pivot:
            i += 1
        
        while i <= j and arr[j] >= pivot:
            j -=1
            
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -=1
    
    arr[low], arr[j] = arr[j], arr[low]
    return j
    


def quickSortIterative(arr, l, h):
  #write your code here
  
  stack = []
  stack.append((l, h))
  
  while len(stack):
    low, high = stack.pop()
    if low < high:
        partition_index = partition(arr, low, high)
        stack.append((low, partition_index - 1))
        stack.append((partition_index + 1, high))
    

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5]
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 