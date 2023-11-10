#time complexity:
#space complexity:
#passed all cases on LeetCode:
#difficulty faced:
# comments:

# Python program for implementation of MergeSort 
def mergeSort(arr):
  if len(arr) > 1:

    mid = len(arr)//2

    Left = arr[:mid]
    Right = arr[mid:]

    mergeSort(Left)
    mergeSort(Right)

    i,j,k = 0,0,0

    while i < len(Left) and j < len(Right):
        if Left[i] < Right[j]:
              arr[k] = Left[i]
              i += 1

        else:
            arr[k] = Right[j]
            j += 1

            
        k += 1
    
    while i < len(Left):
        arr[k] = Left[i]
        i += 1
        k += 1 

    while j < len(Right):
        arr[k] = Right[j]
        j += 1
        k += 1 
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
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 