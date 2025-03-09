// Time Complexity :O(nlogn)
// Space Complexity :O(n)
// Did this code successfully run on Leetcode :
// Any problem you faced while coding this :


// Your code here along with comments explaining your approach
import java.util.ArrayList;

class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here
       ArrayList<Integer> d= new ArrayList<>();
       int i=l;
       int j=m+1;
       while(i<=m && j<=r)
       {
        if(arr[i]<=arr[j]){
            d.add(arr[i]);
            i++;
        }
        else{
            d.add(arr[j]);
            j++;
        }
        }
        while (i<=m) {
            d.add(arr[i]);
            i++;
        }
        while (j<=r){
            d.add(arr[j]);
            j++;
        }
        for(int k=l;k<=r;k++){
            arr[k]=d.get(k-l);
        }
        
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 
        if(l>=r) return;
        int m=(l+r)/2;
        sort(arr,l,m);
        sort(arr,m+1,r);
        merge(arr,l,m,r);
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