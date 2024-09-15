class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x)
    {
        //create variables and set index value to -1
        int mid;
        int index = -1;

        while(l <= r){
            //calculate mid point of array
            mid = (l+r)/2;

            //set l value to one more than mid point valye if x is not in left side
            if(arr[mid] < x){
                l=mid+1;
                //set r value to 1 less than mid value if x is not in the right side
            } else if(arr[mid] > x){
                r = mid -1;
                //set index value if x is found in array
            } else if(arr[mid] == x){
                index = mid;
                break;
            }
        }
        return index;
    }

    //1 2 3 4 5 69 703 309 52

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
