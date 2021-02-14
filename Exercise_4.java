public class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
       int leftArrayLength = m-l+1;
       int rightArrayLength = r-m;
        int left[] = new int[leftArrayLength];
        int right[] = new int[rightArrayLength];
       for(int i=0;i<leftArrayLength; i++)
       {
           left[i] = arr[l+i];
       }
       for(int j=0;j<rightArrayLength; j++)
       {
            right[j] = arr[m+1+j];
       }
       int i=0, j=0, k=l;
       while(i<leftArrayLength && j<rightArrayLength)
       {
           if(left[i]<=right[j])
           {
               arr[k++] = left[i++];
           }
           else
           {
               arr[k++] = right[j++];
           }
       }

       for(;i<leftArrayLength;i++)
       {
           arr[k++] = left[i];
       }
       for(;j<rightArrayLength;j++)
       {
           arr[k++] = right[j];
       }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() rightArrayLength
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 
        if (l < r) {
            int m =l+ (r-l)/2;
            sort(arr, l, m);
            sort(arr, m + 1, r);
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
        int arr[] = {12, 11, 13, 5, 6, 7, 14, 22, 31, 2, 4, 21, 13}; 
  
        System.out.println("Given Array"); 
        printArray(arr); 
  
        MergeSort ob = new MergeSort(); 
        ob.sort(arr, 0, arr.length-1); 
  
        System.out.println("\nSorted array"); 
        printArray(arr); 
    } 
} 