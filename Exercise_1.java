// Time Complexity : O(log n)
// Space Complexity :  O(1) if the Array is provided, O(n) if not
// Did this code successfully run on Leetcode : Y
// Any problem you faced while coding this : N

class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
      

        while(l>=0 && r<arr.length && l<=r)
        {
            int middle = l + (r-l)/2;

            if(arr[middle] == x)
            return middle;
            if(arr[middle]>x)
            {
                r=middle-1;
            }
            else l=middle+1;

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
