class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here
        if(arr[m] <= arr[m+1]){
            return;
        }
       int[] temp = new int[r-l+1];

       int i = l;
       int j = m+1;
       int index = 0;

       while(i < m+1 && j < r+1){
           temp[index++] = arr[i] <= arr[j] ? arr[i++] : arr[j++];
       }

       if(i<=m){
           for(int k=l+index;k<r+1;k++){
               temp[k] = arr[i++];
           }
       }

       int ind = 0;
       for(int k=l;k<r+1;k++){
           arr[k] = temp[ind++];
       }

    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here
        if(l == r){
            return;
        }
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
        int arr[] = {12, 11, 13, 5, 6};
  
        System.out.println("Given Array"); 
        printArray(arr); 
  
        MergeSort ob = new MergeSort(); 
        ob.sort(arr, 0, arr.length-1); 
  
        System.out.println("\nSorted array"); 
        printArray(arr); 
    } 
} 