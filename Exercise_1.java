//class BinarySearch { 
	public class Exercise_1 { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        //Write your code here
    	int res=-1;
    	int low,high,mid;
    	low=l;
    	high=r;
    	while(low<=high)
    	{
    		mid= low+(high-low)/2;
    		if(arr[mid]==x) return mid;
    		else if( arr[mid]<x) low=mid+1;
    		else {
    			high=mid-1;
    		}
    	}
    	
    	return res;
    } 
  
    // Driver method to test above 
    public static void main(String args[]) 
    { 
    	Exercise_1 ob = new Exercise_1(); 
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
// TC- O(logn)
//SC-O(1)