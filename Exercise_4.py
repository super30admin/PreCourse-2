# Python program for implementation of MergeSort
def mergeSort(arr):
    #divide the array to left and right portions until you no longer can divide left and right arrays
    if len(arr)>1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L) #recursively call mergeSort on each part of array
        mergeSort(R)

        i,j,k=0,0,0

        while i <len(L) and j<len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i+=1
                k+=1
            else:
                arr[k]=R[j]
                j+=1
                k+=1
        #adding remaininging elements in aary
        while i<len(L):
            arr[k]=L[i]
            i+=1
            k+=1
        while j<len(R):
            arr[k]=R[j]
            k+=1
            j+=1


# Code to print the list
def printList(arr):
    print(arr)

# driver code to test the above code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print ("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)

#Time complexity: O(nlogn)
