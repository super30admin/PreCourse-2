class MergeSort {
    void merge(int arr[], int l, int m, int r) {
        int subarraySizeOne = m - l + 1;
        int subarraySizeTwo = r - m;

        int tempOne[] = new int[subarraySizeOne];
        int tempTwo[] = new int[subarraySizeTwo];

        for (int i = 0; i < subarraySizeOne; ++i)
            tempOne[i] = arr[l + i];
        for (int j = 0; j < subarraySizeTwo; ++j)
            tempTwo[j] = arr[m + j + 1];

        int i = 0, j = 0;

        int mIndex = l;

        while (i < subarraySizeOne && j < subarraySizeTwo) {
            if (tempOne[i] <= tempTwo[j]) {
                arr[mIndex] = tempOne[i];
                i++;
            } else {
                arr[mIndex] = tempTwo[j];
                j++;
            }
            mIndex++;
        }

        while(i<subarraySizeOne)
        {
            arr[mIndex] = tempOne[i];
            i++;
            mIndex++;
        }
        while(j<subarraySizeTwo)
        {
            arr[mIndex] =tempTwo[j];
            j++;
            mIndex++;
        }
    }


    void sort(int arr[], int l, int r) 
    { 
	   if(l<r){
           int mid = l+(r-l) /2;

           sort(arr, l, mid);
           sort(arr,mid+1,r);
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