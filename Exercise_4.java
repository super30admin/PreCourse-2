import java.lang.reflect.Array;
//O(n log n)
class MergeSort
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r)

    {   // Lenght of the arrays
      //  System.out.println(l+";"+m+","+r);
        int l1 = m-l+1;
        int l2 = r-m;
        //Create sub arrays
        int[] leftarray = new int[l1];
        int[] rightarray = new int[l2];
        //Copying the elements on teh array
        for(int i=0; i<l1;++i ){
            leftarray[i] = arr[l+i];
        }
        for(int j=0; j<l2;++j ){
            rightarray[j] = arr[m+1+j];
        }
        // Initial indexes of first and second sub arrays
        int i=0,j=0,k=l;
        while (i<l1 && j<l2){

            if(leftarray[i]<rightarray[j]){
                arr[k] = leftarray[i++];

            }else
            {arr[k] = rightarray[j++];}
                k++;
        }
        while (i<l1){
            arr[k++] = leftarray[i++];
         }
        while (j<l2){
            arr[k++] = rightarray[j++];
        }

        }

  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here
        if(l>=r){return;}
        System.out.println(l + " " + " " + r);
        int mid = (r + l)/2;

            sort(arr, l, mid);
           // System.out.println(l + " "+ mid + " " + r);
            sort(arr, mid+1, r);
            merge(arr, l, mid , r);


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