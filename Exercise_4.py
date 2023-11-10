# Python program for implementation of MergeSort 

def mergeSort(nums):
  if len(nums) > 1:
    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]

    mergeSort(left)
    mergeSort(right)

    i =j = k = 0

    while i < len(left) and j < len(right):

      if left[i] < right[j]:
        nums[k] = left[i]
        i += 1
      else:
        nums[k] = right[j]
        j+=1

      k += 1

    while i < len(left):
      nums[k] = left[i]
      i+=1
      k += 1

    while j < len(right):
      nums[k] = right[j]
      j+=1
      k+=1



def printList(nums):
  return nums
    
    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
    nums = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(nums) 
    mergeSort(nums) 
    print("Sorted array is: ", end="\n") 
    printList(nums) 
