class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here 
       int left = m - l + 1; // left subarray size inclusive of m
       int right = r - m; // right subarray exclusive of m

       //create temporary arrays to store the left and right sub arrays of arr[]
       int[] leftArr = new int[left];
       int[] rightArr = new int[right];

        // fill these subarrays
        for(int i=0;i<left;i++){
             leftArr[i] = arr[i+l] ;
        }

        for(int i=0;i<right;i++){
            rightArr[i] = arr[i+m+1];
        }


        // indexes of left and right subarrays
        int li =0;
        int ri = 0;
        int resi = l; // index of result array
        while(li<left && ri < right){
            // since left and right subarrays are sorted already,
            if(leftArr[li] <= rightArr[ri]){
                arr[resi] = leftArr[li];
                li++;
            }else{
                arr[resi] = rightArr[ri];
                ri++;
            }
            resi++;
            
        }

        //residual aray elements from leftArr[]
        while(li<left ){
            // System.out.println(resi);
            arr[resi] = leftArr[li];
            
            li++;
            resi++;
        }
        // residual array elements from rightArr[]
        while(ri < right){
            // System.out.println(resi);
            arr[resi] = rightArr[ri];
            ri++;
            resi++;
            
        }
       
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
    //Write your code here
        
        //Call mergeSort from here 
        if(l < r){
            int m = (l + r)/2;
            sort(arr,l,m);
            // System.out.println("r"+r);
            sort(arr,m+1,r);
            merge(arr,l,m,r);
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


