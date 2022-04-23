// Time Complexity :O(logn)(base 2) as we are dividing our array to half everytime;where n =no.of elements in array
// Space Complexity :O(1)constant(we are not using any extra space)
// Did this code successfully run on Leetcode :NA
// Any problem you faced while coding this :no
class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1
    int binarySearch(int arr[], int l, int r, int x) {
        int start = l;
        int end = r;
        // assigning values to start and end(we can use l and r directly too)
        while (start <= end) {// making sure we dont get caught up in infinite loop using this condition
            // and all indices will be checked at start==end

            int mid = start + (end - start) / 2;// using this instead of start+end to avoid integer out of range error
            if (arr[mid] == x) {// if we found the element, we'll simply return the index
                return mid;
            }
            if (arr[mid] < x) {// else there are these two conditions, if element at index mid is greater than
                               // target,
                // means we have to go left so we'll set our end to mid-1 else set start to
                // mid+1 as target is smaller
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }
        // Write your code here
        return -1;// return -1 if element is not found
    }

    // Driver method to test above
    public static void main(String args[]) {
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

// ------------------BRUTE
// FORCE----------------------------------------------------
// Time Complexity :O(n) as we are traversing through the while array
// Space Complexity :O(1)constant(we are not using any extra space)
// Did this code successfully run on Leetcode :NA
// Any problem you faced while coding this :no
class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1
    int binarySearch(int arr[], int l, int r, int x) {
        // we'll traverse until target is found
        for (int i = 0; i < r; i++) {
            if (arr[i] == x) {
                return i;
            }
        }
        // Write your code here
        return -1;// return -1 if element is not found
    }

    // Driver method to test above
    public static void main(String args[]) {
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
