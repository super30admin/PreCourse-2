# Python program for implementation of MergeSort 
def mergeSort(arr):
  #write your code here
    if len(arr)<=1:
        return arr
    mid =len(arr)//2  #finding mid
    left_arr=arr[:mid] #Dividing array in left and right subarrays
    right_arr=arr[mid:]

    left_arr=mergeSort(left_arr) #Recursively sorting both the subarrays
    right_arr=mergeSort(right_arr)

    mergedArr=[]
    i=j=0

    while i<len(left_arr) and j<len(right_arr):
        if left_arr[i]<right_arr[j]:
            mergedArr.append(left_arr[i])
            i+=1
        else:
            mergedArr.append(right_arr[j])
            j+=1
    mergedArr.extend(left_arr[i:])  #to add remaining elements from left and right subarray
    mergedArr.extend(right_arr[j:])

    return mergedArr


# Code to print the list 
def printList(arr):
    #write your code here
    for i in range(len(arr)):
        print(arr[i], end=" ")

  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    sorted=mergeSort(arr)
    print("\n"+"Sorted array is: ", end="\n")
    printList(sorted)
