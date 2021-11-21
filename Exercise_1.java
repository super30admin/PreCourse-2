// Time Complexity: O(logn), as the number of elements to be checked are halved on every recursive call to the binarySearch function
//Space Complexity: Constant Order,as except for a few place holder variables no extra space is created

import java.util.Arrays; // importing this for Arrays.sort() method
class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1
    int binarySearch(int arr[], int l, int r, int x)
    {
        //Write your code here
        if( r >= l){ //check of r is greated than or equal to l
            int mid = l + (r-l)/2; // calculate mid. we are calculating it l+(r-l)/2 to prevent overflow
            if(arr[mid] == x) // if element is found at mid return mid
                return mid;
            if(arr[mid] > x) // check if the element is smaller than the value at mid, if so the the element should be on the first half of the current array partition, as we have sorted the array
                return binarySearch(arr, l, mid-1, x);
            else if(arr[mid] < x) // else element should be present in the other half
                return binarySearch(arr, mid+1, r, x);
        }
        return -1; // if element is not found return -1
    }

    // Driver method to test above
    public static void main(String args[])
    {
        BinarySearch ob = new BinarySearch();
        int arr[] = { 2, 3, 4, 10, 40 };
        int n = arr.length;
        int x = 10;
        Arrays.sort(arr); // making sure array is sorted as for binary search we expect the array to be sorted.
        int result = ob.binarySearch(arr, 0, n - 1, x);
        if (result == -1)
            System.out.println("Element not present");
        else
            System.out.println("Element found at index " + result);
    }
}
