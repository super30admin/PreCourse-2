// Time Complexity : O(nlogn)
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No
class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
       int k1 = m - l + 1;
       int k2 = r - m;
       
       int left[] = new int[k1];
       int right[] = new int[k2];

       for(int i=0;i<k1;i++)
          left[i]= arr[l+i];
       for(int j=0;j<k2;j++)
          right[j] = arr[m+1+j];
       int x=0,y=0;
       int t = l;
       while(x<k1 && y<k2){
           if(left[x]<=right[y]){
               arr[t] = left[x];
               x++;
           }
           else
           {
               arr[t] = right[y];
               y++;
           }
           t++;
       }
       while(x<k1){
           arr[t] = left[x];
           x++;
           t++;
       }
       while(y<k2){
           arr[t] = right[y];
           y++;
           t++;
       }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 
        if(l<r)
        {
            int mid = l +(r-l)/2;
            sort(arr, l,mid);
            sort(arr, mid+1,r);
            merge(arr,l,mid,r);
        }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 
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