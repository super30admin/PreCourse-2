class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
       int temp[] = new int[r-l+1];
       int i = l,j = m + 1,k =0;
       while(i <= m && j <= r)
       {
           if(arr[i] <= arr[j])
           {
               temp[k] = arr[i];
               k++;
               i++;
           }
           else
           {
               temp[k] = arr[j];
               k++;
               j++;
           }
       }
       
       while(i <= m){
           temp[k] = arr[i];
           k++;
           i++; 
       }
       while(j <= r){
           temp[k] = arr[j];
           k++;
           j++; 
       }
       
       for(i = l; i <= r;i++)
       {
           arr[i] = temp[i-l];
       }
       

    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 
        if(l < r)
        {
            int mid = l+(r-l)/2;
            sort(arr,l, mid);
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
//Time Complexity = O(n log n)
//Space Complexity = O(n)