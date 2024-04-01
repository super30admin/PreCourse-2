# Python program for implementation of MergeSort 

def merge(l,r):
    re=[]
    i,j=0,0

    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            re.append(l[i])
            i += 1
        else:
            re.append(r[j])
            j += 1

    while i < len(l):
        re.append(l[i])
        i += 1

    while j < len(r):
        re.append(r[j])
        j += 1

    return re
    
    
def mergeSort(arr):
  
  #write your code here
    if len(arr)<=1:
        return arr
    
    left = arr[: len(arr)//2]
    right = arr[(len(arr)//2) :]

    l = mergeSort(left)
    r = mergeSort(right)

    return merge(l,r)
    
  
# Code to print the list 
def printList(arr): 
    
    #write your code here
    for i in range(len(arr)):
        print(arr[i])
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    result = mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(result) 
