class QuickSort
{
    /* This function takes last element as pivot,
       places the pivot element at its correct
       position in sorted array, and places all
       smaller (smaller than pivot) to left of
       pivot and all greater elements to right
       of pivot */
    void swap(int arr[],int i,int j){
        //Your code here : Swaping using a tempVariable
    int swapElement=arr[i];
    arr[i]=arr[j];
    arr[j]=swapElement;
    }

    int partition(int arr[], int low, int high)
    {
   	//Write code here for Partition and Swap
        int i= low;

       int pivotElement=arr[high];
for (int j=low;j<high;j++){
    if(arr[j]<pivotElement){
        this.swap(arr,i,j);
        i=i+1;

    }
}
int index=i+1;
this.swap(arr,i,high);
printArray(arr);
return i;

    }
    /* The main function that implements QuickSort()
      arr[] --> Array to be sorted,
      low  --> Starting index,
      high  --> Ending index */
    void sort(int arr[], int low, int high)
    {
            // Recursively sort elements before
           // partition and after partition
    if ( low<high ) {
        int pivotIndex = partition(arr,low, high);
        this.sort(arr, low, pivotIndex - 1);
        this.sort(arr, pivotIndex + 1, high);

    }
    }

    /* A utility function to print array of size n */
    static void printArray(int arr[])
    {
        int n = arr.length;
        for (int i=0; i<n; ++i)
            System.out.print(arr[i]+" ");
        System.out.println();
    }

    // Driver program
    public static void main(String args[])
    {
        int arr[] = {10, 4, 8, 9, 1, 5,-1};
        int n = arr.length;

        QuickSort ob = new QuickSort();
        ob.sort(arr, 0, n-1);

        System.out.println("sorted array");
        printArray(arr);
    }
}
