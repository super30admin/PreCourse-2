# Python program for implementation of MergeSort
def mergeSort(arr):
  
  if len(arr)>1:#to check if the array is non empty
         mid=len(arr)//2# setting mid point
         L=arr[:mid]#divinding the array
         R=arr[mid:]

         mergeSort(L)
         mergeSort(R)
        
         i=j=k=0
         while i<len(L) and j<len(R):
                if L[i]<R[j]:

                    arr[k]=L[i]
                    i=i+1
                else:
                    arr[k]=R[j]
                    j=j+1
                k=k+1
         while i<len(L):

                 arr[k]=L[i]
                 i=i+ 1
                 k=k+1

         while j<len(R):

                 arr[k]=R[j]
                 j=j+ 1
                 k=k+1

        
  
# Code to print the list
def printList(arr):
    for i in range(len(arr)):
        
         print(arr[i],end=" ")
    print()
    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
