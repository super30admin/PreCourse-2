#Time Complexity :
# O(Log N)

#Space Complexity :
# O(N)

#Did this code successfully run on Leetcode :
#I got 10/18 test cases to pass and had TLE on the rest
#Any problem you faced while coding this :
#Workig on the time issue
# Python program for implementation of MergeSort 

def merge(arr,l,m,r):
    #for elem in 
    i = 0
    j = m
    new_array = []
    # Merging both arrays - traverse through both arrays and add whichever element is smaller
    
    while (i < len(arr[l:m]) or j < m+len(arr[m:r])):
        flag = 0
        # If all elements from 1 list have been added, then add elements from the other list
        if j == m + len(arr[m:r]):
            new_array.append(arr[i])
            i+=1
            continue
        # If all elements from 1 list have been added, then add elements from the other list
        if i ==  len(arr[0:m]):
            new_array.append(arr[j])
            j+=1
            continue
        #Whichever is smaller is added first
        if arr[i] > arr[j]:
            new_array.append(arr[j])
            if j < m+len(arr[m:r]):
                j+=1
            else :
                flag = 1
        else :
            new_array.append(arr[i])
            if i < len(arr[l:m]):
                i+=1
            else :
                flag = 2
        #Checking if we reached the end of one list -then we move the other list iterator
        if flag == 1:
            i += 1
        elif flag == 2:
            j+= 1
    return new_array

def mergeSort(arr):
    #write your code here

    #If single element, return it
    if len(arr) == 1:
        return arr
    #If 2 elements, put them in correct position and return
    if len(arr) == 2 :
        if arr[0] <= arr[1]:
            return arr
        else :
            elem = arr[0]
            arr[0] = arr[1]
            arr[1] = elem
            return arr
    l = 0
    m = int(len(arr)/2)
    r = len(arr)
    #Sort the left half
    left_sorted = mergeSort(arr[l:m])
    #Sort the Right half
    right_sorted = mergeSort(arr[m:r])
    total_len = len(left_sorted)+len(right_sorted)
    #Merge the sorted half lists
    arr = merge(left_sorted+right_sorted,0,int(total_len/2),total_len)
    return arr
 
  
# Code to print the list 
def printList(arr): 
    print (arr)
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 23,7]  
    arr = [5,2,3,1]
    print ("Given array is", end="\n")  
    printList(arr) 
    new_arr = mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(new_arr) 
