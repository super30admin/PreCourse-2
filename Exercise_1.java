// Time Complexity : O(log n)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : 
// Initially had an issue with the mid calculation and misplaced braces,
// but after fixing those, the logic worked correctly.



// I used an iterative Binary Search approach. In each iteration, I compute
// the mid index and compare the middle element with the target.
// - If arr[mid] equals the target, I return mid.
// - If the target is smaller, I move the right pointer to mid - 1.
// - If the target is larger, I move the left pointer to mid + 1.
// I continue this until left > right. If no match is found, I return -1.
class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
       while(l <= r){
	      int mid = l +(r-1)/2;
	     
	     if (arr[mid]==x){
		    return mid;
		   //Write your code here
    } 

	    if (arr[mid] > x){
		    r = mid -1;
	    }
	    else{
		    l=mid + 1;
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
