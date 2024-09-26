// Time Complexity :O(nlogn)
// Space Complexity :O(n)
// Did this code successfully run on Leetcode :
// Any problem you faced while coding this :


// Your code here along with comments explaining your approach


class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
       int n1 = m-l+1;  // size of left array
       int n2 = r-m;    // size of right array
       //initialize 2 temp arrays left and right
       int[] left = new int[n1];
       int[] right = new int[n2];
       //Populate the left and right arrays
       for(int a = 0;a<n1;a++){
           left[a]=arr[l+a];
       }
       for(int b = 0;b<n2;b++){
           right[b]=arr[m+b+1];
       }

       int i=0;
       int j=0;
       int k=l;//pointer for main array
       //Compare the two arrays
       while(i<n1 && j<n2){
           if(left[i]<=right[j]){
               arr[k]=left[i];
                i++;
           }
           else{
               arr[k]=right[j];
               j++;
           }
           k++;
       }
       //If one array ends 
       while(i<n1){
           arr[k]=left[i];
           i++;
           k++;
       }
       while(j<n2){
           arr[k]=right[j];
           j++;
           k++;
       }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 
        if(l<r){
            int mid = (r+l)/2;
            sort(arr,l,mid);
            sort(arr,mid+1,r);
            merge(arr,l,mid,r);
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