# Python program for implementation of MergeSort 
def merge(l_half, r_half, length):
  # Time Complexity : O(n)
  # Space Complexity : O(n) 
  merged = [0 for i in range(length)]
  i=0
  j=0
  k=0
  while(j<len(l_half) and k<len(r_half)):
    if(l_half[j]<r_half[k]):
      merged[i]=l_half[j]
      j+=1
    else:
      merged[i]=r_half[k]
      k+=1
    i+=1

  if(i<=length-1):
    while(j<len(l_half)):
      merged[i]=l_half[j]
      i+=1
      j+=1
    while(k<len(r_half)):
      merged[i]=r_half[k]
      i+=1
      k+=1  
  return merged

def mergeSort(arr):
  # Time Complexity : O(n log n)
  # Space Complexity : O(n log n), because of new copies of l_half, r_half and merged arrays  
  #write your code here
  if(len(arr)<=1):
    return arr

  middle = (len(arr)-1)//2
  l_half = mergeSort(arr[:middle+1])
  r_half = mergeSort(arr[middle+1:])
  return merge(l_half, r_half, len(arr))

# Code to print the list 
def printList(arr): 
    
    #write your code here
    print(arr)

# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    print("Sorted array is: ", end="\n") 
    print(mergeSort(arr))
