//Considering that the array is sorted 

// Time Complexity : O(log n)
// Space Complexity : O(log n) (recursive approach)due to call stack, O(1) (Iterative approach)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No

class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
        //Recursive Approach
        /* In this approach we will calculate mid and then we will check if the element == arr[mid] if yes then we will return mid
         * If the element is less than arr[mid] then we will make a recursive call  where r = mid-1
         * If the element is greater than arr[mid] then we will make a recursive call where l = mid+1 
         * If the element is not found return -1
         * If at any moment l>r == true then it means the element is not present in the array and we will return -1
         */
        /*
        if(l > r) return -1;

        int mid = l+ (r-l)/2;

        if(x == arr[mid]){
            return mid;
        }
        else if(x<arr[mid]){
            return binarySearch(arr, l, mid-1, x);
        }
        else if(x > arr[mid]){
            return binarySearch(arr, mid+1, r, x);
        }
        return -1; */

        // Iterative Approach:
        /* In this approach we will run a while loop till l<=r  and we will calculate mid in every iteration
         * If x = arr[mid] ten we will return mid index
         * If x < arr[mid] then we will update the value of r to mid-1. 
         * If x > arr[mid] then we will update the value of l to mid +1
         * If the element is not found return -1
        */

        while(l <= r){
            int mid = l + (r-l)/2;

            if(x == arr[mid]){
                return mid;
            }

            else if(x < arr[mid]){
                r = mid-1;
            }

            else if(x > arr[mid]){
                l = mid +1;
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
