# Python program for implementation of MergeSort
#Time Complexity: O(n logn).
#Space Complexity: O(n) + O(n) stack space for the recursion.
def mergeSort(arr, low, high):
  #write your code here
    if low>=high: # base case to stop the termination
        return
    mid = (low+high)//2
    mergeSort(arr, low, mid) #Recursively sort left subarray
    mergeSort(arr, mid+1, high) #Recursively sort right subarray
    merge(arr, low, mid, high) #merge the left and the right subarray

def merge(arr, low, mid, high):
    tempArr = [] #create a temp array
    left, right = low, mid+1 #create left and right pointers to iterate the left and right subarray respectively
    while left <= mid and right <=high: 
      if arr[left] <= arr[right]: #choose the smaller element from the left and right subarray and insert in the temporary array and move respective pointers
        tempArr.append(arr[left])
        left+=1
      else:
        tempArr.append(arr[right])
        right+=1
    
    while left<=mid: #place any remaining elements in the left subarray at the end of the temporary array
      tempArr.append(arr[left])
      left+=1

    while right<=high: #place any remaining elements in the right subarray at the end of the temporary array
      tempArr.append(arr[right])
      right+=1
    
    for i in range(low, high+1): #move elements in the temporary array to the original array
      arr[i] = tempArr[i-low]
   
# Code to print the list 
def printList(arr): 
    
    #write your code here
   print(arr)

  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr,0,len(arr)-1) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
