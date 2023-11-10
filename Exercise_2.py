def quickSort(nums,low,high):
  if low >= high:
    return 
  pivot = nums[high]
  left = low
  right = high

  while left < right:

    while nums[left] <= pivot and left < right:
      left += 1
    while nums[right] >= pivot and left < right:
      right -= 1

    nums[left], nums[right] = nums[right], nums[left]

  nums[left], nums[high] = nums[high], nums[left]
  print('last',nums)
  quickSort(nums,low,left - 1)
  quickSort(nums,left + 1, high)  
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
