# Python program for implementation of MergeSort
def mergeSort(arr,low,high):
    if(low<high):
        mid=low+((high-low)//2)
        mergeSort(arr,low,mid)
        mergeSort(arr,mid+1,high)
        merge(arr,low,mid,high)
# write your code here

def merge(arr,low,mid,high):
    size1=mid-low+1
    size2=high-mid
    leftList=list()
    rightList=list()
    for index in range(size1):
        leftList.append(arr[low+index])
    for index1 in range(size2):
        rightList.append(arr[mid +1 +index1])
    i=0
    j=0
    k=low
    while (i<size1 and j<size2):
        if leftList[i]<rightList[j]:
            arr[k]=leftList[i]
            k+=1
            i+=1
        else:
            arr[k] = rightList[j]
            k += 1
            j += 1
    for idx in range(i,len(leftList)):
        arr[k]=leftList[idx]
        k+=1
    for idx in range(j,len(rightList)):
        arr[k]=rightList[idx]
        k+=1
# Code to print the list
def printList(arr):
    for num in arr:
      print(num,end=" ")

# write your code here

# driver code to test the above code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr,0,len(arr)-1)
    print("Sorted array is: ", end="\n")
    printList(arr)
