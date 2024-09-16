class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here
       
       int n_left=m-l+1;
       int n_right=r-m;
      

       int L[]=new int[n_left];
       int R[]=new int[n_right];


       for(int i=0;i<n_left;i++){
           L[i]=arr[l+i];

       }
       for(int i=0;i<n_right;i++){
           R[i]=arr[m+1+i];
       }
        int k=l;
       int i=0;
       int j=0;
       while(i<n_left && j<n_right){
           if(L[i]<=R[j]){
                arr[k]=L[i];
                i++;
           }
           else{
               arr[k]=R[j];
               j++;
           }
           k++;
        }

        while(i<n_left){
            arr[k]=L[i];
            i++;
            k++;
        }
        while(j<n_right){
            arr[k]=R[j];
            j++;
            k++;
        }
           
       }   
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 

        if(l<r){
            int mid=(l+r)/2;
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