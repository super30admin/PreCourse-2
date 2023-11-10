// Time Complexity :    O(n*n)
// Space Complexity :   O(n)
//  tried leetcode 912 problem using this, got time limit exceed error.
// No I don't face any problem.

class QuickSort
{
    /* This function takes last element as pivot,
       places the pivot element at its correct
       position in sorted array, and places all
       smaller (smaller than pivot) to left of
       pivot and all greater elements to right
       of pivot */
    void swap(int arr[],int i,int j){
        //Your code here
        int temp = arr[i]; // swapping logic
        arr[i]=arr[j];
        arr[j]=temp;
    }

    int partition(int arr[], int low, int high)
    {
        //Write code here for Partition and Swap
        //   int arr[] = {5,1,1,2,0,0};

        int pivot = arr[high]; // assign last element as pivot
        int i = low;
        int j = high;

        while (i<j) { // continue loop while i and j pointer haven't crossed
            while (arr[i] <= pivot & i < high) { //when element is smaller than pivot, increment i pointer
                i++;
            }
            while (arr[j] >= pivot & j > low) { //when element is larger than pivot, increment i pointer
                j--;
            }
            if (i < j) { //check if i and j pointer crossed each other
                swap(arr, i, j);
            }
        }
        swap(arr, i, high ); // swap i and pivot

        return i; //return pivot position
    }
    /* The main function that implements QuickSort()
      arr[] --> Array to be sorted,
      low  --> Starting index,
      high  --> Ending index */
    void sort(int arr[], int low, int high)
    {
            // Recursively sort elements before
            // partition and after partition
        if(low<high){ //check if low is less than high, termination condition for recursion

            int partitionIndex=partition(arr, low, high);
            sort(arr, low, partitionIndex-1); //divide the list into 2 halves
            sort(arr, partitionIndex+1,high);
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
        int arr[] = {5,1,1,2,0,0};


        int n = arr.length;

        QuickSort ob = new QuickSort();
        ob.sort(arr, 0, n-1);

        System.out.println("sorted array");
        printArray(arr);
    }
}
