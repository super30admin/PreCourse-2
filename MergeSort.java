/*
TimeComplexity: O(nlogn)
SpaceComplexity: O(n) // For temp array
 */
class MergeSort
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {
        //last element of left partition(m-1) if it is less than or equal to first element of right partition,
        // no need to put to temp
       if(arr[m-1]<=arr[m]){
           return;
       }
       int i = l;
       int j = m;
       int tempIndex = 0;

       int temp[] = new int[r-l];
       while(i<m && j<r){
           temp[tempIndex++] = arr[i] <= arr[j] ? arr[i++] : arr[j++];
       }
       System.arraycopy(arr,i,arr, l + tempIndex, m-i);
       System.arraycopy(temp,0,arr,l,tempIndex);
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	    //break condition
        if(r - l < 2)
            return;
        //logical partition
        int mid = (l + r )/2;
        sort(arr,l,mid);
        sort(arr,mid,r);
        merge(arr,l,mid,r);
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
        ob.sort(arr, 0, arr.length);
  
        System.out.println("\nSorted array"); 
        printArray(arr); 
    } 
} 