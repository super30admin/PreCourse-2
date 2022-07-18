// Time Complexity : O(nlogn) as we need to divide array everytime into half log(n) and then to merge n
// Space Complexity : O(n) we are using a temp array
// Did this code successfully run on Leetcode : yes
// Any problem you faced while coding this : yes needed to refer how does merge sort work



class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       int[] temp = new int[r-l+1];
        int i = l;
        int j = m +1;
        int c=0;
        while(i<=m && j<=r){
            if(arr[i]<arr[j]){
                temp[c] = arr[i];
                i++;
            }
            else {
                temp[c] = arr[j];
                j++;
            }
            c++;
        }
        while(i<=m){
            temp[c] = arr[i];
            i++;
            c++;
        }
        while(j<=r){
            temp[c] = arr[j];
            j++;
            c++;
        }
        c=0;
        for(int k=l;k<=r;k++) {
            arr[k] = temp[c];
            c++;
        } 
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
    	if(l>=r)
            return;
        int mid = l + (r-l)/2;
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
