# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
  #write your code here
  # Rearranges the array so that smaller and greater elements are to left side and right side of pivot element respectively. 
  pivot = arr[h]
  i = l - 1
  for j in range(l,h):
    if arr[j] < pivot:
      i+=1
      arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[h] = arr[h],arr[i+1]
  return i+1


def quickSortIterative(arr, l, h):
  #write your code here
  # This approach follows the idea of appending the start and end indexes of arrays and corresponding subarrays for the array partitions.
  st = []
  st.append((0,len(arr)-1))
  while st:
    l,h = st.pop()
    if l <h :
      pi = partition(arr,l,h)
      st.append((l,pi-1))
      st.append((pi+1,h))

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
print(arr)