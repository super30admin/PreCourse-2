// Time o(nlogn) and space o(n)
// divide the array in two halves, and keep dividing until we have array of size 1
// Two sorted parts of array are mergeed using third array of twice their size
class MergeSort
{
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void merge(int arr[], int l, int m, int r)
    {
       //Your code here

       int[] temp = new int[r-l+1];
       int x = 0;
       int i =l;
       int j = m+1;

       while(i<=m || j<=r){
         if(i>m){
           temp[x++] = arr[j++];
         }
         else if(j>r){
           temp[x++] = arr[i++];
         }
         else{
           if(arr[i] < arr[j]){
             temp[x++] = arr[i++];
           }
           else{
             temp[x++] = arr[j++];
           }
         }
       }

       for(int y=l,k=0; y<=r; y++, k++){
         arr[y] = temp[k];

       }
    }

    // Main function that sorts arr[l..r] using
    // merge()
    void sort(int arr[], int l, int r)
    {
	//Write your code here
        //Call mergeSort from here

        if(arr == null || arr.length == 0 ) return ;

        if(l == r)return;

        int mid = l + (r-l)/2;
        sort(arr, l, mid);
        sort(arr, mid+1, r);
        merge(arr, l, mid, r);

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
      //  int arr[] = {12, 11, 13, 5, 6, 7};
          //int arr[] = {};
          //int arr[] = {12,11};

          //int arr[] = {1,2,3,4,5,6};

          int arr[] = {6,5,4,3,2,1};

        System.out.println("Given Array");
        printArray(arr);

        MergeSort ob = new MergeSort();
        ob.sort(arr, 0, arr.length-1);

        System.out.println("\nSorted array");
        printArray(arr);
    }
}
