// Time Complexity : O(nlogn)
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : Yes, needed a complete refresher for merge sort algorithm. Also took some help after coding it. Also got confused with the space complexity and had to refer online
// Your code here along with comments explaining your approach
class MergeSort
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here

        int leftSubArraySize = m-l+1, rightSubArraySize = r-m;

        // Declare additional sub arrays for placing the elements and then merging later
        int[] leftSubArray = new int[leftSubArraySize];
        int[] rightSubArray = new int[rightSubArraySize];

        // copy the first sub array
        int a = 0;
        for(int k = l;k<=m;k++) {
            leftSubArray[a++] = arr[k];
        }

        // copy the second sub array
        a=0;
        for(int k = m+1;k<=r;k++) {
            rightSubArray[a++] = arr[k];
        }
        a=0; int b = 0;

        // copy both the sub arrays back to the main array with proper sorted pattern
        int i = l;
        while(a<leftSubArraySize && b<rightSubArraySize) {
            if(leftSubArray[a]<=rightSubArray[b]) {
                arr[i++] = leftSubArray[a++];
            } else {
                arr[i++] = rightSubArray[b++];
            }
        }

        // copy remaining elements back to the main arr
        while(a<leftSubArraySize) arr[i++] = leftSubArray[a++];
        while(b<rightSubArraySize) arr[i++] = rightSubArray[b++];
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here
        // If at all the sorting goes out of bounds, we return
        if(l>=r) return;

        // calculate midpoint for partitioning and then merging
        int mid = l+(r-l)/2;

        // sort the first part
        sort(arr, l, mid);

        //sort the second part
        sort(arr, mid+1, r);

        // merge the sorted sub arrays
        merge(arr, l, mid, r);
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
        int arr[] = {-1, 11, 13, 5, 6, -2};
  
        System.out.println("Given Array"); 
        printArray(arr); 
  
        MergeSort ob = new MergeSort(); 
        ob.sort(arr, 0, arr.length-1); 
  
        System.out.println("\nSorted array"); 
        printArray(arr); 
    } 
} 