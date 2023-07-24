class MergeSort 
{
    //Time Complexity :- O(nlogn)
    //Space Complexity :- O(n)
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here
               int n1 = m - l + 1;
        int n2 = r - m;
        int p[] = new int[n1];
        int q[] = new int[n2];

        for (int i = 0; i < n1; ++i)
            p[i] = arr[l + i];
        for (int j = 0; j < n2; ++j)
            q[j] = arr[m + 1 + j];

        int s = 0, w = 0;
        int k = l;
        while (s < n1 && w < n2) {
            if (p[s] <=q[w]) {
                arr[k] = p[s];
                s++;
            }
            else {
                arr[k] = q[w];
                w++;
            }
            k++;
        }
        while (s < n1) {
            arr[k] = p[s];
            s++;
            k++;
        }
        while (w < n2) {
            arr[k] = q[w];
            w++;
            k++;
        }

    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
    //Call mergeSort from here 
        if (l < r) {
            int m = l + (r - l) / 2;
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
        int arr[] = {12, 11, 13, 5, 6, 7}; 
  
        System.out.println("Given Array"); 
        printArray(arr); 
  
        MergeSort ob = new MergeSort(); 
        ob.sort(arr, 0, arr.length-1); 
  
        System.out.println("\nSorted array"); 
        printArray(arr); 
    } 
} 