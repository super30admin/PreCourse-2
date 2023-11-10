//Time complexity : O(log(n))

package precourse2;


public class BinarySearch {

	int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
//		l=0;
//		r = arr.length - 1;
		int mid= l + (r-l)/2;
		while (l <= r) {
			mid= l + (r-l)/2;
			if (arr[mid]==x) {
				return mid;
			}
			else if (arr[mid]<x) {
				l=mid+1;
			}
			else {
				r=mid-1;
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
        int x = 2; 
        int result = ob.binarySearch(arr, 0, n - 1, x); 
        if (result == -1) 
            System.out.println("Element not present"); 
        else
            System.out.println("Element found at index " + result); 
    } 

}

