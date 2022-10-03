

// Time Complexity : O(nlogn)
// Space Complexity : O(1)


package S30_Codes.PreCourse_2;

class QuickSort
{ 
    /* This function takes last element as pivot, 
       places the pivot element at its correct 
       position in sorted array, and places all
       smaller (smaller than pivot) to left of
       pivot and all greater elements to right 
       of pivot */
    void swap(int arr[],int i,int j){
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
    
    int partition(int arr[], int low, int high) 
    {
        int pivot = arr[high];
        int pivotIdx = low-1;

        for(int i=low; i<=high; i++){
            if(arr[i] <= pivot)
                pivotIdx++;
        }

        swap(arr, pivotIdx, high);

        int part1Idx = low;
        int part2Idx = pivotIdx + 1;
        int tempIdx = low;

        while(tempIdx <= high){

            // Value less than or equal to pivot
            if(arr[tempIdx] <= pivot) {
                //tempIdx is greater than pivotIdx
                if(tempIdx > pivotIdx) {
                    // finds place in part1 where element is greater, so we can replace smaller element with it.
                    while (arr[part1Idx] <= pivot)
                        part1Idx++;

                    swap(arr, tempIdx, part1Idx++);
                }
                tempIdx++;
            }

            // Value Grater than pivot
            else {
                //tempIdx is less than pivotIdx
                if(tempIdx < pivotIdx) {
                    // finds place in part2 where element is smaller, so we can replace bigger element with it.
                    while (arr[part2Idx] > pivot) {
                        part2Idx++;
                    }
                    swap(arr, tempIdx, part2Idx++);
                }
                tempIdx++;
            }
        }

        return pivotIdx;
    }
    void sort(int arr[], int low, int high) 
    {
        if(low < high){
            int pivotIdx = partition(arr, low, high);
            sort(arr, low, pivotIdx-1);
            sort(arr, pivotIdx+1, high);
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
        int arr[] = {10, 7, 8, 9, 1, 5};
        int n = arr.length; 
  
        QuickSort ob = new QuickSort(); 
        ob.sort(arr, 0, n-1);
  
        System.out.println("sorted array"); 
        printArray(arr); 
    } 
} 
