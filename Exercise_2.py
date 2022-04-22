# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach

'''
Approach:
1. Used Lomuto Algorithm for partitioning
2. First we will partition the list
3. During partitioning we have to decide the pivot. Here my pivot will be arr[high]
4. In partitioning, I have created 2 ptr's
    4.1 jth ptr for "R2" region. All elements in R2 region will be greater than "pivot".
    4.2 ith ptr for "R1" region. All elements in R1 region will be less than "pivot".
    4.3 Our initial partition will look like following [<---R1--->,<---R2--->,PIVOT]
    4.4.Will will swap the pivot with 1st element of R2 region. Now our list will look as follows
        [<---R1--->,PIVOT,<---R2--->]
    4.5 Our partition finction will return the pivot index
5. Will will again perform quick sort on the lhs of the pivot and rhs of the pivot
6. Our quick-sort and partition function will be called recursively till our array is not sorted
7. Time Compexity is 0(nlogn)
'''
# Use LOMUTO Algo
def partition(arr,low,high):  
    
    # 1. Set pivot
    pivot = arr[high]
    
    
    # For region R2 i.e. values greater than 'pivot'
    j = low
    
    # For region R1 i.e. values less than 'pivot'
    i = j - 1
    
    
    # Perform Iteration check
    while j != high:
        
        if arr[j]<pivot:
            # Add to R1
            
            #1. Perform swap
            arr[i+1], arr[j] = arr[j], arr[i+1]
            
            #2. Increment i counter
            i+=1
        
        # For other case simply increase counter of j 
        # It will be added to R2 region
        j+=1
        
        continue
    
    # Adjust the pivot
    arr[i+1],arr[high] = arr[high], arr[i+1]
    
    # Return the pivot index
    return i+1    
    

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    if high <= low:
        # We have only 1 element
        return
    
    #write your code here
    # 1. Perform partition
    pivotIndex = partition(arr, low, high)
    
    # Quick Sort LHS of the list
    quickSort(arr, low, pivotIndex-1)
    
    # Quick Sort RHS of the list
    quickSort(arr, pivotIndex+1, high)
    
    return arr

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
print(quickSort(arr,0,n-1)) 

print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 

 

