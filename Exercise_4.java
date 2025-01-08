class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  

       //Your code here
       int n1 = m+1-l; // left array length
       int n2 = r-m; // right array length
       int larr[] = new int[n1];
       int rarr[] = new int[n2];

       for(int x=0;x<n1;x++){
        larr[x] = arr[l+x]; // copying left array
       }
       for(int x=0;x<n2;x++){
        rarr[x] = arr[m+1+x]; // copying right array
       }
       int i=0,j=0,k=l;

       while(i<n1 && j<n2){
        if(larr[i]<=rarr[j]){ // comparing left and right array
            arr[k++]=larr[i++]; // updating acutal array
        }
        else{
            arr[k++]=rarr[j++];
        }
       }

       while(i<n1){
        arr[k++]=larr[i++]; // remainder is added
       }
       while(j<n2){
        arr[k++]=rarr[j++];
       }

    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 
        if(l<r){
            int mid=l+(r-l)/2;
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
  
        System.out.println("Given Array"); 
        printArray(arr); 
  
        MergeSort ob = new MergeSort(); 
        ob.sort(arr, 0, arr.length-1); 
  
        System.out.println("\nSorted array"); 
        printArray(arr); 
    } 
} 