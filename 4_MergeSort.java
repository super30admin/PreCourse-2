// Time Complexity : O(nlogn)
// Space Complexity : O(n)

// Your code here along with comments explaining your approach
class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
        int[] merged = new int[r-l+1];
        int idx = 0;
        int leftIdx = l;
        int rightIdx = m+1;
        while(leftIdx<=m&&rightIdx<=r){
            if(arr[leftIdx]<=arr[rightIdx])
                merged[idx++] = arr[leftIdx++];
            else 
                merged[idx++] = arr[rightIdx++];
        }
        while(leftIdx<=m)
            merged[idx++] = arr[leftIdx++];
        while(rightIdx<=r)
            merged[idx++] = arr[rightIdx++];
        idx=0;
        for(int i=l;i<=r;i++){
            arr[i] = merged[idx++];
        }
        
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 
        if(l<r){
            int mid = l + (r-l)/2;
            sort(arr, l, mid);
            sort(arr, mid+1, r);
            merge(arr, l, mid, r);
        }
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
        ob.sort(arr, 0, arr.length-1); 
  
        System.out.println("\nSorted array"); 
        printArray(arr); 
    } 
} 