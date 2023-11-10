#Time Complexity : O(nlogn)
#Space Complexity : O(n)
#It runs fine on my machine with desired output
#I had to learn the algorithm again.


# Python program for implementation of MergeSort

def merge(arr,low,mid,high):
    temp = [0] * (high - low + 1)
    i,j,k = low , mid+1 , 0
    while i<=mid and j<=high: #merging the two list in ascending order
        if arr[i] < arr[j]:
            temp[k] = arr[i]
            i = i+1
        else:
            temp[k] = arr[j]
            j = j+1
        k = k+1

    while i<=mid: #checking if any element is left in 1st half part of the list
        temp[k] = arr[i]
        k = k+1
        i = i+1

    while j<=high: #checking if any elements is left from the 2nd part of the list
        temp[k] = arr[j]
        k = k+1
        j = j+1

    for i in range(low,high+1):
        arr[i] = temp[i-low]

def mergeSort(arr,low,high):
    mid = (low+high)//2 #finding the mid point of the list
    if low<high: #terminate condition
        mergeSort(arr,low,mid) #recursion statement for first half of the list
        mergeSort(arr,mid+1,high) #recursion statement for 2nd half of the list
        merge(arr,low,mid,high) #merging the above splitted list in ascending order
  
# Code to print the list 
def printList(arr): 
    for i in arr:
        print(i)
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr,0,len(arr)-1)
    print("Sorted array is: ", end="\n") 
    printList(arr) 
