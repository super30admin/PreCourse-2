// Time Complexity : O(nlogn)
// Space Complexity : O(nlogn)
class MergeSort
{
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void merge(int arr[], int l, int m, int r)
    {
       //Your code here
       int num1 = m - l + 1;
       int num2 = r - m;

       int ls[] = new int[num1];
       int rs[] = new int[num2];

       for(int i = 0; i < num1; ++i) {
           ls[i] = arr[l + i];
       }
       for(int j = 0; j < num2; ++j) {
           rs[j] = arr[m + 1 + j];
       }
       int i = 0, j = 0, k = l;
       while(i < num1 && j < num2)
       {
           if(ls[i] <= rs[j]) {
               arr[k] = ls[i];
               i++;
           }
           else{
               arr[k] = rs[j];
               j++;
           }
           k++;
       }
        while(i < num1)
        {
            arr[k] = ls[i];
            i++;
            k++;
        }
        while(j < num2)
        {
            arr[k] = rs[j];
            j++;
            k++;
        }
    }

    // Main function that sorts arr[l..r] using
    // merge()
    void sort(int arr[], int l, int r)
    {
	//Write your code here


        if(l < r)
        {

                int m = (l+(r-1))/2;
                sort(arr,l,m);
                sort(arr,m+1,r);
                merge(arr,l,m,r);
            }
        else{
            return;
        }
        }
        //Call mergeSort from here



    /* A utility function to print array of size n */
    static void printArray(int arr[])
    {
        int n = arr.length;
        for(int i=0; i<n; ++i)
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