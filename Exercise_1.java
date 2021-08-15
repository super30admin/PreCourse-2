
// Time Complexity: O(log n)
// Space Complexity: O(log n)
// Did this code successfully run on Leetcode:
//Any problems you faced while coding this:

class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    {

        int m = l + (r-l) / 2;
        while(l<r){
            if (x == arr[m]){
                return m;
            }
            if (x < arr[m]){
                return binarySearch(arr, l, m-1, x);
            }
            else{
                return binarySearch(arr,m+1, r, x);

            }
        }
        return -1;
        //Write your code here
    } 
  
    // Driver method to test above 
    public static void main(String args[]) 
    { 
        BinarySearch ob = new BinarySearch(); 
        int arr[] = { 2, 3, 4, 30, 40 };
        int n = arr.length; 
        int x = 2;
        int result = ob.binarySearch(arr, 0, n - 1, x); 
        if (result == -1) 
            System.out.println("Element not present"); 
        else
            System.out.println("Element found at index " + result); 
    } 
} 
