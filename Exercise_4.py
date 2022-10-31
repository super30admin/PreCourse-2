#Time complexity:O(nlog(n))
#space complexity: O(n)
#Ran in leetcode: yes
#problems/issues: None
#split the array into left and right halfs. Then merge the left and right subarray(which are sorted) and return the output
# Python program for implementation of MergeSort 
def merge(A,B):
  C=[]
  i=0
  j=0
  while(i<len(A) and j<len(B)):
    if(A[i]<B[j]):
      C.append(A[i])
      i+=1
    else:
      C.append(B[j])
      j+=1

  while(i<len(A)):
    C.append(A[i])
    i+=1
  while(j<len(B)):
    C.append(B[j])
    j+=1
  return C

def mergeSort(arr,low,high):
  if(low>=high):
    #print(low)
    return [arr[high]]
  #write your code here
  mid=(low+high)//2
  #print(low,high)
  A=mergeSort(arr,low,mid)
  B=mergeSort(arr,mid+1,high)
  C=merge(A,B)
  return C

  
# Code to print the list 
def printList(arr): 
    
    #write your code here
    for i in arr:
      print(i)
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    #printList(arr) 
    arr=mergeSort(arr,0,len(arr)-1) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
