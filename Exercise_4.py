# Time Complexity : O(n log n)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode: I ran this code in VS Code editor in my local machine
# Any problem you faced while coding this: No


# Python program for implementation of MergeSort 

def mergeSort(arr):
  #  Divide the given array if it has more than 1 elements, else just sort it 
   if len(arr)>1:
      sorted_array = []
      ending_index = len(arr)-1

      if(ending_index<=0):
        return 

      # Find middle index of the given array
      mid_index = (ending_index)// 2

      # Initialize L and R arrays to contains left and right half of the given array
      L=[]
      R=[]

      # Fill values in L and R array 
      for i in range(mid_index+1):
        L.append(arr[i])
        i+=1

      for j in range(mid_index+1,ending_index+1):
        R.append(arr[j])
        j+=1

      # Call mergeSort to further divide L and R if possible
      mergeSort(L)
      mergeSort(R)

      # Iterate through the divided L and R array and fill the sorted values back to arr
      i=j=k=0

      while len(L)>i and len(R)>j:
         if L[i]<=R[j]:
            arr[k]=L[i]
            i+=1
         else:
            arr[k]=R[j]
            j+=1
         k+=1

      while len(L) > i:
         arr[k] = L[i]
         i+=1
         k+=1

      while len(R) > j:
         arr[k] = R[j]
         j+=1
         k+=1
  
  
# Code to print the list 
def printList(arr):
  end_index = len(arr)
    
  for i in range(end_index):
      print(arr[i], end=" ")
  print(" ") 
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
