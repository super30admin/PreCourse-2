// Time Complexity : O(log(n))
// Space Complexity : O(log(n))
// Any problem you faced while coding this : //finding mid point optimally, if-else not put properly, return stmt not used properly


class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        if (r >= l) {
        //Write your code here
        int m = l+ (r-l)/2;
        if(arr[m]== x)
        {
            return m;
        }
        if (arr[m]>x)
        {
            return binarySearch(arr, l,m-1,x);
        }
        else{
            return binarySearch(arr, m+1,r,x);
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
