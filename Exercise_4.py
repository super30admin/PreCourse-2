'''
====== Submission Details =======
Student Name: Pavan Kumar K. N.
Email       : pavan1011@gmail.com
S30 SlackID : RN32MAY2021
=================================
'''

# 
# Python program for implementation of MergeSort

#-------------  
# Explanation:
#-------------
# MergeSort also uses the Divide and Conquer strategy.
# Divide: Divide the input array in half and obtain 2 subsequences (n -> n/2)
# Conquer: Sort the two subsequences recursively
# Combine: the individually sorted subsequences into a sorted sequence
#                         
# As opposed to Quick Sort, the main logic is implemented in the 
# combine stage rather than the divide stage. 

#-----------------
# Time Complexity:
#-----------------

# T(n) = theta(1) if n = 1, <- Constant time to return single element (sorted)
#      = 2 T(n/2) + theta (n) if n> 1 <- Recursion 

# Therefore, average case: O(n log n) <- Master theorem
# No worst or best case. 

#-----------------
# Space Complexity: 
#-----------------
# Average case: O(n) - Space inefficient. Quicksort worst case = Mergesort

def mergeSort(arr):
    # arr: Input array of "n" elements 
    # Termination condition: Array of 1 element (which is already sorted)
    if len(arr)>1:
        
        # Obtain the index of the mid element
        mid = len(arr)//2
        
        # Divide the input array into left and right with n/2 elements each
        left = arr[:mid]
        
        right = arr[mid:]
        
        # Conquer via recursion
        mergeSort(left)
        
        mergeSort(right)

        # The next stage is to Combine the sorted left and right subsequences
        
        # An example of the simplest case: left and right have 1 element each:
        # - compare element from left to element on right
        # - combine them s.t. the smallest element added to output array first

        # A non-trivial example: 
        #   Left and Right subsequences have "l" and "r" elements respectively 
        #       - Even though Left and Right are sorted, 
        #       - Combine them s.t the combined list is also sorted
        
        # Logic: 
        # Step 1: Iterate over Left (L) and Right (R). 
        # Step 2: At every step, compare each element in L with that of R
        # Step 3: If left is smaller, add to output, else add right to o/p
        # Step 4: When either L or R runs out of elements,
        #         if there are any remaining elements in the other array 
        #         add them to output.
        # Step 5: Output array is sorted.
        
        # Initialize iterators. i-> left, j-> right, k-> output array
        i = j = k = 0

        # Iterate until we run out of elements on either left or right
        while i < len(left) and j < len(right):
            
            # compare each element in L with that of R
            if left[i] < right[j]:
                
                # If left is smaller, add to output 
                arr[k] = left[i]
                
                # Increment the iterator for left since we added element
                # from left to output
                i += 1
            
            else:
                # If right is smaller, add right to o/p
                arr[k] = right[j]
                
                # Increment the iterator for right since we added element
                # from right to output
                j += 1
            
            # Increment the iterator for output at every step since we add
            # one element at each step
            k += 1

        # Check if any elements are remaining in left
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        # Check if any elements are remaining in right
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1 
  
# Code to print the list 
def printList(arr):
    print(arr)

  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
