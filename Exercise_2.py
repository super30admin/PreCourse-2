# Time Complexity: Best case = O(nlog(n)); Worst Case= O(n^2)
# Space Complexity: Best Case = O(log(n)); Worst Case= O(n)
# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
  pivot = arr[low +(high-low)//2]
  i=low-1
  j=high+1
  while True:
    while True:
       i+=1
       if arr[i]>=pivot:
          break
    while True:
       j-=1
       if arr[j] <=pivot:
          break
    if i>=j:
       return j
    
    arr[i], arr[j]=arr[j],arr[i]
    #write your code here
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low<high:
        j = partition(arr, low, high)
        quickSort(arr, low, j)
        quickSort(arr, j + 1, high)

    #write your code here
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
