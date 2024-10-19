// Time Complexity: o(logn)
// Space Complexity: o(1)

class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
        while (l<=r){
            int m = l + (r-l)/2;

            // check if x is present at mid
            if (arr[m] == x)
                return m;

            // check if x is greater than mid
            // then ignore left half
            if (arr[m] < x)
                l=m+1;
            else
                // ignore right half
                r=m-1;
        }
        // element not present
        return -1
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
