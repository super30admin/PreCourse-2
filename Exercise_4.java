// Time Complexity : O(nlog(n))
// Space Complexity : O(n)

//MergeSort
class Exercise_4
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r]

    void merge(int arr[], int l, int m, int r)
    {
        int num1 = m - l + 1;
        int num2 = r - m;

        int left[]  = new int[num1];
        int right[] = new  int[num2];

        for( int i = 0; i < num1; i++){
            left[i] = arr[l+i];
        }
        for ( int j = 0; j < num2; j++){
            right[j] = arr[ m + 1 + j];
        }

        int x = 0, y = 0;
        int p = l;
        while ( x < num1 && y< num2){
            if(left[x] <= right[y]){
                arr[p] = left[x];
                x++;
            }else{
                arr[p] = right[y];
                y++;
            }
            p++;
        }
        while( x < num1){
            arr[p] = left[x];
            x++;
            p++;
        }
        while (y < num2){
            arr[p] = right[y];
            y++;
            p++;
        }
    }

    // Main function that sorts arr[l..r] using
    // merge()
    void sort(int arr[], int l, int r) {
        if( l < r){
            int mid = l + (r - l) / 2;
            sort( arr, l, mid);
            sort( arr, (mid+1) , r);
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

        Exercise_4 ob = new Exercise_4();
        ob.sort(arr, 0, arr.length-1);

        System.out.println("\nSorted array");
        printArray(arr);
    }
}
