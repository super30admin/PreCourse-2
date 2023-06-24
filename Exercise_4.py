# Python program for implementation of MergeSort 
# Time Complexity:O(n log n)
# Space Complexity:O(n)
def mergeSort(arr):
  if len(arr)>1:
     leftArray=arr[:len(arr)//2]
     rightArray=arr[len(arr)//2:]

     mergeSort(leftArray)
     mergeSort(rightArray)

     i=0
     j=0
     k=0

     while i<len(leftArray) and j< len(rightArray):
      if leftArray[i]<rightArray[j]:
         arr[k]=leftArray[i]
         i+=1
         k+=1
      else:
         arr[k]=rightArray[j]
         j+=1
         k+=1

     while i<len(leftArray):
       arr[k]=leftArray[i]
       i+=1
       k+=1

     while j< len(rightArray):
        arr[k]=rightArray[j]
        j+=1
        k+=1
         
         



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
