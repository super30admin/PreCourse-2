"""
Time Complexity: O(nlogn)
Space Complexity: o(n)
"""


def merge(list1, list2):
    i, j = 0, 0
    combined = [] 

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1

    while i < len(list1):
        combined.append(list1[i])
        i += 1
    while j < len(list2):
        combined.append(list2[j])
        j += 1
    return combined 


def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list
    mid_index = len(my_list) // 2
    left = merge_sort(my_list[:mid_index])
    right = merge_sort(my_list[mid_index:])

    return merge(left, right)

  
# Code to print the list 
def printList(arr): 
    for i in arr:
        print(f"{i}")
    
    
    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]
    print ("Given array is", end="\n")  
    printList(arr) 
    print("Sorted array is: ", end="\n") 
    printList(merge_sort(arr))
   
