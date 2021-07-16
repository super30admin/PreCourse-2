class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        /*
            Time Complexity:
            - In the best case it is o(1)
            - In the worst case it is o(logn)
         */
        //For binary search- the array should be always sorted. we cannot do binary search with unsorted array.
        //since the array is sorted. The lest side element of array should be always less than right element of array
        if (l < r) {
            //find the mid element
            int middleElement = l + (r-1)/2;

            //case-1: if data == a[mid] then return mid
            if (x == arr[middleElement]) {
                return middleElement;
            }
            /*
                case-2: if data < a[mid] then:
                - left position remains the same
                - shift right = mid -1
                -  pass the array
             */
            if (x < arr[middleElement]) {
                return binarySearch(arr, l, middleElement-1, x);
            }
            /*
                case-3: if data > a[mid] then:
                - shift left = mid +1
                - right position remains the same
                -  pass the array
             */
            if (x > arr[middleElement]) {
                return binarySearch(arr, middleElement +1, r, x);
            }
        }

        //we reach here when the element is not present in the array.
        System.out.println("given element not present in the array");
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
