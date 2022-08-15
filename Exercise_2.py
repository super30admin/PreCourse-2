# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach

# Time Complexity : o(nlogn) (Average Case Complexity)
# Space Complexity : o(n)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

def partition(nums, l, r):
    # Last element will be the pivot and the first element the pointer
    pivot, ptr = nums[r], l
    for i in range(l, r):
        if nums[i] <= pivot:
            # Swapping values smaller than the pivot to the front
            nums[i], nums[ptr] = nums[ptr], nums[i]
            ptr += 1
    # Finally swapping the last element with the pointer indexed number
    nums[ptr], nums[r] = nums[r], nums[ptr]
    return ptr
 
def quickSort(nums, l, r):
    if len(nums) == 1:  # Terminating Condition for recursion. VERY IMPORTANT!
        return nums
    if l < r:
        pi = partition(nums, l, r)
        quickSort(nums, l, pi-1)  # Recursively sorting the left values
        quickSort(nums, pi+1, r)  # Recursively sorting the right values
    return nums
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
    
#Output 
# Sorted array is:
# 1
# 5
# 7
# 8
# 9
# 10
  
 
