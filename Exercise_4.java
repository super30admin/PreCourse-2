class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here
       int n1 = m-l+1;
       int n2 = r-m;

       int[] left = new int[n1];
       int[] right = new int[n2];

       for(int i=0; i<left.length; i++){
           left[i] = arr[l+i];
       }
       for(int i=0; i<right.length; i++){
           right[i] = arr[m+1+i];
       }
       int k=l;
       int i=0, j=0;
       while(i<n1 && j<n2){
           if(left[i]<=right[j]){
               arr[k] = left[i];
               k++;
               i++;
           }
           else{
               arr[k] = right[j];
               k++;
               j++;
           }
       }

       while(i<n1){
           arr[k] = left[i];
           k++;
           i++;
       }
       while(j<n2){
           arr[k] = right[j];
           k++;
           j++;
       }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        if(l<r){
            int mid = (l+r)/2;
            sort(arr, l, mid);
            sort(arr, mid+1, r);
            //Call mergeSort from here
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
  
        System.out.println("Given Array"); 
        printArray(arr); 
  
        MergeSort ob = new MergeSort(); 
        ob.sort(arr, 0, arr.length-1); 
  
        System.out.println("\nSorted array"); 
        printArray(arr); 
    } 
} 