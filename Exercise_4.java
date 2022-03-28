// Time Complexity : O(NlogN)
// Space Complexity : O(N)
// Did this code successfully run on Leetcode :
// Any problem you faced while coding this : No

class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    int []merge(int first[], int second[]) 
    {  
        int result[] = new int[first.length + second.length];
        
        int i=0,j=0,k=0;
        while(i < first.length && j < second.length) {
            if(first[i]  <= second[j]) {
                result[k++] = first[i++]; 
            } else {
                result[k++] = second[j++];
            }
        }
        
        while(i < first.length) {
            result[k++] = first[i++]; 
        }
        
        while(j < second.length) {
            result[k++] = second[j++];
        }

        return result;
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    int []sort(int arr[], int l, int r) 
    { 
        if(l == r) {
            int []base = new int[1];
            base[0] = arr[l];
            return base;
        }
        
        int mid = l+(r-l)/2;
        int first[] = sort(arr, l ,mid);
        int second[] = sort(arr, mid+1, r);
        arr = merge(first, second);

        return arr;
    } 
  
    /* A utility function to print array of size n */
    static void printArray(int arr[]) 
    { 
        int n = arr.length; 
        for (int i=0; i<n; ++i) 
            System.out.print(arr[i] + " "); 
        System.out.println(); 
    } 
  
    // Driver method 
    public static void main(String args[]) 
    { 
        int arr[] = {12, 11, 13, 5, 6, 7}; 
  
        System.out.println("Given Array"); 
        printArray(arr); 
  
        MergeSort ob = new MergeSort(); 
        arr = ob.sort(arr, 0, arr.length-1); 
  
        System.out.println("\nSorted array"); 
        printArray(arr); 
    } 
} 