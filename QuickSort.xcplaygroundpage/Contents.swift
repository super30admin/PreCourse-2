// Time complexity O(n*logn)
// Space complexity O(1)

func quickSory(_ array: inout [Int],_ low: Int,_ high: Int) {
    if low < high {
        let pi = partition(&array, low, high)
        quickSory(&array, low, pi - 1)
        quickSory(&array, pi + 1, high)
    }
}

func partition(_ array: inout [Int],_ low: Int,_ high: Int) -> Int {
    let pivot = array[high]
    var i = low - 1
    for j in low..<high {
        if array[j] < pivot {
            i += 1
            swap(&array, i, j)
        }
    }
    swap(&array, i + 1, high)
    return i + 1
    
}

func swap(_ array: inout [Int],_ fromInded: Int,_ toIndex: Int)  {
    let temp = array[fromInded]
    array[fromInded] = array[toIndex]
    array[toIndex] = temp
}

var array = [1, 2, 3, 4, 5, 6]
quickSory(&array, 0, array.count - 1)

