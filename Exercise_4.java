// TC: O(nlogn)
// SC: O(n)

class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
       int p1 = l,p2 = m+1;
       int temp[] = new int [r-l+1];
       int k=0;
       while(p1<=m && p2<=r)
       {
           if(arr[p1]<=arr[p2]){
               temp[k++] = arr[p1++];
           }
           else{
               temp[k++] = arr[p2++];
           }
       }
       while(p1<=m){
           temp[k++] = arr[p1++];
       }
       while(p2<=r){
           temp[k++] = arr[p2++];
       }
       for(int i=l;i<r+1;i++)
       {
           arr[i] = temp[i-l];
       }      
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
        if(l==r) return;
        int mid = l + (r-l)/2;
        sort(arr,l,mid);
        sort(arr,mid+1,r);
        merge(arr,l,mid,r);       
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