// Time Complexity: O(log n)
// Space Complexity: O(1)
// This is an implementation of the Binary Search algorithm in Java
// It searches an element in sorted array
class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1
    int binarySearch(int arr[], int l, int r, int x)
    {
        if(l > r){
            return -1;
        }
        //Write your code here
        int mid = (l + r) / 2;
        if(arr[mid] == x){
            return mid;
        }
        else if(arr[mid] < x){
            return binarySearch(arr, mid + 1, r, x);
        } else if(arr[mid] > x){
            return binarySearch(arr, l, mid - 1, x);
        }

        return -1;
    }

    // Driver method to test above
    public static void main(String args[])
    {
        BinarySearch ob = new BinarySearch();
        int arr[] = { 2, 3, 4, 10, 40 };
        int n = arr.length;
        int x = 11;
        int result = ob.binarySearch(arr, 0, n - 1, x);
        if (result == -1)
            System.out.println("Element not present");
        else
            System.out.println("Element found at index " + result);
    }
}