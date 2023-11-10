# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    
    print(arr)
    print("low=", low, "high=", high)
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1] 
    return i+1    
        

# Function to do Quick sort 
def quickSort(arr,low,high):
  size=high-low+1
  stack=[0]*size
  top=-1
  
  top+=1
  stack[top]=1
  top+=1
  stack[top]=high
  
  while top >= 0:
        high = stack[top]
        top = top - 1
        low = stack[top]
        top = top - 1

        p = partition( arr, low, high )

        if p-1 > low:
            top = top + 1
            stack[top] = low
            top = top + 1
            stack[top] = p - 1
        if p + 1 < high:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = high
  

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 

for i in range(n): 
    print ("%d" %arr[i]), 
  
 
