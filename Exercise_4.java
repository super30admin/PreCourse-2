class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       int sa1 = m-l+1;
       int sa2 = r-m;
       
       int L[] = new int[sa1];
       int R[] = new int[sa2];

       for(int i=0;i<sa1;i++){
           L[i] = arr[l+i];
       }
       for(int i=0;i<sa2;i++){
           R[i] = arr[m+1+i]; 
       }

       int a = 0;
       int b = 0;
       int c = l;

       while(a<sa1 && b<sa2){
           if(L[a] <= R[b]){
               arr[c] = L[a];
               a++;
           }
           else{
               arr[c] = R[b];
               b++;
           }
           c++;
       }
       while(a<sa1){
           arr[c] = L[a];
           a++;
           c++;
       }

       while(b<sa2){
           arr[c] = R[b];
           b++;
           c++;
       }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
        if(l<r){
            int m = (l+r)/2;

            sort(arr, l, m);
            sort(arr, m+1, r);

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