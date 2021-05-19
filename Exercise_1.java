class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int a[], int l, int r, int x)
    { 
        //Write your code here
        if(l >= r) {
            return -1;
        }
        int m = l + (r - l) / 2;
        if(a[m] == x) {
            return m;
        } else if(a[m] > x) {
            return binarySearch(a, l, m - 1, x);
        }
        return binarySearch(a, m + 1, r, x);
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