class MergeSort 
{ 
    // Time Complexity : O(NlogN)
// Space Complexity : O(N)
// Did this code successfully run on Leetcode :
// Any problem you faced while coding this : No


    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
       int[] b = new int[r-l+1];
       int p1 = l;
       int p2 = m+1;
       int i=0;
       
       while((p1 <= m) && (p2 <= r)){
           if(arr[p1] <= arr[p2]){
               b[i] = arr[p1];
               p1++;
           }
           else{
               b[i] = arr[p2];
               p2++;
           }
           i++;
       }
       for(int j=p1;j<=m;j++){
           b[i] = arr[j];
           i++;
       }
       for(int j=p2;j<=r;j++){
           b[i] = arr[j];
           i++;
           
       }
       for(int k =l;k<(r-l+1);k++){
           arr[k] = b[k];
       }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 
        if(l>=r){
            return;
        }
        else{
            int m = (l+r)/2;
            sort(arr,l,m);
            sort(arr,m+1,r);
            merge(arr,l,m,r);
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