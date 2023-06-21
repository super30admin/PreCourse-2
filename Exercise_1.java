/*
    Time Complexity:
    O(log(n))->since the array is divided into two halves repetitively till we find
               an element

    Space Complexity->O(1)...we are not allocating extra space to store array elements

 */

class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    {

        int mid=0;
        while(l<=r) {

            //find mid of the array
            mid = l + (r - l) / 2;

           // compare mid-element with no to search
            //if found return mid
            if (arr[mid] == x) {
                return mid;
            } else if (arr[mid] > x) { //if mid element is greater than no,then no present
                                       //in left half,change right index
                r = mid - 1;
            } else if (arr[mid] < x) { //if mid element is greater than no,then no present
                                        //in right half,change left index
                l = mid + 1;
            }
        }
        return -1; //element not present
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
