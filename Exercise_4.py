# Python program for implementation of MergeSort 
def merge(arr1,arr2):
    # merge arr1 and arr2
    i=0
    j=0
    res=[]
    while True:
        if i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                res.append(arr1[i])
                i += 1
            else:
                res.append(arr2[j])
                j += 1
        else:
            if i >= len(arr1):
                res = res + arr2[j:len(arr2)]
                return res
            else:
                res = res + arr1[i:len(arr1)]
                return res

def mergeSort(arr):
  #write your code here
    if len(arr)>1:
        left=mergeSort(arr[0:len(arr)//2])
        right=mergeSort(arr[len(arr)//2:len(arr)])
        return merge(left,right)
    else:
        return arr
# Code to print the list 
def printList(arr): 
    for i in arr:
        print(i)
    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    arr=mergeSort(arr)
    print("Sorted array is: ", end="\n") 
    printList(arr) 
