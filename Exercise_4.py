'''
Time Complexity : O(nlog(n))
Space Complexity : O(n) 
'''

# Python program for implementation of MergeSort 
def mergeSort(arr):
  op = []
  fp  =0
  sfp = 0
  if(len(arr)<=1):
    return arr
  mid = int(len(arr)/2)
  l = mergeSort(arr[:mid])
  r = mergeSort(arr[mid:])
  while(fp<=len(l)-1 and sfp<=len(r)-1):
    if(l[fp]<r[sfp]):
      op.append(l[fp])
      fp += 1
    elif(l[fp] == r[sfp]):
      op.append(l[fp])
      op.append(r[sfp])
      fp += 1
      sfp += 1
    else:
      op.append(r[sfp])
      sfp += 1
  if(fp == len(l) and sfp<=len(r)-1):
    op.extend(r[sfp:])
  elif(sfp==len(r) and fp<=len(l)-1):
    op.extend(l[fp:])
  return op
  
  
  #write your code here
  
# Code to print the list 
def printList(arr): 
    print(arr)
    
    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    # print ("Given array is", end="\n")  
    # printList(arr) 
    arr = mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
