# Time Complexity : O(nlogn)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : Ran this in VS Code ide
# Any problem you faced while coding this : Yes
# Problem - I again ran into a typo where I wasn't adding low_pointer to mid .. so my code always considered only from the zero(th) index.
# Wrong formula that I initially used => mid = (rp-lp)//2.

# Approach - I changed the definition of mergeSort given to take in low and high pointer too.
# The merge step returns a new array of sorted elements

def merge(left_subarray, right_subarray):
    result = []
    left_subarray_size = len(left_subarray)
    right_subarray_size = len(right_subarray)
    lp, rp = 0, 0
    # use two pointers to compare elements of the two sorted arrays
    while lp < left_subarray_size and rp < right_subarray_size:

        # if left_element < right_element - add/process it to the result array and move the left pointer
        if left_subarray[lp] < right_subarray[rp]:
            result.append(left_subarray[lp])
            lp = lp + 1
        else:
            result.append(right_subarray[rp])
            rp = rp + 1

    # if there are elements on the left subarray
    while lp < left_subarray_size:
        result.append(left_subarray[lp])
        lp = lp + 1

    # if there are elements on the right subarray
    while rp < right_subarray_size:
        result.append(right_subarray[rp])
        rp = rp + 1

    return result


def mergeSort(arr, lp, rp):
    # if the pointers are the same, it means there is only one element
    if rp == lp:
        return [arr[lp]]
    if lp < rp:
        mid = lp + (rp-lp)//2
        # sort left half
        sort_left = mergeSort(arr, lp, mid)
        # sort right half
        sort_right = mergeSort(arr, mid+1, rp)
        # merge the halves
        merged_arr = merge(sort_left, sort_right)
        return merged_arr

# Code to print the list


def printList(arr):
    for element in arr:
        print(element,  end="\t")
    print()
    # write your code here

    # driver code to test the above code
if __name__ == '__main__':
    arr = [10, 80, 50, 90, 40, 100, 70]
    print("Given array is", end="\n")
    printList(arr)
    arr = mergeSort(arr, 0, len(arr)-1)
    print("Sorted array is: ", end="\n")
    printList(arr)
