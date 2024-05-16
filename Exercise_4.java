/**
 *
 * Time Complexity : O(mlog(n))
 * Space Complexity : O(n)
 *
 */
import java.util.ArrayList;

class MergeSort
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here
        ArrayList<Integer>temp = new ArrayList<>();
        int lp = l;
        int rp = m+1;
        while(lp<=m && rp<=r){
            if(arr[lp]<=arr[rp]){
                temp.add(arr[lp]);
                lp++;
            }else{
                temp.add(arr[rp]);
                rp++;
            }
        }
        while (lp<=m){
            temp.add(arr[lp]);
            lp++;
        }
        while (rp<=r){
            temp.add(arr[rp]);
            rp++;
        }

        for(int i=l;  i<=r; i++){
            arr[i] = temp.get(i - l);
        }
    }

    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here
        if(l>=r)
            return;
        int mid = (l+r)/2;
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