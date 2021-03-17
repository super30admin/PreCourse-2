class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //printArray(arr);
       //Your code here  
       System.out.println(" l "+ l+" r "+r +" m "+ m);
       int x = m - l + 1;
       int y = r - m;

       int L[] = new int[x];
       int R[] = new int[y];

       for(int i = 0; i < x ; i++){
           L[i] = arr[l + i];
       }
       for(int j = 0; j < y ; j++){
           R[j] = arr[m + 1 + j];
       }
       System.out.print("left array ");
       printArray(L);
       System.out.print("Right array ");
       printArray(R);

    
       
       //printArray(arr);
       int i = 0,j = 0;

       int k = l;

       while( i < x && j < y){
           if(L[i] <= R[j]){
               arr[k] = L[i];
               i++;
           }
           else{
               arr[k] = R[j];
               j++;
           }
           k++;

       }
       while( i < x){
           arr[k] = L[i];
           i++;
           k++;
       }
       while(j < y){
           arr[k] = R[j];
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
        if(l < r){
           int m = l + (r-l)/2;
           //printArray(arr);
           sort(arr, l, m);
           sort(arr, m + 1, r);
           //printArray(arr);
           //System.out.println(" l "+ l+" r "+r +" m "+ m);
           merge(arr, l, m, r);


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