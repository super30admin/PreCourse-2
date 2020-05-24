class Exercise_4
{
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r)
    {
        int p1 = m -l+1;
        int p2= r -m;

        int L[]= new int[p1];
        int R[]=new int[p2];


        for(int i=0;i<p1;i++){
            L[i]=arr[l+i];
        }
        for(int j=0;j<p2;j++){
            R[j]=arr[m+1+j];
        }

        int i=0,j=0;
        int k= l;
        while(i<p1&& j<p2){
            if(L[i]<=R[j]){
                arr[k]=L[i];
                i++;
            }
            else{
                arr[k]=R[j];
                j++;
            }
            k++;
        }


        while(i<p1){
            arr[k]=L[i];
            i++;
            k++;
        }

        while(j<p2){
            arr[k]= R[j];
            j++;
            k++;
        }

    }

    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r)
    {
      if(l<r){
          int m = (l+r)/2;

          sort(arr,l,m);
          sort(arr,m+1,r);


          merge(arr,l,m,r);
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

        Exercise_4 ob = new Exercise_4();
        ob.sort(arr, 0, arr.length-1);

        System.out.println("\nSorted array");
        printArray(arr);
    }
} 

//Time Complexity O(n log n)