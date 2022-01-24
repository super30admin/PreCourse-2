// Operation:            Mergesort
// Time Complexity:       n*log(n)
// Space Complexity:         n
// Yes, this code ran successfully
// No, I didn't face any problem in this problem statement

class MergeSort {
    // Merges two subarrays of arr[].
    // First subarray is arr[l..m]
    // Second subarray is arr[m+1..r]
    void merge(int arr[], int l, int m, int r) {
        //Your code here
        int i = l ;
        int j = m+1 ;
        int k = l ;
        int index = 0;
        int temp[] = new int[r-l+1];

        while(i<=m && j<=r) {
            if (arr[i] < arr[j]) {
                temp[index] = arr[i];           // taking values to its sorted position in temp array
                i++;
                index++;
            } else {
                temp[index] = arr[j];           // taking values to its sorted position in temp array
                j++;
                index++;
            }
        }

        //adding remaining elements
        while(j<=r)                             // taking values left from 2nd partition of array
        {
            temp[index] = arr[j] ;
            j++ ;
            index++ ;
        }

        while(i<=m)                             // taking values left from 1st partition of array
        {
            temp[index] = arr[i] ;
            i++ ;
            index++ ;
        }

        int id=0;
        while(id<index)                         // taking sorted array back to arr array
        {
            arr[k] = temp[id] ;
            k++ ;
            id++;
        }
    }

    // Main function that sorts arr[l..r] using
    // merge()
    void sort(int arr[], int l, int r) {
        //Write your code here
        //Call mergeSort from here
        if(l<r)
        {
            int mid = (l + r) / 2;
            sort(arr, l, mid);
            sort(arr, mid + 1, r);
            merge(arr, l, mid, r);
        }
    }

    /* A utility function to print array of size n */
    static void printArray(int arr[]) {
        int n = arr.length;
        for (int i = 0; i < n; ++i)
            System.out.print(arr[i] + " ");
        System.out.println();
    }
}

public class Exercise_4
{
    // Driver method
    public static void main(String args[])
    {
        int arr[] = {12, 11, 13, 5, 6, 7};

        System.out.println("Given Array");
        MergeSort.printArray(arr);

        MergeSort ob = new MergeSort();
        ob.sort(arr, 0, arr.length-1);

        System.out.println("\nSorted array");
        MergeSort.printArray(arr);
    }
}