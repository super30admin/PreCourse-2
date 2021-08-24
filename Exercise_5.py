# Python program for implementation of Quicksort
  
#TimeComplexity: O(n log n)
#SpaceComplexity: O(n)

def partition(arr, l, h):
    
    #set last element as pivot
    pivot = arr[h]
    #keep track of the index of swaps when the element is smaller than pivot element
    small_iter = l-1
    
    #for all element before pivot element
    for i in range(l,h):
        #if the element is smaller take it to the front of array else do nothing
        if arr[i]<pivot:
            small_iter += 1
            arr[small_iter], arr[i] = arr[i], arr[small_iter]
    #place the pivot element just after the element swapped as they are smaller
    #we obtain correct index for pivot element
    arr[small_iter + 1], arr[h] = arr[h], arr[small_iter + 1]
    
    #return the partition index where we placed the pivot element
    return small_iter+1
  


def quickSortIterative(arr, l, h):
    #create a stack
    stack = [0]*len(arr)
    top_of_stack = -1
    
    #push l and h
    top_of_stack += 1
    stack[top_of_stack] = l
    top_of_stack += 1
    stack[top_of_stack] = h
    
    while top_of_stack > -1:
        
        #remove l and h
        h = stack[top_of_stack]
        top_of_stack -= 1
        l = stack[top_of_stack]
        top_of_stack -= 1
        
        #get partition index
        p = partition(arr, l, h)
        
        #if there are small element push left index
        if p-1>l:
            top_of_stack += 1
            stack[top_of_stack] = l
            top_of_stack += 1
            stack[top_of_stack] = p-1
        
        #if there are larger elements push right index
        if p+1<h:
            top_of_stack += 1
            stack[top_of_stack] = p+1
            top_of_stack += 1
            stack[top_of_stack] = h
    

