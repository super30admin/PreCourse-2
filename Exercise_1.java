// Time Complexity :  O(nlog(n))
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : No
// Any problem you faced while coding this : No


class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code 
    
      if(l<=r)
      {
        int mid = l + (r-l)/2;    //index of middle element
        if(x == arr[mid]){
            //if element to be searched same as middle element
            return mid;
        }
        if(x<arr[mid]){
            //search left
            return binarySearch(arr, l, mid-1, x);
        }else{
            //search right
           return binarySearch(arr, mid+1, r, x);
        }
      }        
        return -1;
    } 
  
    // Driver method to test above 
    public static void main(String args[]) 
    { 
        BinarySearch ob = new BinarySearch(); 
        int arr[] = { 2, 3, 4, 10, 40};          //sorted array
        int n = arr.length; 
        int x = 10; 
        int result = ob.binarySearch(arr, 0, n - 1, x); 
        if (result == -1) 
            System.out.println("Element not present"); 
        else
            System.out.println("Element found at index " + result); 
    } 
} 
