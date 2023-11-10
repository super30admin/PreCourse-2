class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 

    //TC : O(nlogn)
    //SC : O(n)
    void merge(int arr[], int l, int m, int r, int[] aux) 
    {  
       //Your code here  
       int i =1, j = m+1, k =0;

       while(i <= m && j <= r){
        if(arr[i] < arr[j]){
            aux[k++] = arr[i++];
        }
         else aux[k++] = arr[j++];
       }

       while(i <= m ) {
           aux[k++] = arr[i++];
       }
       while(j <=r){
           aux[k++] = arr[j++];
       }

        for(i = 0; i < k; ++i){
            arr[i] = aux[i];
        }

       }

    // Main function that sorts arr[l..r] using 
    // merge() 

    void sort(int[] arr){
        int[] aux = new int[arr.length];
        auxMergesort(arr, 0, arr.length-1, aux);
        }

    void auxMergesort(int arr[], int l, int r, int[] aux) 
    { 
	//Write your code here
        //Call mergeSort from here 

        
        if( l >= r) return;

        int m = (l + r) / 2;
        auxMergesort(arr, l , m, aux);
        auxMergesort(arr, m+1, r, aux);
        merge(arr, l, m , r, aux);

    } 

    
    
  
    /* A utility function to print array of size n */
     static void printArray(int arr[]) 
     { 
         int n = arr.length; 
         for (int i=0; i<n; ++i) 
             System.out.print(arr[i] + " "); 
         System.out.println(); 
     } 
    
}

public class Exercise_4{
    // Driver method
    public static void main(String args[]) 
    { 
        int arr[] = {12, 11, 13, 5, 6, 7}; 

        System.out.println("Given Array"); 
        MergeSort.printArray(arr); 
  
        MergeSort ob = new MergeSort(); 
        ob.sort(arr); 
  
        System.out.println("\nSorted array"); 
        MergeSort.printArray(arr);  
    }
    

   

    
}
  
     
