class Exercise_4 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       int llength = m-l+1;
       int rlength = r-m;
       
       int larr[]=new int[llength];
       int rarr[]=new int[rlength];

       for(int i=0;i<llength;i++){
        larr[i]=arr[l+i];
       }
       for(int j=0;j<rlength;j++){
        rarr[j]=arr[m+1+j];
       }

       int i=0,j=0,index=l;
       while(i<llength && j<rlength){
        if(larr[i]<=rarr[j]){
            arr[index]=larr[i];
            i++;
        }else{
            arr[index]=rarr[j];
            j++;
        }
        index++;
       }

       while(i<llength){
        arr[index]=larr[i];
        i++;
        index++;
       }

       while(j<rlength){
        arr[index]=rarr[j];
        j++;
        index++;
       }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
        if(l<r){
            int m = l+r/2;
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
  
        Exercise_4 ob = new Exercise_4(); 
        ob.sort(arr, 0, arr.length-1); 
  
        System.out.println("\nSorted array"); 
        printArray(arr); 
    } 
} 