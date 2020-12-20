#Time complexity= O(nlogn)
#Space complexity=O(n)

# Python program for implementation of MergeSort 
def mergeSort(arr):
  #write your code here
    if(len(arr)>1):
        m=len(arr)//2
        l=arr[m:] #left partition
        r=arr[:m] #right partition
        mergeSort(l)# recursively calling left half
        mergeSort(r)# recursively calling right half 
        i=0
        j=0
        k=0
        while( i<len(l) and j<len(r)):
            if(l[i]<r[j]):
                arr[k]=l[i]
                i+=1
            else:
                arr[k]=r[j]
                j+=1
            k+=1
        while(i<len(l)):
            arr[k] = l[i]
            i += 1
            k += 1
        while(j<len(r)):
            arr[k] = r[j]
            j += 1
            k += 1
        
        
# Code to print the list 
def printList(arr): 
    
    #write your code here
    print(arr)
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
