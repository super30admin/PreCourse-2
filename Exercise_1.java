
/*
 * * Time Complexity: O(log n)
 * 
 * Space Complexity: O(n)
 * 
 * This code will run successfully on Leetcode
 * 
 * Any problems you face while coding this - No
 * 
 * Approach: 
 * 1. find mid of array (assuming array is sorted).
 * 2. check if element at mid point index in array is equal to element we are searching, if yes we found the element we looking for so we return index mid
 * 3. Else two possibilities, element at mid index is greater than element target or less than target element
 * 4. if element at mid is greater than target then all elements ahead of mid index are also greater than target including mid index element
 * 	  as array is sorted so no point in searching ahead of mid index so we make r pointer to mid - 1 and continue search
 * 5. if element at mid index is less than target then all elements coming before mid index are also small than target
 *    as array is sorted including element at mid index so no point in looking at element coming before mid 
 *    so make l = mid + 1 and continue our search
 * 6. We continue our search till l < r, as soon as l becomes greater than r, we can be sure that
 * 	  target element is not in array so we return -1.
 *
 */


class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
    	while(l <= r) {
    		
    		int mid = l + (r - l) / 2;
    		
    		if(arr[mid] == x)return mid;
    		else if(arr[mid] < x) {
    			l = mid + 1;
    		}else if(arr[mid] > x) {
    			r = mid - 1;
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
        int x = 40; 
        int result = ob.binarySearch(arr, 0, n - 1, x); 
        if (result == -1) 
            System.out.println("Element not present"); 
        else
            System.out.println("Element found at index " + result); 
    } 
} 