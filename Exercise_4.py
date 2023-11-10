# Python program for implementation of MergeSort
# Time Complexity : O(n*log n)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : N/A
# Any problem you faced while coding this : None
def mergeSort(arr):

  #write your code here
  length_of_arr = len(arr)
  # condition for dividing the list
  if length_of_arr > 1:
      mid = length_of_arr // 2
      left_part_of_list = arr[:mid]
      right_part_of_list = arr[mid:]
      mergeSort(left_part_of_list)
      mergeSort(right_part_of_list)
      left_index = 0
      right_index = 0
      final_list_index = 0

      # condition for merging the lists
      while left_index < len(left_part_of_list) and right_index < len(right_part_of_list):
          if left_part_of_list[left_index] < right_part_of_list[right_index]:
              arr[final_list_index] = left_part_of_list[left_index]
              left_index += 1
              final_list_index += 1
          else:
              arr[final_list_index] = right_part_of_list[right_index]
              right_index += 1
              final_list_index += 1

      # condition to check if any valye is left in left sublist and if it is left then it is added to final list
      while left_index < len(left_part_of_list):
          arr[final_list_index] = left_part_of_list[left_index]
          left_index += 1
          final_list_index += 1
     # condition to check if any value is left in right sublist and if it is left then it is added to final list
      while right_index < len(right_part_of_list):
          arr[final_list_index] = right_part_of_list[right_index]
          right_index += 1
          final_list_index += 1
# Code to print the list
def printList(arr):

    #write your code here
    return print(arr)

# driver code to test the above code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print ("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)
