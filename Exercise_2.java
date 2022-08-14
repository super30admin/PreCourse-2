// Time Complexity :O(nlogn)
// Space Complexity : O(n)
class QuickSort
{
    void swap(int arr[],int i,int j){
        //Your code here
        int temp;
        temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    int partition(int arr[], int low, int high)
    {
        int pivot = arr[low];
        int i= low, j = high;
        while(i<j){
            while(arr[i]<=pivot){
                i++;
            }

            while(arr[j]>pivot){
                j--;
            }

            if(i<j)
                swap(arr, i, j);
        }
        swap(arr, arr[low], j);
        return j;


    }

    void sort(int arr[], int low, int high)
    {
        if(low<high){
            int j = partition(arr,low, high);
            sort(arr, low, j);
            sort(arr, j+1, high);
        }
    }

    static void printArray(int arr[])
    {
        int n = arr.length;
        for (int i=0; i<n; ++i)
            System.out.print(arr[i]+" ");
        System.out.println();
    }

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