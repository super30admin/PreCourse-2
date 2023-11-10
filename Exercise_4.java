// Time Complexity : O(nlogn)
// Space Complexity : O(n)
class MergeSort
{
    void merge(int arr[], int l, int m, int r)
    {
        //Your code here
        int temp1 = m-l+1;
        int temp2 = r-m;

        int L[] = new int[temp1];
        int R[] = new int[temp2];

        for(int i=0;i<temp1;i++){
            L[i] = arr[l+i];
        }
        for(int j=0;j<temp2;j++){
            R[j] = arr[m+j+1];
        }

        int i=0, j=0;
        int k=0;
        while(i<temp1 && j<temp2){
            if(L[i] <= R[j]){
                arr[k] = L[i];
                i++;
            }
            else{
                arr[k] = R[j];
                j++;
            }
            k++;
        }
        while(i<temp1){
            arr[k] = L[i];
            i++;
            k++;
        }
        while(j<temp2){
            arr[k] = R[j];
            j++;
            k++;
        }

    }

    void sort(int arr[], int l, int r)
    {
        //Write your code here
        //Call mergeSort from here

        if(l<r){
            int mid = (l+r)/2;
            if(arr.length%2 ==1 ){
                mid = mid+1;
            }
            sort(arr, l, mid);
            sort (arr,mid+1,r);
            merge(arr, l , mid, r);
        }
    }

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