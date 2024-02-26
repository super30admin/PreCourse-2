class BinarySearch {
    // Time Complexity : O(log n)
    // Space Complexity : O(n), because it is recursive and so it used stack to store results.
    //                      By default, it needs space equal to height of recursion which will be O(log n) and so
    // Did this code successfully run on Leetcode :
    // Any problem you faced while coding this :

    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int left, int right, int key)
    {
        int mid = (left+right)/2;
        if(arr[mid] == key){
            return mid; // found the element
        }
        // when there is crossover then return -1, key not found
        if(left > right){
            return -1;// key not present
        }
        if(arr[mid] > key) {
            right = mid - 1; //key is smaller than arr[mid] move left
            return binarySearch(arr, left, right, key);
        } else {
            // equal condition is already checked above so only left condition is arr[mid] < key
            // in that case we have to move right
            left = mid + 1;
            return binarySearch(arr, left, right, key);
        }
    }

    // Driver method to test above
    public static void main(String args[])
    {
        BinarySearch ob = new BinarySearch();
        int arr[] = { 2, 3, 4, 10, 40 };
        int n = arr.length;
        int key = 10;
        int result = ob.binarySearch(arr, 0, n - 1, key);
        if (result == -1)
            System.out.println("Element not present");
        else
            System.out.println("Element found at index " + result);

        // test: 2
        key = 50;
        result = ob.binarySearch(arr, 0, n - 1, key);
        if (result == -1)
            System.out.println("Element not present");
        else
            System.out.println("Element found at index " + result);
    }
} 
