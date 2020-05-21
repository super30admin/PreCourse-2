/***
 * 
 * Merge sort Time Complexity : O(nlogn )
 * space complexity : O (N)
 */

public class Exercise_4 
    { 
        // Merges two subarrays of arr[]. 
        // First subarray is arr[l..m] 
        // Second subarray is arr[m+1..r] 
        void merge(int arr[], int l, int m, int r) 
        {  
            int left_size = m - l + 1; 
            int right_size = r - m; 

            int left_arr[] = new int [left_size]; 
            int right_arr[] = new int [right_size]; 

            for (int i=0; i<left_size; ++i) 
                left_arr[i] = arr[l + i]; 
            for (int j=0; j<right_size; ++j) 
                right_arr[j] = arr[m + 1+ j]; 

        
            int i = 0, j = 0; 

            int k = l; 
            while (i < left_size && j < right_size) 
            { 
                if (left_arr[i] <= right_arr[j]) 
                { 
                    arr[k] = left_arr[i]; 
                    i++; 
                } 
                else
                { 
                    arr[k] = right_arr[j]; 
                    j++; 
                } 
                k++; 
            } 

            while (i < left_size) 
            { 
                arr[k] = left_arr[i]; 
                i++; 
                k++; 
            } 

            while (j < right_size) 
            { 
                arr[k] = right_arr[j]; 
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
            if(l < r){
                int mid = (l + r)/2;
                sort(arr, l, mid);
                sort(arr, mid+1, r);
                merge(arr, l, mid, r);
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
    
            Exercise_4 ob= new Exercise_4(); 
            ob.sort(arr, 0, arr.length-1); 
    
            System.out.println("\nSorted array"); 
            printArray(arr); 
        } 
    } 