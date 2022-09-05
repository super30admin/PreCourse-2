//Complexity: 
//Time : O(log n)
//Space : O(n)

class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
        //approach: check if the value of r is less than or equal to l, if it is less, return -1
        //get the mid index of l and r by rounding (l+r)/2
        //if mid index value is equal to x then return mid else if value at mid is less than or greater than x then call binary search recursively
        if(r<=l) {
            return -1;
        }
        int mid = (int)Math.round((l+r)/2);
        if(arr[mid] == x) {
            return mid;
        } else if(x > arr[mid]) {
            return binarySearch(arr, mid, r, x);
        } else {
            return binarySearch(arr, l, mid, x);
        }
        
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
