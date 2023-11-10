public class MergeSort
{

    /*
    TimeComplexity : O(NlogN)
    Space Complexity : O(N)
    */

    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       int leftHalf = m-l+1;
       int rightHalf = r-m;
       int leftArray[] = new int [leftHalf];
       int rightArray[] = new int[rightHalf];

       for(int i=0; i<leftHalf; i++) {
           leftArray[i] = arr[l+i];
       }

        for(int i=0; i<rightHalf; i++) {
            rightArray[i] = arr[m+1+i];
        }
        int i=0,j=0,k=l;
        while(i<leftHalf && j<rightHalf) {
            if(leftArray[i] <= rightArray[j]){
                arr[k] = leftArray[i];
                i++;
            } else {
                arr[j] = rightArray[j];
                j++;
            }
            k++;
        }

        while(i<leftHalf){
            arr[k] = leftArray[i];
            i++;
            k++;
        }
        while(j<rightHalf){
            arr[k] = rightArray[j];
            j++;
            k++;
        }
    }
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r)
    {
        if(l<r) {
            int mid = (l+r)/2;
            sort(arr, l,mid);
            sort(arr, mid+1,r);
            merge(arr, l, mid, r);
        }
	//Write your code here
        //Call mergeSort from here 
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