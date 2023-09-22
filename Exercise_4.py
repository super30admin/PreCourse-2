#space complexity: O(n)
#time complexity: O(nlogn)
# Python program for implementation of MergeSort 

def merge(array1, array2):                   #function to merge two lists in a sorted manner
  combined = []
  i = 0
  j = 0
  while i < len(array1) and j < len(array2):    #i transverse through list1 ans j through list2
        if array1[i] < array2[j]:               #which ever is smaller gets added to the new list
            combined.append(array1[i])          #loop continues till both lists are traversed
            i += 1
        else:
            combined.append(array2[j])
            j += 1
              
  while i < len(array1):                     #if any value left in list1, gets added in combined list
        combined.append(array1[i])
        i += 1

  while j < len(array2):                     #if any value left in list2, gets added in combined list
        combined.append(array2[j])
        j += 1

  return combined
  
def merge_Sort(arr):                            #function to merge sort
      if len(list) == 1:
        return list
    mid_index = int(len(list)/2)               #list is splited recursively, left and right side of list is sorted and merged back again recursively
    left = merge_sort(list[:mid_index])    
    right = merge_sort(list[mid_index:])
    return merge(left,right)
  
  
# driver code to test the above code
original_list = [3,1,4,2]

sorted_list = merge_sort(original_list)

print('Original List:', original_list)

print('\nSorted List:', sorted_list)
