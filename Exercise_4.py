# Python program for implementation of MergeSort 
#time complexity T(n) = nlog(n)
#space complexity: O(n)

def mergeSort(arr):

  if len(arr) > 1:
    leftA = arr[:len(arr)//2]
    rightA = arr[len(arr)//2:]

    mergeSort(leftA)
    mergeSort(rightA)

    i=j=k=0

    while(i<len(leftA) and j<len(rightA)):
      if leftA[i] < rightA[j]:
        arr[k] = leftA[i]
        i +=1
      else:
         arr[k] = rightA[j]
         j +=1
      
      k += 1

    while i< len(leftA):
      arr[k] = leftA[i]
      i +=1
      k +=1
    
    while j< len(rightA):
      arr[k] = rightA[j]
      j +=1
      k +=1


    
  #write your code here
  
# Code to print the list 
def printList(arr): 
    print(str(arr))
    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
