# Python program for implementation of MergeSort 
def mergeSort(arr):
    # print(arr)
    if len(arr) == 1:
        return  arr
    elif len(arr) == 0:
        return

    else:
        l = 0
        r = len(arr) - 1
        m = int((l + r)/2)
        sorted_left = mergeSort(arr[l:m+1])
        sorted_right = mergeSort(arr[m+1:])

        
        left_i = 0
        right_i = 0
        final_sorted = []
        while left_i <= len(sorted_left) and right_i <= len(sorted_right):
            print(sorted_right,sorted_left)
            if left_i >= len(sorted_left) and right_i < len(sorted_right) :
                for val in sorted_right[right_i:]:
                    final_sorted.append(val)
                break

            elif right_i >= len(sorted_right) and left_i < len(sorted_left):
                for val in sorted_left[left_i:]:
                    final_sorted.append(val)
                break

            else: 
                if sorted_left[left_i] < sorted_right[right_i]:
                    final_sorted.append(sorted_left[left_i])
                    left_i += 1
                elif sorted_right[right_i] < sorted_left[left_i]:
                    final_sorted.append(sorted_right[right_i])
                    right_i += 1
                else:
                    final_sorted.append(sorted_right[right_i])
                    final_sorted.append(sorted_left[left_i])
                    left_i += 1
                    right_i += 1
        return final_sorted
  
# Code to print the list 
def printList(arr): 
    print(arr)
    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7,8,7,4,5,1]  
    print ("Given array is", end="\n")  
    printList(arr) 
    arr = mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
