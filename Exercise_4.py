# Python program for implementation of MergeSort 
def mergeSort(arr):

    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_arr = mergeSort(arr[:mid])
    right_arr = mergeSort(arr[mid:])

    result = []

    l = r = 0

    while l < len(left_arr) and r < len(right_arr):
        if left_arr[l]<=right_arr[r]:
            result.append(left_arr[l])
            l+=1
        else:
            result.append(right_arr[r])
            r+=1

    if l<len(left_arr):
        result.extend(left_arr[l:])
    elif r<len(right_arr):
        result.extend(right_arr[r:])

    return result

  
  #write your code here
  
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
    arr = mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
