# Python program for implementation of MergeSort 
def mergeSort(arr):
    divideandconquer(arr,0,len(arr)-1)

def divideandconquer(arr,low,high):
    if (high-low)<1:
        return low
    mid = int((low+high)/2)
    divideandconquer(arr,low,mid)
    divideandconquer(arr,mid+1,high)
    merge(arr,low,mid,high)

def merge(arr,low,mid,high):

    i,j=low,mid+1
    while i<mid+1 and j<high+1:
        if arr[i]>arr[j]:
            arr[i],arr[j]=arr[j],arr[i]
            j+=1
        else:
            i+=1



# Code to print the list
def printList(arr):
    for i in arr:
        print(i)
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr)
    print("Sorted array is: ", end="\n") 
    printList(arr) 

# Complexity

# Time Complexity - merge o(n), divide- log(n) total nlog(n)
# Space Complexity - o(1) as iam  not using the extra space