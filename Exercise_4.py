# Python program for implementation of MergeSort
# Time complexity O(n log n)
# Space complexity O(n)

def mergeSort(arr):
    if len(arr)>1:
        Left = arr[:len(arr)//2]                    #Divide and Conquer
        Right= arr[len(arr)//2:]

        mergeSort(Left)                             #Recursively dividing an array to smallest sub arrays
        mergeSort(Right)

        i=j=k=0                                         #k is the result array index
        while i< len(Left) and j< len(Right):           #merge back
            if Left[i]<Right[j]:
                arr[k]= Left[i]
                i+=1
            else:
                arr[k]=Right[j]
                j+=1
            k+=1

        #checking if any element is still left
        while i< len(Left):
            arr[k] = Left[i]
            i += 1
            k += 1
        while j< len(Right):
            arr[k] = Right[j]
            j += 1
            k += 1


# Code to print the list 
def printList(arr): 
    for i in range(len(arr)):
        print(arr[i]," ")

  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
