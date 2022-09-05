# Python program for implementation of MergeSort 

# Time Complexity: O(nlogn)
# Space Complexity: O(n)

def merge(l, r):
  li, ri = 0, 0 
  result = list()

  while li < len(l) and ri < len(r):
    if l[li] < r[ri]:
      result.append(l[li])
      li += 1
    else:
      result .append(r[ri])
      ri +=1
    
  result += l[li:]
  result += r[ri:]

  return result

def mergeSort(arr):
  
  #write your code here
  if len(arr) <= 1:
    return arr

  h = int(len(arr) / 2)
  l = mergeSort(arr[:h])
  r = mergeSort(arr[h:])

  return merge(l, r)
  
# Code to print the list 
def printList(arr): 
    
  #write your code here
  print(arr)
  
# driver code to test the above code 
if __name__ == '__main__': 
  arr = [12, 11, 13, 5, 6, 7]  
  print ("Given array is", end="\n")  
  printList(arr) 
  a = mergeSort(arr) 
  print("Sorted array is: ", end="\n") 
  printList(a) 
