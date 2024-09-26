class Exercise_4 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    public static void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here 
       int i=l;
       int j=m+1;
       int k = 0;
       int[] copy = new int[r-l+1];
       while(i<=m && j<=r){
          if(arr[i]<arr[j]){
            copy[k] = arr[i];
            i+=1;
          }else{
              copy[k] = arr[j];
              j+=1;
          }
          k+=1;
       }
       while(i<=m){
          copy[k] = arr[i];
          i+=1;
          k+=1;
       }
       while(j<=r){
          copy[k] = arr[j];
          j+=1;
          k+=1;
       }
       while(k>0){
            arr[r--] = copy[--k];
        }
    } 
    
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    public static void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 
        if(r-l<=0){
            return;
        }
        int m = l+(r-l)/2;
        sort(arr,l,m);
        sort(arr,m+1,r);
        merge(arr,l,m,r);
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
  
        //MergeSort ob = new MergeSort(); 
        sort(arr, 0, arr.length-1); 
  
        System.out.println("\nSorted array"); 
        printArray(arr); 
    } 
} 