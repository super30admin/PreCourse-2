# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 

# Time Complexity : O log(n)
#Space Complexity : O(1)
#Did this code successfully run on Leetcode : yes
#Any problem you faced while coding this : I never used here partition method. Partition method is difficult to understand
def quicksort(sequence):
    length = len(sequence) #check array length
    if length <= 1:  # length 1 return value
        return sequence
    else:
        pivot = sequence.pop() # if not then pop last element meance choose last element as pivot
    
    items_small = [] # Create small array if pivot is less than itmes in sequence
    items_big = []
    
    for x in sequence:
        if x > pivot:
            items_big.append(x)
        else:
            items_small.append(x)
    
    return quicksort(items_small) + [pivot] + quicksort(items_big) #return small array pivot and large element array
    
    

print(quicksort([10, 7, 8, 9, 1, 5]))