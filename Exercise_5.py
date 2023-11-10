# Python program for implementation of Quicksort

# This function is same in both iterative and recursive

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
def partition(arr, l, h):
    
    # ith index for region 1
    # jth index for region 2
    # pivot is arr[h]
    
    j = l
    i = j-1
    
    while j != h:
        
        if arr[j] < arr[h]:
            arr[i+1], arr[j] = arr[j], arr[i+1]
            i+=1
        
        j+=1
        continue
    
    arr[i+1],arr[h] = arr[h], arr[i+1]
    
    return i+1

def quickSortIterative(arr, l, h):
    if l>=h:
        return arr
    
    # Perform Partition
    pIndex = partition(arr, l, h)
    
    # Quick lhs of the partition index
    partition(arr, l, pIndex-1)
    
    # Quick rhs of the partition index
    partition(arr, pIndex+1, h)
    
    return arr
    
arr = [12, 11, 13, 5, 6, 7]
print(quickSortIterative(arr,0,len(arr)-1))