# Python program for implementation of MergeSort 
#Time Complexity :  O(nlogn)
#Space Complexity : O(n)
#Did this code successfully run on Leetcode : yes
#Any problem you faced while coding this : no
def merge(l,r):
      i = 0
      j = 0
      k = 0

      result = []
      while(i<len(l) and j<len(r)):
            if l[i]<r[j]:
                  result.append(l[i])
                  i = i+1
            else:
                  result.append(r[j])

                  j = j+1
      while i<len(l):
            result.append(l[i])
            i = i+1
      while j<len(r):
            result.append(r[j])
            j = j+1
      print(result)
      return result
            
            


def mergeSort(arr):
      if len(arr)<2:
            return arr
      mid = int(len(arr)/2)
      left = mergeSort(arr[:mid])
      right = mergeSort(arr[mid:])
      return merge(left,right)
      
  
  #write your code here
  

  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    print(arr) 
     
    a1 = mergeSort(arr)
    print(a1)
