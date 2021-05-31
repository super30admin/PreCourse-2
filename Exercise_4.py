# Python program for implementation of MergeSort
# Time Complexity : O(nlog(n))
# Space Complexity : O(n)
def mergeSort(arr):
    length_of_array = len(arr)

    if length_of_array > 1:
        #  getting mid of the current array
        mid_index = length_of_array / 2
        #  define left and right hand side array to recursively call merge sort
        left_side_array = arr[0:mid_index]
        right_side_array = arr[mid_index: length_of_array]

        # calling mergesort on both side array
        mergeSort(left_side_array)
        mergeSort(right_side_array)

        left_index = 0
        right_index = 0
        new_index = 0
        new_array = []
        #  Iterate till we reached end of both arrays
        while left_index < len(left_side_array) and right_index < len(right_side_array):
            # move left pointer by one if left is lower than right else move right pointer
            if left_side_array[left_index] < right_side_array[right_index]:
                arr[new_index] = left_side_array[left_index]
                left_index += 1
            else:
                arr[new_index] = right_side_array[right_index]
                right_index += 1
            new_index += 1

        # Move left pointer by one of left element is lowe than right and vice-versa just to check
        # if all elements are at their place

        while left_index < len(left_side_array):
            arr[new_index] = left_side_array[left_index]
            left_index += 1
            new_index += 1

        while right_index < len(right_side_array):
            arr[new_index] = right_side_array[right_index]
            right_index += 1
            new_index += 1

def printList(arr): 
    
    for i in range(len(arr)):
        print (arr[i])
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is")
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ")
    printList(arr) 
