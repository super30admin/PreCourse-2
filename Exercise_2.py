'''
====== Submission Details =======
Student Name: Pavan Kumar K. N.
Email       : pavan1011@gmail.com
S30 SlackID : RN32MAY2021
=================================
'''

# Python program for implementation of Quicksort Sort 

#-------------  
# Explanation:
#-------------

# Quicksort uses the divide and conquer paradigm
# Three step process:

# Step 1 (Divide): Partition (rearrange) the input array A[p..r] 
#         s.t A[p..q-1] and A[q+1, r] are two subarrays where, 
#         each element of A[p..q-1] <= each element of A[q+1, r]
#         compute q as part of partitioning

# Step 2 (Conquer): Sort A[p..q-1] and A[q+1..r] by recursive calls

# Step 3 (Combine): Subarrays are sorted and A[p..r] will be sorted

# The Partition function 
# It rearranges the array s.t 
# Elements to the left of the pivot are <= pivot
# Elements to the right of the pivot are > pivot
# Pivot element is at the partition index
# returns the index of partition or the "pivot" element

# There can be different strategies to select pivot:
# - rightmost element (as done in this implementation)
# - leftmost element
# - random element 
# - median

# Time Complexity:
# Best case: O(nlogn)
# Average case: O(nlogn)
# Worst case: O(n^2) - Input = sorted list


def partition(arr,low,high):
    # Pseudocode
    # partition(A, p, r)
    #   x = A[r]  <- x: "pivot" element
    #   i = p-1 <- i: index of rightmost element on the left side 
    #                 of the pivot (aka partition index)
    #                 s.t all elements of A[p..i] are <= pivot (x)

    #   for j = p to r-1  <- "j": iterator to do one pass over A
    #       if A[j] <= x  <- Identified an element that's supposed 
    #                        to be at the left of the pivot
    #           i = i + 1
    #           swap A[i] with A[j] <- Swap elements 
    #   swap A[i+1] with A[r]  <- Place pivot at the partition index
    #   return i+1             <- Return the index of the pivot
    
    pivot_index = high      # Choosing the rightmost as pivot element
    i = low - 1     # Initialize the partition index, i.e., rightmost element 
#                     to the left of pivot
#                     NOTE: True partition index will be i+1
    for j in range(low, high):    #iterator to do one pass over A
        
        if arr[j] <= arr[pivot_index]:
        #This element (arr[j]) should be to the right of pivot 
            
            #Increment partition index because we will swap element <= pivot        #
            i += 1      

            #In-place swap
            arr[i], arr[j] = arr[j], arr[i] 
    
    #Place pivot at the partition index                                                            index
    arr[i+1], arr[pivot_index] = arr[pivot_index], arr[i+1] 
    
    #Return partition index at which pivot is placed
    #Now all elements to the left <= pivot <= elements to the right 
    return i+1 





# Function to do Quick sort

def quickSort(arr,low,high):
    # Pseudocode:
    # quickSort(A, p, r)
    # if p < r
    #   q = partition(A, p, r)
    #   quickSort(A, p, q-1)
    #   quickSort(A, q+1, r)

    if low < high:
        #Partition the array s.t.,
        #elements to the left partition_index are less than 
        #elements to the right of the partition_index
        #with pivot element at the partition 
        partition_index = partition(arr, low, high)

        #Recursive call to sort left side of partition
        quickSort(arr, low, partition_index-1)

        #Recursive call to sort right side of partition
        quickSort(arr, partition_index+1, high)

    # Process repeats until we get an empty subarray to the left
    # Which means list is sorted    
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 

# arr = [1, 2, 3, 4, 5, 6] #Worst case scenario
# arr = [4, 1, 3, 5, 6, 7, 2] #Best case scenario


n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
