class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
       int num1 = m-1+1
       int num2 = r-m;

       // creating the subarrays
       int L[] = new int[num1];
       int R[] = new int[num2];

       //copying the data
       for (int i=0; i<num1; i++){
        L[i] = arr[l+i];
       }
       for(int j=0; j<num2; j++){
        R[j] = arr[j+m+1];
       }

       // initial index 
       int k = l;

       //comparing the values of both the sub arrays
       while(i<num1 && j <num2){
        if(L[i]<R[j]){
            arr[k] = L[i];
            i++;
        }
        else{
            arr[k] = R[j];
            j++;
        }
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
            // mid point
            int m = l + (r - l) / 2;

            // sorting
            sort(arr, l, m);
            sort(arr, m + 1, r);

            //merging 
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