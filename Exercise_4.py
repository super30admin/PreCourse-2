# Python program for implementation of MergeSort 

'''
Merge sort is a divide and conquer approach
1. Divide the array till you get the last element
2. Once you get the last elements, start merging the elements
3. Start merging the elemnts from lhs of the list
4. You merge the left list and the right list, perform comparison and return the new merged list
5. You perform merge till all the recursive calls for lhs and rhs side of the list are completed
6. Time Complexity:
    1. Its 0(nlogn)
    2. Divide is a logn complexity
    3. Merge is n complexity because you perform check with individual elements
'''
def mergeSort(arr):
    return divide(arr,0,len(arr)-1)

def divide(arr,low,high):
    
    if low == high:
        return [arr[low]]
    
    # Get the midpoint
    mid = (high-low)//2+ low
    leftList = divide(arr,low,mid)
    rightList = divide(arr,mid+1,high)
    
    return conquer(leftList,rightList)
    
def conquer(leftList,rightList):
    
    # ptr to left list
    l = 0
    
    # ptr to right list
    r = 0
    
    # return the list
    rtrList = []
    
    # total count
    flag = False
    
    while flag != True:
        
        if l < len(leftList) and r <len(rightList):
            
            if leftList[l] < rightList[r]:
                
                # Append leftList[l] to rtrList
                rtrList.append(leftList[l])
                l+=1
            
            elif rightList[r] < leftList[l]:
                
                # Append rightList[l] to rtrList
                rtrList.append(rightList[r])
                r+=1
        
        elif l == len(leftList) and r < len(rightList):
            
            # Exhausted with leftList, only left with rightList elements
            rtrList.append(rightList[r])
            r+=1
        
        elif r == len(rightList) and l < len(leftList):
            
            # Exhausted with rightList, only left with leftList elements
            rtrList.append(leftList[l])
            l+=1
        
        else:
            
            # Set flag
            flag = True
        
        continue
    
    return rtrList

if __name__ == '__main__': 

    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    print(arr)
    print("\nSorted array is: ", end="\n") 
    print(mergeSort(arr))