import java.util.Arrays;
class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  int[] temp1 = new int[m-l+1];
       for(int i = 0 ; i<m-l+1; i++){
           temp1[i] = arr[l+i];
       }
       int[] temp2 = new int[r-m];
       for(int i = 0 ; i<r-m; i++){
        temp2[i] = arr[m+1+i];
    }

       //Your code here  
       int j = l;
       int k = 0;
       int i = 0;
       while(i < m-l+1 && k < r-m){
            if(temp1[i] <= temp2[k]){
                arr[j] = temp1[i];
                i++;
            } else {
                arr[j] = temp2[k];
                k++;
            }
            j++;
       }
       while(i < m-l+1)
            {arr[j] = temp1[i];
            i++;
            j++;}
        while(k < r-m )
            {arr[j] = temp2[k];
            k++;
            j++;}
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 
        if(l<r){
            int mid = (l+r)/2;
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