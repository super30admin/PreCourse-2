# Python program for implementation of Quicksort  
  
# This function is same in both iterative and recursive 

def partition(arr, low, high): 
    l = low-1
    pivot = arr[high]
    for k in range(low, high):
        if arr[k]<=pivot:
            l +=1
            arr[l],arr[k] = arr[k], arr[l]
    arr[l+1],arr[high] = arr[high], arr[l+1]
    return l+1
  

def quickSortIterative(arr, l, h): 
  
    stack=[]
    stack.append(l)
    stack.append(h)
    while stack:
        h = stack.pop()
        l = stack.pop()

        i = partition(arr, l,h)
        if (i-1)> l :
            stack.append(l)
            stack.append(i-1)
        if (i+1)<h:
            stack.append(i+1)
            stack.append(h)
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr, 0, n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("% d" % arr[i]), 