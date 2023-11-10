
// Time Complexity: O(log n)
// Space Complexity: O(1)

class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x)
    {
        //Write your code here
        if(l <= r)
        {
            int midpoint = l + (r - l)/2;

            if(arr[midpoint] == x)
            {
                return midpoint;
            }

            else if (arr[midpoint] < x) {
                return binarySearch(arr, midpoint+1, r, x);
            }

            else
            {
                r = midpoint - 1;
                return binarySearch(arr, l, midpoint-1, x);
            }
        }

        return -1; // Return -1 if element not found in the array
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
