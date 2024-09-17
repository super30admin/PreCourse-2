# Python program for implementation of MergeSort 
def mergeSort(arr, l, r):
    if l >= r:
        return 
    m = (l+r)//2
    mergeSort(arr, l, m)
    mergeSort(arr, m+1, r)
    merge(arr, l, m, r)

def merge(arr, l, m, r):
    left = l
    right = m+1
    while left <= m and right <= r:
        if arr[left] <= arr[right]:
            left += 1
        else:
            temp = arr[right]
            arr[right] = arr[left]
            arr[left] = temp
            left += 1
            right += 1
    
    

  
  #write your code here
  
# Code to print the list 
def printList(arr): 
    for i in range(len(arr)):         
        print(arr[i], end=" ")
    
    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr, 0, len(arr)-1) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
