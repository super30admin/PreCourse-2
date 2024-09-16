# Python program for implementation of MergeSort 
def merge(arr,low,mid,high):
    i = low
    r = mid+1
    temp = []
    while(i <= mid and r <=high):
        if(arr[i] <= arr[r]):
            temp.append(arr[i])
            i+=1
        else:
            temp.append(arr[r])
            r+=1
    while i <= mid:
        temp.append(arr[i])
        i+=1
    while r <= high:
        temp.append(arr[r])
        r+=1
    for i in range(low,high+1):
        arr[i] = temp[i - low] #because the temp array starts at index 0, while arr has elements starting at index low which may not be 0.

def mergeSort(arr,low,high):
    if(low == high):
        return
    mid = (low + high) // 2
    mergeSort(arr,low,mid)
    mergeSort(arr,mid+1,high)
    merge(arr,low,mid,high)

  
  #write your code here
  
# Code to print the list 
def printList(arr):
    print(arr)
    
    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr,0,len(arr)-1) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
