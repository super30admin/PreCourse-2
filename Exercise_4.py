#time complexity is O(nlogn)
# space complexity is O(n)

# Python program for implementation of MergeSort 

def mergeSort(arr):
    if len(arr) > 1 :
      mid  = len(arr) // 2  #floor function
      L = arr[:mid]
      R = arr[mid:]

      mergeSort(L)
      mergeSort(R)

      left = 0
      right = 0
      main = 0

      while(left < len(L) and right < len(R)):
          if L[left] <= R[right]:
            arr[main] = L[left]
            main  =  main + 1
            left = left + 1
          else:
            arr[main] = R[right]
            main = main + 1
            right = right + 1
      while(left < len(L)):
         arr[main] = L[left]
         main =  main + 1
         left  = left + 1
      while(right < len(R)):
         arr[main] = R[right]
         main = main + 1
         right = right + 1
      



  
  #write your code here
  
# Code to print the list 
def printList(arr): 
  for i in range(0, len(arr)):
    print(arr[i], end=" ")
  print("\n")
    
    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
