"""  
 
 Time Complexity : O(nlogn)
 Space Complexity : O(n)
 Did this code successfully run on Leetcode : Yes
 Any problem you faced while coding this : No


 Your code here along with comments explaining your approach :
 Merge Sort algorithm splits the existing array into half and repeats the same again of splitted left and right halves.
 Once the length reaches <= 1 it returns the element and now it starts to merge back in the sorted order by running a loop against
 these two halves and we check which is smaller and we store that element in the arr along with incrementing the index based on the
 array ele we pushed that is if it's left then we increment left_index, if it's right we increment right index. The main array index
 will be left_index+right_index. Once the loop is done we again check the left_index against length of left array and 
 right index against length of right array to see if any array still has elements, if yes, we store them back to arr based on left_index+right_index.
 We repeat this process on the splitted arrays and hence the array is sorted.
 """

# Python program for implementation of MergeSort 
def mergeSort(arr):
  #write your code here
  
  if len(arr) <= 1:
     return
  
  mid = len(arr) // 2

  left_arr = arr[:mid]
  right_arr = arr[mid:]

  mergeSort(left_arr)
  mergeSort(right_arr)
  mergeSortHelper(arr, left_arr, right_arr)

def mergeSortHelper(arr, left_arr, right_arr):
  left_index, right_index = 0, 0
  
  while left_index < len(left_arr) and right_index < len(right_arr):
    if left_arr[left_index] <= right_arr[right_index]:
      arr[left_index + right_index] = left_arr[left_index]
      left_index += 1
    else:
      arr[left_index + right_index] = right_arr[right_index]
      right_index += 1

  while left_index < len(left_arr):
    arr[left_index + right_index] = left_arr[left_index]
    left_index += 1

  while right_index < len(right_arr):
    arr[left_index + right_index] = right_arr[right_index]
    right_index += 1

# Code to print the list 
def printList(arr): 
    #write your code here
    for ele in arr:
        print(f"{ele} \n")
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
