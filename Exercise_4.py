# Python program for implementation of MergeSort

def merge(arr,l,mid,r):

    first=mid-l+1
    second=r-mid

    left=arr[l:mid+1]
    right=arr[mid+1:r+1]

    i=0
    j=0
    k=l

    while i<first and j<second:

        if left[i]<right[j]:
            arr[k]=left[i]
            i+=1
        else:
            arr[k]=right[j]
            j+=1

        k+=1

    while i <first:
        arr[k]=left[i]
        i+=1
        k+=1

    while j<second:
        arr[k]=right[j]
        j+=1
        k+=1

def mergeSort(arr,l,r):

    if l<r:
        mid=l+(r-l)//2
        mergeSort(arr,l,mid)
        mergeSort(arr,mid+1,r)
        merge(arr,l,mid,r)

  #write your code here

# Code to print the list
def printList(arr):

    print(arr)
    #write your code here

# driver code to test the above code
if __name__ == '__main__':
    arr = [12,13]
    print ("Given array is", end="\n")
    printList(arr)

    mergeSort(arr,0,len(arr)-1)
    print("Sorted array is: ", end="\n")
    printList(arr)
