import java.util.Stack;

class QuickSort_iterative
{
    /* This function takes last element as pivot,
       places the pivot element at its correct
       position in sorted array, and places all
       smaller (smaller than pivot) to left of
       pivot and all greater elements to right
       of pivot */
    void swap(int arr[],int i,int j){
        int temp=arr[i];
        arr[i]=arr[j];
        arr[j]=temp;
    }

    int partition(int arr[], int low, int high)
    {
        int pivot=arr[high]; // Pivot element (last element - high)
        int k=low;
        for(int i=low;i<high;i++)
        {
            if(arr[i]<pivot) {
                swap(arr, k, i);
                k++;
            }
        }
        int temp=arr[high];
        arr[high]=arr[k];
        arr[k]=temp;
        return k;
    }
    /* The main function that implements QuickSort()
      arr[] --> Array to be sorted,
      low  --> Starting index,
      high  --> Ending index */
    void sort(int arr[], int low, int high)
    {
        // Recursively sort elements before
        // partition and after partition
        Stack<Integer> s1=new Stack<>();
        s1.push(low);
        s1.push(high);
        while(!s1.isEmpty())
        {
            int h1=s1.pop();
            int l1=s1.pop();
            int p=partition(arr,l1,h1);
            if(p-1>l1)
            {
                s1.push(l1);
                s1.push(p-1);
                //sort(arr,low,p-1);
            }
            if(high>(p+1))
            {
                s1.push(p+1);
                s1.push(h1);
            }
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
        System.out.println("Before sorting the array");
        int n = arr.length;
        printArray(arr);
        QuickSort_iterative ob = new QuickSort_iterative();
        ob.sort(arr, 0, n-1);

        System.out.println("sorted array");
        printArray(arr);
    }
}
