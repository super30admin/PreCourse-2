# // Time Complexity :O(N^2) - O(N) for partitioning and O(N) for the iteration
# // Space Complexity :O(N)
# // Did this code successfully run on Leetcode :yes
# // Any problem you faced while coding this : had some trouble figuring out this one because I hadn't done it iteratively before, so had to do a lot of research


# Python program for implementation of Quicksort

# This function is same in both iterative and recursive version
def partition(arr, l, h):
  #write your code here
  #partition should be the same for recursive and iteration
  pivot = arr[h]       # we are using the last element as the pivot
  index=l               # we always start at low
  while l <h:
      if(arr[l]<=pivot):        # if the number is less than the pivot, then swap it with the first greater number in the array
          arr[l], arr[index] = arr[index] , arr[l]
          index+=1
      l+=1
  arr[h], arr[index] = arr[index], arr[h]       #at the end, swap the pivot next to the last number smaller than it
  return index



def quickSortIterative(arr, l, h):
  sublist = []            # to store all the sublist we will be partitioning
  first, last = 0, h      #starting with the whole array

  sublist.append((first, last))             #add the index of the whole array to partition first as a tuple

  while (sublist != []):
    first, last = sublist.pop()         #get the elements you want to partition first

    p = partition(arr, first, last)

    if first < p -1:                    # if there are elements on the left of pivot, keep pushing them to the sublist to partition
      sublist.append((first, p-1))

    if last > p+1:                       # if there are elements on the right of pivot, keep pushing them to the sublist to partition
      sublist.append((p+1, last))

#added the test case from exercise 2
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  