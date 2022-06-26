# Python program for implementation of MergeSort 
def merge(list1,list2):
  comb_list = []
  i = 0
  j = 0
  while(i<len(list1) and j<(len(list2))):
    if(list1[i]<list2[j]):
      comb_list.append(list1[i])
      i+=1
    else:
      comb_list.append(list2[j])
      j+=1
  while(i<len(list1)):
    comb_list.append(list1[i])
    i+=1
  while(j<len(list2)):
    comb_list.append(list2[j])
    j+=1
  return comb_list


def mergeSort(arr):
  if(len(arr)==1):
    return arr
  mid = int(len(arr)/2)
  left = arr[:mid]
  right = arr[mid:]
  return merge(mergeSort(left),mergeSort(right))

  
  #write your code here
  
# Code to print the list 
def printList(arr):
  print(arr)
  
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    arr = mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
