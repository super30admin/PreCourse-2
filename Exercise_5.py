# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
    i = ( low-1 )         # index of smaller element
    pivot = arr[high]     # pivot
  
    for j in range(low , high):
  
        # If current element is smaller than or
        # equal to pivot
        if   arr[j] <= pivot:
          
            # increment index of smaller element
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
  
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 )
    
  
    

def quickSortIterative(arr, l, h):
    #create a stack
    size=h-l+1
    stack=[0]*(size)
    
    #intialize top
    top=-1
    
    #push inital values of l and h
    top=top+l
    stack[top]=l
    top=top+l
    stack[top]=h
    
    #keep popping stack while is non empty
    while top >=0:
        #pop h and l
        h=stack[top]
        top=top-1
        l=stack[top]
        top=top-1
        
        #set pivot element
        p=partition(arr,l,h)
        #if the p is lesser than l, push them towards left
        if p-1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1
         #if the p is greater than h, put them towards right of pivot
        if p + 1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h
    
  
