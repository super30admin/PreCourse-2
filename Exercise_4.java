
//Time Complexity: O(n log n)
// Space Complexity: O(n)
//Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No
import java.util.ArrayList;

class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
       int left= l;
        int right = m+1;
        ArrayList<Integer> temp = new ArrayList<>();

       while(left<=m && right<=r){
            if(arr[left]<=arr[right])
            {
                temp.add(arr[left]);
                left++;
            }    
            else{
                temp.add(arr[right]);
                right++;
            }
       }
       while(left <= m)
       {
              temp.add(arr[left]);
              left++;
       }
        while(right <= r)
        {
                temp.add(arr[right]);
                right++;
        }
        for(int i=l; i<=r;i++)
        {
            arr[i] = temp.get(i-l);
        }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
        //Write your code here
        //Call mergeSort from here 
        if(l>=r) return;
            int m = l+(r-l)/2;
            sort(arr,l,m);
            sort(arr,m+1,r);
            merge(arr,l,m,r); // Add a semicolon at the end of this line
        
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