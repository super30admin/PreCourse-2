class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x)
    {
        // Time Complexity : o(logn) --> middle index value : o(1)
        // Space Complexity : 0(n)

        //Write your code here
        if (arr == null) {
            return -1;
        }
        int halfLength = r / 2;
        if (arr[halfLength] < x) {
            while (halfLength <= r) {
                if (arr[halfLength] == x) {
                    return halfLength;
                }
                if (arr[halfLength] > x) {
                    return -1;
                }
                halfLength++;
            }
        } else if (arr[halfLength] > x) {
            while (halfLength >= l) {
                if (arr[halfLength] == x) {
                    return halfLength;
                }
                if (arr[halfLength] < x) {
                    return -1;
                }
                halfLength--;
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
