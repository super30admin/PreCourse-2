# Python program for implementation of MergeSort 
def mergeSort(arr):
  
  
    if len(arr)>1:
    # 1. Get Left and right sub arrays.
        # left sub-array
        lsa= arr[:len(arr)//2]
        #rsa= arr[len(lsa)-1:]//2
        rsa= arr[len(arr)//2:]
        mergeSort(lsa)
        mergeSort(rsa)
        
    # 2. Comparing left most element in left array with the left most element in the right array.
        i=j=k=0

        while i<len(lsa) and j<len(rsa):
            if lsa[i]<rsa[j]:
                arr[k]= lsa[i]
                i+=1
            else:
                arr[k]= rsa[j]
                j+=1 
            k+=1

    # 3. Adding all the LEFT OVER elements in the left array to the main array.
        while i<len(lsa) :
            arr[k]= lsa[i]
            i+=1
            k+=1
        
    # 4. Adding all the LEFT OVER elements in the right array to the main array.
        while j<len(rsa) :
            arr[k]= rsa[j]
            j+=1
            k+=1
    return arr

  
  
# Code to print the list 
def printList(arr): 
    
    return [print(i) for i in arr]

# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 