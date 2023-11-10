// time complexity 0(logn)
// space complexity 0(n)

class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1
    int binarySearch(int arr[], int l, int r, int x)
    {
        // to traverse the array
        for(int i=0;i<arr.length;i++)
        {
            // calculate the mid
            int mid=((l+r)/2);
            // if x = midle element just return the index
            if(arr[mid]==x)
            {
                return mid;
            }
            // if search element is greater than mid start searching from mid+1
            if(arr[mid]<x)
            {
                l=(mid+1);
            }
            // if searching element is small than mid  search only till mid-1
            else
            {
                r=(mid-1);
            }


        }
        // not found -1
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