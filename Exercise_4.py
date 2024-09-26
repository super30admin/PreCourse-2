# Python program for implementation of MergeSort 

def merge(arr,l,mid,h):
    
    
    i,j,k = 0,0,l
    a,b = arr[l:mid+1],arr[mid+1:h+1]
    m,n = len(a) - 1, len(b) - 1
    while i <= m and j <= n:
        if a[i] < b[j]:
            arr[k] = a[i]
            arr[k+1] = b[j]
            k += 1
            i += 1
        elif a[i] > b[j]:
            arr[k] = b[j]
            arr[k+1] = a[i]
            k += 1
            j += 1
        else:
            arr[k] = a[i]
            i += 1
            j += 1
            k += 1
            

    if i != m:
        for ele in a[i:]:
          arr[k] = ele
          k += 1
    elif j != n:
        for ele in b[j:]:
          arr[k] = ele
          k += 1

            

def mergeSort(arr,l,h):
      
      if l < h:
          #print(l,h)
          mid = round((h-l)/2) + l
          mergeSort(arr,l,mid)
          mergeSort(arr,mid+1,h)
          merge(arr,l,mid,h) 

    
  
  #write your code here
  
# Code to print the list 
def printList(arr): 
    print(arr)
    
    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr,0,len(arr)-1) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 


