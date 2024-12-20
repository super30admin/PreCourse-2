# Python program for implementation of Quicksort

# This function partitions the array and places the pivot in its correct position
def partition(arr, l, h):
    pivot = arr[h] 
    i = l - 1  

    for j in range(l, h):  
        if arr[j] <= pivot:  
            i += 1  
            arr[i], arr[j] = arr[j], arr[i]  
            
    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return i + 1  


def quickSortIterative(arr, l, h):
    
    stack = []
    stack.append((l, h)) 

    while stack:
        start, end = stack.pop()
        
        pivot_index = partition(arr, start, end)

        if pivot_index - 1 > start:
            stack.append((start, pivot_index - 1))
        
        if pivot_index + 1 < end:
            stack.append((pivot_index + 1, end))

if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is:", arr)
    quickSortIterative(arr, 0, len(arr) - 1)
    print("Sorted array is:", arr)