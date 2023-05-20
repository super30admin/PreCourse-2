"""
Time Complexity - O(nlogn)
Space Complexity - O(n)

"""
# Python program for implementation of MergeSort 
def mergeSort(arr):
  if len(arr)<=1:
    return arr
  middle=len(arr)//2
  left_merge=mergeSort(arr[:middle])
  right_merge=mergeSort(arr[middle:])
  return list(merge(left_merge,right_merge))


# merging two lists
def merge(left_half,right_half):
  res=[]
  while len(left_half)!=0 and len(right_half)!=0:
    if left_half[0]<right_half[0]:
      res.append(left_half[0])
      left_half.remove(left_half[0])
    else:
      res.append(right_half[0])
      right_half.remove(right_half[0])
  if len(left_half)==0:
    res+=right_half
  else:
    res+=left_half
  return res
    
  
  #write your code here

  # Code to print the list

def printList(arr):
#write your code here
  for i in arr:
    print(i)
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    arr=mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
