// Time Complexity : O(log n)
// Space Complexity : O(log n)
// Did this code successfully run on Leetcode : yes
// Any problem you faced while coding this : no


/*Your code here along with comments explaining your approach
repeat till low <= high, find mid, if x == arr[mid] then return mid element or check further
if  x<mid element then x lies on right side of mid so reduce the right index, if x>mid then the element to be found is on the right so increase the left index

*
*/


class Exercise_1 { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
    	int mid;
    	 while(l<=r) {
    		 
    		 mid=(l+r)/2;
    		 
    		 if(arr[mid]==x) {
    			 return mid;
    		 }
    		 
    		 else if(arr[mid]>x) {
    		 r=mid-1;
    		 }
    		 
    		 else if(arr[mid]<x){
    			 l=mid+1;
    		 }
    		 
    	 }
    	 return -1;
    	
    
    } 
  
    // Driver method to test above 
    public static void main(String args[]) 
    { 
    	Exercise_1 ob = new Exercise_1(); 
        int arr[] = { 2, 3, 4, 10, 40 }; 
        int n = arr.length; 
        int x = 4; 
        int result = ob.binarySearch(arr, 0, n - 1, x); 
        if (result == -1) 
            System.out.println("Element not present"); 
        else
            System.out.println("Element found at index " + result); 
    } 
} 
