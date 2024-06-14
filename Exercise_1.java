// Time Complexity : O(log n)
// Space Complexity : O(1)
class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here

        // assigning left and right variables
        l = 0;
        r = arr.length - 1;

        // this will evaluate until left is less than equal to right
        while(l <= r) {

            int mid = l + (r-l)/2;

            if (x == arr[mid])
                return mid;
            // if element is less than value of mid then evaluate left size of array from mid
            else if (x < arr[mid])
                r = mid - 1;
            // else evaluate right size of array from mid
            else {
                l = mid + 1;
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
