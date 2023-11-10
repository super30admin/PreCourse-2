// Time Complexity : O(log n)
// Space Complexity :O (1)
// Did this code successfully run on Leetcode :n/a
// Any problem you faced while coding this :no


// Your code here along with comments explaining your approach


class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
        
         while (l <= r) {
            int mid = l + (r - l) / 2;

            // the element is found
            if (arr[mid] == x){
                return mid;}

            // the element is present in the left subarray
           else if (arr[mid] > x){
                r = mid - 1;}

            // the element is present in the right subarray
            else{
                l = mid + 1;}
        }

        // the element is not present in the array
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
