# Python program for implementation of Quicksort Sort 
  
#Time Complexity: O(nlogn)
#Space Complexity: O(logn)

def swap(a,b,element):
    if a!=b:
        tmp=element[a]
        element[a]=element[b]
        element[b]=tmp
         
def partition(arr,low,high):
    pivot_index=low
    pivot=arr[pivot_index]

    while low<high:
        while low<len(arr) and arr[low]<=pivot:
            low +=1
        while arr[high]>pivot:
            high -=1
        if low<high:
            swap(low, high, arr)
    swap(pivot_index, high, arr)
    return high

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low<high:
        pi = partition(arr, low, high)
        quickSort(arr,low,pi-1)
        quickSort(arr,pi+1,high)

  

if __name__=='__main__':
    # Driver code to test above 
    arr = [10, 7, 8, 9, 1, 5] 
    n = len(arr) 
    quickSort(arr,0,n-1) 
    print(arr) 
  
 
