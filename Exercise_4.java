class MergeSort {
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]

    // Complexity is O(n log n)
    void merge(int arr[], int l, int m, int r) {
        // Your code here
        int[] aux = new int[arr.length];
        for(int i=0; i<aux.length; i++){
            aux[i] = arr[i];
        }
        // using an auxillary array to compare and swap the values in the main array
        int index_left = l;
        int index_right = m+1;

        int mode = 0;
        for(int i=l; i<=r; i++){
            if(mode == 0){
                if(aux[index_left] <= aux[index_right]){
                    index_left++;
                }
                else{
                    arr[i] = aux[index_right];
                    index_right++;
                }
                if(index_left > m){
                    mode = 1;
                }
                else if(index_right > r){
                    mode = 2;
                }
            }
            else if(mode == 1){
                arr[i] = aux[index_right];
                index_right++;
            }
            else if(mode == 2){
                arr[i] = aux[index_left];
                index_left++;
            }
        }
    }

    // Main function that sorts arr[l..r] using
    // merge()
    // complexity log n
    void sort(int arr[], int l, int r) {
        // Write your code here
        // Call mergeSort from here
        if(l>=r){
            return;
        }
        int m = l+ (r-l)/2;
        this.sort(arr, l, m);
        this.sort(arr, m+1, r);
        this.merge(arr, l, m, r);
    }

    /* A utility function to print array of size n */
    static void printArray(int arr[]) {
        int n = arr.length;
        for (int i = 0; i < n; ++i)
            System.out.print(arr[i] + " ");
        System.out.println();
    }

    // Driver method
    public static void main(String args[]) {
        int arr[] = { 12, 11, 13, 5, 6, 7 };

        System.out.println("Given Array");
        printArray(arr);

        MergeSort ob = new MergeSort();
        ob.sort(arr, 0, arr.length - 1);

        System.out.println("\nSorted array");
        printArray(arr);
    }
}