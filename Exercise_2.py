"""
Time complexity for:
partition of elements = n
quicksort = O(logn)

Space complexity for quicksort = O(n)
"""

def partition(arr,low,high):
    #write your code here
    pivot = arr[high]
    ip = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            ip += 1
            arr[j], arr[ip] = arr[ip], arr[j]
    arr[ip+1], arr[high] = arr[high], arr[ip+1]
    return ip+1


def quickSort(arr,low,high):
    #write your code here
    if low < high:
        partition_index = partition(arr, low, high)
        quickSort(arr, low, partition_index - 1)
        quickSort(arr, partition_index + 1, high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i])

print("*"*10)
arr = [1, 6, 56, 9, 1, 53] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i])