# Python program for implementation of MergeSort 
# Time Complexity : O(nlogn)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode :
# Any problem you faced while coding this : Implementation took some time, especially the merge function

def mergeSort(arr, low, high):
  
  #write your code here
  ''' finds the midpoint, then partitions the array based on pointers. 
  once the array is divided down to it's last element, it calls the merge function
  '''
  if (low >= high): 
    return
  mid = (low + high)//2
  mergeSort(arr, low, mid)
  mergeSort(arr, mid+1, high)
  merge(arr, low, mid, high)
  
def merge(arr, low, mid, high):
    #Creates a temporary array to store the sorted array
    temp = []
    left = low
    right = mid+1
    
    #Compares two halves of the an array and appends it to temp
    while left<=mid and right<=high:
        if (arr[left] <= arr[right]):
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1

    #appends remaining elements for left subarray to temp
    while left <= mid:
        temp.append(arr[left])
        left+=1

     #appends remaining elements for right subarray to temp
    while right <= high:
        temp.append(arr[right])
        right+=1
        
    #stores the sorted elements into normal array from temporary array
    for i in range(low, high+1):
        arr[i] = temp[i-low]
        
# Code to print the list 
def printList(arr): 
    print(arr)
    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    low = 0
    high = len(arr) - 1
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr, low, high) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
