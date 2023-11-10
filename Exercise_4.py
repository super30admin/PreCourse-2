# Python program for implementation of MergeSort 
def mergeSort(arr):
    if len(arr)> 1:
        mid = len(arr)//2
        lefthalf  = arr[:mid]
        righthalf = arr[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0

        while i <len(lefthalf)  and j <len(righthalf):
            if lefthalf[i]< righthalf[j]:
                arr[k]=lefthalf[i]
                i+=1
            else:
                arr[k] = righthalf[j]
                j+=1
            k+=1

        while i<len(lefthalf):
            arr[k] = lefthalf[i]
            i+=1
            k+=1
        while j < len(righthalf):
            arr[k] = righthalf[j]
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

#time complexity - O(nLog(n))