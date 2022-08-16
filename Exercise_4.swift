import Cocoa

// Time Complexity -  O(nlogn)
// Space Complexity - O(n)
func mergeSortArray(_ nums: [Int]) -> [Int] {
        var array = nums
        
        mergeSort(&array, 0, array.count-1)
        
        return array
    }
    
    func mergeSort(_ array: inout [Int], _ left: Int, _ right: Int) {
        if (left >= right) {return}
        
        let mid: Int = left + (right-left)/2
        
        mergeSort(&array, left, mid)
        mergeSort(&array, mid+1, right)
        
        merge(&array, left, right)
    }
    
    func merge(_ array: inout[Int], _ left: Int, _ right: Int) {
        let leftEnd: Int = left+(right-left)/2
        var l = left
        var r = leftEnd+1
        let rightEnd = right
        
        var helper:[Int] = Array()
        
        while (l <= leftEnd && r <= rightEnd) {
            if array[l] <= array[r] {
                helper.append(array[l])
                l += 1
            } else {
                helper.append(array[r])
                r += 1
            }
        }
        
        while (l <= leftEnd) {
            helper.append(array[l])
            l += 1
        }
        
        while (r <= rightEnd) {
            helper.append(array[r])
            r += 1
        }
        
        for i in 0...(right-left) {
            array[left+i] = helper[i]
        }
    }


let array = [10, 20, 1, 4, 100, 2, 15, 56]
print(mergeSortArray(array))


