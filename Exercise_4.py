#did not understand how to implement  printlistPart
# Python program for implementation of MergeSort 
def mergeSort(arr):
    if len(arr) >1:
        mid = (len(arr))//2
        left = arr[:mid]
        right = arr[mid:]
    i =0
    j =0
    c=[]
    while i+j < len(arr) +len(arr):
        if i == len(arr):
            c.append(arr[j])
            j+=1
        elif j == len(arr):
            c.append(arr[i])
            i+=1
        elif arr[i]<arr[j]:
            c.append(arr[i])
            i+=1
        elif arr[j]<arr[i]:
            c.append(arr[j])
            j+=1
        return printList
  
# Code to print the list 
def printList(arr):   
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
