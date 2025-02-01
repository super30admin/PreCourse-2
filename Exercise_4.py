# Python program for implementation of MergeSort 
def mergeSort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        lf=arr[:mid]
        rf=arr[mid:]
        mergeSort(lf)
        mergeSort(rf)
        i=j=k=0

        while i <len(lf) and j<len(rf):
            if lf[i]<rf[j]:
                arr[k]=lf[i]
                i+=1
            else:
                arr[k]=rf[j]
                j+=1
            k+=1

        while i<len(lf):
            arr[k]= lf[i]
            i+=1
            k+=1
        while j<len(rf):
            arr[k]= rf[j]
            j+=1
            k+=1
  
# Code to print the list 
def printList(arr):
    for i in arr:
        print(i, end ="")  
    print()   
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
