// Time Complexity :  O(nlogn)
// Space Complexity :   O(n)
// Did this code successfully run on Leetcode :  Yes
// Any problem you faced while coding this :  Was confused while merging the temporary arrays and then copying to the original array


// Your code here along with comments explaining your approach

class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
       int[] merged=new int[r-l+1];
       int i=l, j=m+1;
       int curr=0;
       while(i<=m && j<=r){
            if(arr[i]<=arr[j]){
                merged[curr++]=arr[i++];
            }
            else{
                merged[curr++]=arr[j++];
            }
        }
        while(i<=m){
            merged[curr++]=arr[i++];
        }
        while(j<=r){
            merged[curr++]=arr[j++];
        }
    
        for(int x=l, k=0; k<merged.length; x++, k++){
            arr[x]=merged[k];
        }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 

        if(l>=r){
            return;
        }
	//Write your code here
        //Call mergeSort from here 
        int mid=l+(r-l)/2;
        sort(arr,l,mid);
        sort(arr,mid+1,r);
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
        ob.sort(arr, 0, arr.length-1); 
  
        System.out.println("\nSorted array"); 
        printArray(arr); 
    } 
} 