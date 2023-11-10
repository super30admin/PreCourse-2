// Time Complexity : It is O(Log(N)) since getting half everytime
// Space Complexity : Temp Var in Iterative, But Recursively function stack would grow I guess so space it will be required.
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : How would you decide between recursive and iterative ?
class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x)
    {
        //Write your code here
        // Calculating mid
        int mid = (l + r) / 2;
        System.out.println(" Var : l,r,mid : " + l + "," + r + "," + mid);

        if (l > r) {
            return -1;
        }
        if (x == arr[mid]) {
            // Elem found
            System.out.println("Found at " + mid);
            return mid;
        } else if (x > arr[mid]) {
            l = mid + 1;
            return binarySearch(arr, l, r, x);
        } else {
            r = mid - 1;
            return binarySearch(arr, l, r, x);
        }
    }

    public static int iterative_binarySearch(int arr[], int l, int r, int x) {
        while (l <= r) {
            int mid = (l + r) / 2;
            System.out.println(" Var : l,r,mid : " + l + "," + r + "," + mid);
            if (x == arr[mid]) {
                // Elem found
                System.out.println("Found at " + mid);
                return mid;
            } else if (x > arr[mid]) {
                l = mid + 1;
            } else {
                r = mid - 1;
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
            System.out.println("Element found at index Recursively " + result);

        // Iteratively
        result = ob.binarySearch(arr, 0, n - 1, x);
        if (result == -1)
            System.out.println("Element not present");
        else
            System.out.println("Element found at index Iteratively " + result);
    } 
} 
