//Exercise_1 : Binary Search
// Time Complexity : O(log(N))
// Space Complexity : O(1) constant space
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this :  No


// Your code here along with comments explaining your approach

/**** Steps ****/
/* 1) Traverse the array until starting index is less than or equal to the end index;
   2) Find the mid of the array
   3) Check if middle element is equal to the target value. 
          a) If it is equal to the target return the index
          b) Else check whether target is less than the mid element. If it is, it means target element will be on the left side, then search between start and mid-1 index.
          c) Else if check whether target is greater than the mid element, If it is, it means target element will be on the right side, then search between mid+1 index and the end;
   4) If target element not found, return -1;       
   
*/
class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
        int start =l;
        int end   =r; 
        while(start<=end){
            int mid = (end+start)/2;

            if(arr[mid]==x){
                return mid;
            } 

            //Checking if target element is on the left side
            if(x<arr[mid]){
                end = mid-1;
            }else{ //Checking if target element is on the right side
                start = mid+1;
            }

        }
        
        return -1;

    } 
  
    // Driver method to test above 
    public static void main(String args[]) 
    { 
        BinarySearch ob = new BinarySearch(); 
        int arr[] = { 2, 3, 4, 10, 40 }; 
        int n = arr.length; 
        int x = 10; 
        int result = ob.binarySearch(arr, 0, n - 1, x); 
        if (result == -1) 
            System.out.println("Element not present"); 
        else
            System.out.println("Element found at index " + result); 
    } 
} 
