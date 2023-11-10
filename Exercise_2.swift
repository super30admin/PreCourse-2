import Cocoa

// Time Complexity - Best O(nlogn) | Worst - O(n2)
// Space Complexity - Best (logn) | Worst - O(n)
func quickSortArray(_ nums: [Int]) -> [Int] {
       var nums = nums
       quickSort(&nums, 0, nums.count - 1)
       return nums.sorted()
   }
   
   func quickSort(_ arr: inout [Int],_ left: Int,_ right: Int) {
       if left >= right { return }

       let mid = left + (right - left) / 2
       let pivot = arr[mid]
       let index = partition(&arr, left, right, pivot)
       quickSort(&arr, left, index - 1)
       quickSort(&arr, index, right)
   }

   func partition(_ arr: inout [Int],_ left: Int,_ right: Int,_ pivot: Int) -> Int {
       var left = left, right = right

       while left <= right {
           while arr[left] < pivot { left += 1 }
           while arr[right] > pivot { right -= 1}

           if left <= right {
               arr.swapAt(left, right)
               left += 1
               right -= 1
           }
       }

       return left
   }


let array = [10, 20, 1, 4, 100, 2, 15, 56]
print(quickSortArray(array))


