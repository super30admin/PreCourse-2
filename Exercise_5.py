# Python program for implementation of Quicksort

def partition(arr, start, end):
    pivot_index = start
    #pivot = arr[pivot_index]
    print("\nBefore this step: ", arr)
    while start < end:
    
        while start < len(arr) and arr[start] <= arr[pivot_index]:
            start += 1
        while arr[end] > arr[pivot_index] and end >= 0:
            end -= 1
        if start < end:
            arr[start], arr[end] = arr[end], arr[start] 
        print("Internal Sorting Step- ",arr)
    arr[pivot_index], arr[end] = arr[end], arr[pivot_index]
    print("Swap Step- ",arr)  
    print("Partition Index", end)
    
    return end 

def quickSortIterative(arr):
    stack = [(0, len(arr) - 1)]  # stack with the initial bounds
    print(stack)
    while stack:
        l, h = stack.pop()  # Get the bounds
        pi = partition(arr, l, h)  
        
        # left side of the pivot
        if pi - 1 > l:
            stack.append((l, pi - 1))  
            

        # right side of the pivot
        if pi + 1 < h:
            stack.append((pi + 1, h)) 
            
def printList(arr): 
    print(" ".join(map(str, arr)))  

# Driver code to test the above code  
arr = [12, 11, 13, 5, 6, 7]  
print("Given array is: ", end="\n")  
printList(arr)
quickSortIterative(arr) 
print("\nSorted array is: ", end="\n") 
printList(arr) 
