// Time Complexity : O(log n)
// Space Complexity : O(n) just for the array
// Your code here along with comments explaining your approach
/*
* I try to find the mid element iteratively until my left value gets less than or equal to right index
* If I find my target element dorectly at mid index, I return it, if not, I compare the value of target
* with value of mid to see and move my left, right indices to narrow the search criteria. Return -1 if
* target not found.
* */

class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
        while(l <= r) {
            int mid = l + (r - l) / 2;
            if(x == arr[mid])
                return mid;
            else if(arr[mid] < x)
                l = mid + 1;
            else
                r = mid - 1;
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
