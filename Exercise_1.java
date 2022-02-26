// Time Complexity : O(log(n))
// Space Complexity :using only extra one variable O(1)
// Did this code successfully run on Leetcode : yes
// Any problem you faced while coding this : no
//0 1 2 3 4 5 6 7 8 9 10
class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
        while(l<=r){
            int m = (l+r)/2;
            if(arr[m]==x)
                return x;
            if(x<arr[m]){
                r = m-1;
            }else{
                l = m+1;
            }  
        }
        return -1;

    } 
  
    // Driver method to test above 
    public static void main(String args[]) 
    { 
        BinarySearch ob = new BinarySearch(); 
        int arr[] = { 2, 3, 4, 6, 40 }; 
        int n = arr.length; 
        int x = 10; 
        int result = ob.binarySearch(arr, 0, n - 1, x); 
        if (result == -1) 
            System.out.println("Element not present"); 
        else
            System.out.println("Element found at index " + result); 
    } 
} 
