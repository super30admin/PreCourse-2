import java.util.Arrays;

class MergeSort
{
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r)
    {

        System.out.print(" merge l "+l);
        System.out.print(" merge m "+m);
        System.out.print(" merge r "+r);

        int length = r-l+1;
        int n1 = m-l+1;
        int n2 = length - n1;
        int k =0;

        System.out.print(" merge n1 "+n1);
        System.out.print(" merge n2 "+n2);
        int[] temp1 = new int[n1];
        int[] temp2 = new int[n2];

        for (int i=l;i<=m;i++) {
            temp1[k]= arr[i];
            k++;
        }

        System.out.print(" temp1 "+Arrays.toString(temp1));
        k=0;
        for (int i=m+1;i<=r;i++) {
            temp2[k] = arr[i];
            k++;
        }
        System.out.print(" temp2 "+Arrays.toString(temp2));


        k=l;
        int i=0,j=0;
        while (i<n1 && j<n2) {
            if (temp1[i] <= temp2[j]) {
                arr[k] = temp1[i];
                i++;
                k++;
            } else if(temp1[i] > temp2[j]){
                arr[k] = temp2[j];
                j++;
                k++;
            }
        }

        while (i<n1) {
            arr[k] = temp1[i];
            i++;
            k++;
        }

        while (j<n2) {
            arr[k] = temp2[j];
            j++;
            k++;
        }
        System.out.print(" arr "+Arrays.toString(arr));

    }

    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r)
    {

        if (l == r) {
            return;
        }
        int mid = (l+r)/2;
        sort(arr, l, mid);
        sort (arr, mid+1, r);
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
        int arr[] = {12, 11, 13, 5, 6, 7};

        System.out.println("Given Array");
        printArray(arr);

        MergeSort ob = new MergeSort();
        ob.sort(arr, 0, arr.length-1);

        System.out.println("\nSorted array");
        printArray(arr);
    }
}  
