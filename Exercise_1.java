class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1
    // Time Complexity : O(logn) given that array is sorted.
    // Space Complexity : O(n) n elements in an array
    // Any problem you faced while coding this : I forgot to check at l and r which was throwing a weird error.
    int binarySearch(int[] arr, int l, int r, int x)
    { 
        int mid = (l + r)/2;
        int ind = -1;
        if(arr[mid]==x){
            ind = mid;
        }
        else if(arr[l]==x){
            ind = l;
        }
        else if(arr[r]==x){
            ind = r;
        }
        else if(arr[mid]>x){
            ind = binarySearch(arr, mid+1, r-1, x);
        }
        else if(arr[mid]<x){
            ind = binarySearch(arr, l+1, mid-1, x);
        }
        return ind;
        //Write your code here
    } 
  
    // Driver method to test above 
    public static void main(String[] args)
    { 
        BinarySearch ob = new BinarySearch(); 
        int[] arr = { 2, 3, 4, 10, 40 };
        int n = arr.length; 
        int x = 10; 
        int result = ob.binarySearch(arr, 0, n - 1, x); 
        if (result == -1) 
            System.out.println("Element not present"); 
        else
            System.out.println("Element found at index " + result); 
    } 
} 
