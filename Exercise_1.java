class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1
    int binarySearch(int arr[], int l, int r, int x)
    {
        //Write your code here

        /*   Time Complexity : O(log n) because each time we are reducing search size by half
         *    Space Complexity: O(1) we are not taking any extra space to search given array.
         * */

        if(r >= l){
            int mid = l + (r-l) / 2;
            if(arr[mid] == x)
                return mid;
            else if (x > arr[mid])
                return binarySearch(arr, mid+1, r, x);
            else
                return binarySearch(arr, l, mid-1, x);
        }
        return -1;
    }

    // Driver method to test above
    public static void main(String args[])
    {
        BinarySearch ob = new BinarySearch();
        int arr[] = { 2, 3, 4, 10, 40 };
        int n = arr.length;
        int x = 3;
        int result = ob.binarySearch(arr, 0, n - 1, x);
        if (result == -1)
            System.out.println("Element not present");
        else
            System.out.println("Element found at index " + result);
    }
}
