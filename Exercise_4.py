# Python program for implementation of MergeSort 
def mergeSort(arr):
  mid = len(arr)//2
  left = arr[:mid]
  right = arr[mid:]
  print(left)
  print(right)
  mergeSort(left)
  mergeSort(right)

  
  #write your code here
  
# Code to print the list 
# def printList(arr): 
    
    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    # printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    # printList(arr) 
