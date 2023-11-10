
#My logic did not work

def Sort(left, right, arr = []):

    if(not left or not right):

        if(not left):

            return right

        else:

            return left

    if(len(left) > len(right)):

        MAX = len(left)

    else:

        MAX = len(right)

    arr = []
    
    i, j, k = 0, 0, 0

    while(k < MAX):

        try:

            if(left[i] < right[j]):

                while(i < MAX):
                    print('-----')
                    if(left[i] < right[j]):

                        arr.append(left[i])
                        left.remove(left[i])
                        i = i + 1
                    
                    else:

                        break
            
            else:

                while(j < MAX):
                    print('-----')
                    if(left[i] > right[j]):

                        arr.append(right[j])
                        right.remove(right[j])

                        j = j + 1

                    else:

                        break

            k = k + 1
        
        except IndexError:

            if(left and right):

                arr = Sort(left, right, arr)

                return arr

            else:

                if(left and len(right) == 0):

                    for i in range(len(left)):

                        arr.append(left[i])

                    return arr

                elif(right and len(left)):

                    for j in range(len(right)):

                        arr.append(right[i])
                    
                    return arr
    return arr

# Python program for implementation of MergeSort 
def mergeSort(arr, left, right):

    if(len(arr) < 2):

        return arr

    #write your code here
    else:

        mid = int(right/2)

        if(len(arr) == 2):

            temp = arr[0] 
            arr[0] = arr[1]
            arr[1] = temp
        
        left_arr = mergeSort(arr[:mid], 0, mid)
        print('Left: ',left_arr)
        right_arr = mergeSort(arr[mid:], mid, len(arr))
        print('Right: ',right_arr)

        if(len(left_arr) > 1 or len(right_arr) > 1):
    
            arr = Sort(left_arr, right_arr)
     
        return arr
         
    return arr
  
# Code to print the list 
def printList(arr):
    #write your code here
    pass
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    result = mergeSort(arr, 0, len(arr)-1) 
    print("Sorted array is: ", result) 
    printList(arr) 
