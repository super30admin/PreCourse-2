class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) {

        //fins mid value and if it x is less than mid value then search in left subtree or else search in right subtree
        int mid = arr.length / 2;
        if (x == arr[mid]) {
            return mid;
        }
        if (x < arr[mid]) {
            for (int i = 0; i < mid; i++) {
                if (x == arr[i]) {
                    return i;
                }
            }
        } else {
            for (int i = mid+1; i < arr.length; i++) {
                if (x == arr[i]) {
                    return i;
                }
            }
        }
        //if element is not found then return -1

        return -1;
    }

    // Driver method to test above 
    public static void main(String args[]) {
        BinarySearch ob = new BinarySearch();
        int arr[] = {2, 3, 4, 10, 40};
        int n = arr.length;
        int x = 10;
        int result = ob.binarySearch(arr, 0, n - 1, x);
        if (result == -1)
            System.out.println("Element not present");
        else
            System.out.println("Element found at index " + result);
    }

    // Time Complexity - O(n/2)
    //Space Complexity - O(1)
} 
