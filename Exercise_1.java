class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
         //Write your code here
         if(l<=r){
            if(x == arr[(l+r)/2])
                return (l+r)/2;
            if(x < arr[(l+r)/2])
                return binarySearch(arr, l, (l+r)/2 - 1, x);
            if(x > arr[(l+r)/2])
                return binarySearch(arr, (l+r)/2 + 1, r, x);
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

// Time Complexity : O(logN)
// Space Complexity : O(logN)
// Did this code successfully run on Leetcode : yes
// Any problem you faced while coding this : no
