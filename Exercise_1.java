// Time Complexity :
//      binarySearch() - O(log(n)) - everytime dividing the array into two parts for search
//      
// Space Complexity :
//      binarySearch() - O(1)
// Did this code successfully run on Leetcode : N/A
// Any problem you faced while coding this : No

class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
        while(l < r)
        {
            //find the middle element
            int m = (l + r) / 2;

            //check for convergence case
            if(arr[m] == x)
                return m;
            else if(arr[m] < x)
                l = m+1;
            else
                r = m-1;
        }
        //if not found return -1
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
            System.out.println(x +" not present"); 
        else
            System.out.println(x + " found at index " + result);  
    } 
} 
