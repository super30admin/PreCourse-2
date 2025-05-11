//Time Complexity: O(nlogn)
//Space Complexity: O(n)
class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
        //Your code here  
        int arr2[] = new int[r-l+1];
        if(l==r){
            return;
        }
        int i=l, j=m+1, k=0;
        while(i<m+1 && j<r+1){
            if(arr[i]<=arr[j]){
                arr2[k++] = arr[i];
                i=i+1;
            }
            else{
                arr2[k++] = arr[j++];
            }
        }
        while(i<=m){
            arr2[k++] = arr[i++];
        }
        while(j<=r){
            arr2[k++] = arr[j++];
        }
        k=0;
        for(int x=l;x<=r;x++){
            arr[x] = arr2[k++];
        }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 
        if(l<r){
            int mid = l + (r-l)/2;
            sort(arr, l, mid);
            sort(arr, mid+1, r);
            merge(arr, l, mid, r);
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
        //int arr[] = {9, 8, 7, 6, 5, 4, 3, 2, 1};
        System.out.println("Given Array"); 
        printArray(arr); 
  
        MergeSort ob = new MergeSort(); 
        ob.sort(arr, 0, arr.length-1); 
  
        System.out.println("\nSorted array"); 
        printArray(arr); 
    } 
} 