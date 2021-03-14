class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
       int len1 = m-l+1;
       int len2 = r-m;

       int left[] = new int[len1];
       int right[] = new int[len2];

       for(int i =0;i<len1;i++){
           left[i] = arr[l+i];
       }

       for(int j =0;j<len2; j++){
           right[j] = arr[m+1+j];
       }

       int index1 =0; 
       int index2 =0;
       
       for(int i =l; i<r+1; i++){
           if(index1< len1 && index2<len2){
               if(left[index1]<right[index2]){
                   arr[i] = left[index1];
                   index1++;
               }
               else{
                   arr[i] = right[index2];
                   index2++;
               }
           }else if(index1 < len1){
               arr[i] = left[index1];
               index1++;
           }
           else if(index2 < len2){
               arr[i] = right[index2];
               index2++;
           }
       }
       

       

    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
        //Write your code here
        if(l<r){
            int mid = l+ (r-l)/2;
            
            sort(arr,l,mid);
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