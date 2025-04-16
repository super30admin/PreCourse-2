# Python program for implementation of MergeSort 
def mergeSort(arr, low, high):


  if(low >= high):
    return
  mid = (low+high)//2
  mergeSort(arr, low, mid)
  mergeSort(arr, mid+1, high)
  merge(arr, low, mid, high)
def merge(arr, l, mid, h):
  left = l
  right = mid+1
  temp = []
  while(left<= mid and right<=h):
    if(arr[left]<= arr[right]):
      temp.append(arr[left])
      left+=1
    else:
      temp.append(arr[right])
      right+=1
  while(left<=mid):
      temp.append(arr[left])
      left+=1
  while(right<=h):
      temp.append(arr[right])
      right+=1
  for i in range(l, h+1):
      arr[i] = temp[i-l]
    
# Code to print the list 
def printList(arr): 
    for i in range(len(arr)):         
        print(arr[i], end=" ") 
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr,0,len(arr)-1) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
