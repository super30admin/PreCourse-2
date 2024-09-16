# Python program for implementation of MergeSort 
def merge(arrA, arrB):
    arrC = []
    nA = len(arrA)
    nB = len(arrB)
    a = 0
    b = 0

    while a < nA and b < nB:
        if arrA[a] <= arrB[b]:
            arrC.append(arrA[a])
            a += 1
        else:
            arrC.append(arrB[b]) 
            b += 1

    while a < nA:
        arrC.append(arrA[a])
        a += 1

    while b < nB:
        arrC.append(arrB[b])
        b += 1

    return arrC

def mergeSort(arr):
    n = len(arr)

    if n == 1:
        return arr
    
    mid = n//2
    arrA = arr[:mid]
    arrB = arr[mid:]

    arrA = mergeSort(arrA)
    arrB = mergeSort(arrB)

    return merge(arrA, arrB)
  
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
    arr = mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
