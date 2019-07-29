class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here

        int first_size = m - l + 1;
        int second_size = r - m;

        int Left_half[] = new int [first_size];
        int Right_half[] = new int [second_size];
        for (int i=0; i<first_size; ++i)
            Left_half[i] = arr[l + i];
        for (int j=0; j<second_size; ++j)
            Right_half[j] = arr[m + 1+ j];


        int i = 0, j = 0;

        int k = l;
        while (i < first_size && j <second_size)
        {
            if (Left_half[i] <= Right_half[j])
            {
                arr[k] = Left_half[i];
                i++;
            }
            else
            {
                arr[k] = Right_half[j];
                j++;
            }
            k++;
        }

        while (i < first_size)
        {
            arr[k] = Left_half[i];
            i++;
            k++;
        }

        while (j < second_size)
        {
            arr[k] = Right_half[j];
            j++;
            k++;
        }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here



        if(l<r){
            int m=(l+r)/2;
            sort(arr,l,m);
            sort(arr,m+1,r);
            merge(arr, l, m, r);
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