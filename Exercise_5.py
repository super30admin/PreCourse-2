'''
====== Submission Details =======
Student Name: Pavan Kumar K. N.
Email       : pavan1011@gmail.com
S30 SlackID : RN32MAY2021
=================================
'''

# Python program for implementation of Quicksort

#-------------  
# Explanation:
#-------------
# Recursive calls in quicksort to store intermediate pivots
# can cause a lot of overhead.

# Instead, we can use a stack to maintain the indices of the pivot elements
# along with the lowest (l) and highest (h) indices of the intermediate arrays 
# This function is same in both iterative and recursive

#---------------------------
# Time and Space Complexity:
#---------------------------
# Same as recursive implementation.

# he only difference is that in the iterative version
# managing the stack explicitly rather than depending on the implicit stack 
# in the recursive version - which can reduce overhead for large input array

def partition(arr, l, h):
    pivot_index = h      # Choosing the rightmost as pivot element
    i = l - 1     # Initialize the partition index, i.e., rightmost element 
#                     to the left of pivot
#                     NOTE: True partition index will be i+1
    for j in range(l, h):    #iterator to do one pass over A
        
        if arr[j] <= arr[pivot_index]:
        #This element (arr[j]) should be to the right of pivot 
            
            #Increment partition index because we will swap element <= pivot
            i += 1      

            #In-place swap
            arr[i], arr[j] = arr[j], arr[i] 
    
    #Place pivot at the partition index  
    arr[i+1], arr[pivot_index] = arr[pivot_index], arr[i+1] 
    
    #Return partition index at which pivot is placed
    #Now all elements to the left <= pivot <= elements to the right 
    return i+1 


# quickSortIterative Logic: 
# Instead of recursively calling 
# quickSort(arr, l, partition_index-1) or quickSort(arr, partition_index+1, h),
# Step 1: Add the lower (l) index to stack and next the higher (h) index
# Step 2: Pop stack to get higher index first, then pop again to get lower
# Step 3: Call partition(arr, l, h) to get partition index (p) which has pivot 
# Step 4(a): If p-1 > l, treat p-1 as higher index (h), repeat Step 1
# Step 4(b): If p+1 < h, treat p+1 as lower index (l), repeat Step 1 
def quickSortIterative(arr, l, h):
    # arr: input array
    #   l: lowest index of array (start)
    #   h: highest index of array (end)
    
    # We already know what the maximum size of the stack can be:
    # Worst case, we need N = (h-l) + 1 elements
    size = h - l + 1
    
    # stack of 0s with size N
    stack = [0] * size

    # Initialize pointer to top of the stack. This holds the index of the
    # topmost element of the stack
    top = -1

    
    # Step 1: Add lower index to the stack first
    top += 1
    stack[top] = l

    # Step 1: Add higher index to the stack next
    top += 1
    stack[top] = h

    # Iterate Step 2-4 until stack is empty: termination condition
    while top >= 0:
        # Step 2: Pop top element from the stack, this is the highest index
        h = stack[top]
        top -= 1
        
        # Step 2: Pop top element again, this is the lowest index
        l = stack[top]
        top -= 1

        # Step 3: Call partition to get partition index where pivot sits
        p = partition(arr, l, h)

        # Step 4(a): If p-1 is greater than l, treat p-1 as higher index (h)
        if p-1 > l:
            # Repeat Step 1: Add lower index to the stack first
            top += 1
            stack[top] = l
            
            # Repeat Step 1: Add higher index to the stack next
            top += 1
            stack[top] = p-1

        # Step 4(b): If p+1 is less than h, treat p+1 as lower index (l), go to Step1 
        if p+1 < h:
            # Repeat Step 1: Add lower index to the stack first
            top += 1
            stack[top] = p+1
            
            # Repeat Step 1: Add higher index to the stack next
            top += 1
            stack [top] = h

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 

# arr = [1, 2, 3, 4, 5, 6] #Worst case scenario
# arr = [4, 1, 3, 5, 6, 7, 2] #Best case scenario


n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
