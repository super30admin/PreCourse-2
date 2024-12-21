// Time Complexity : Need to refresh my knowledge on this.
// Space Complexity : Need to refresh my knowledge on this.
// Did this code successfully run on Leetcode : YES(Over local ide).
// Any problem you faced while coding this : None, other than t.c and s.c.
class MergeSort
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here
        int leftArrayLenght = m-l+1; //because {0,1,2,3,4} -> m = 3 and it makes the left array of size 3 and right of size 2 total will be 5
        int rightArrayLength = r-m;
        int[] leftArray = new int[leftArrayLenght];
        int[] rightArray = new int[rightArrayLength];
        //now fill the left and right array witht the values
        for(int i = 0; i < leftArrayLenght; i++){
            leftArray[i] = arr[l+i]; // why l+i because let's say L= 3 for the 2nd array then 3+1(#i=1) it means 4th element of the provided array to be added.
        }
        for(int j = 0; j < rightArrayLength; j++){
            rightArray[j] = arr[m+j+1];
        }
        // now we'll create 3 iterator which help us to iterate over the original array and new array created.
        int i=0,j=0,k=l; //k = l because in the 2nd cracked array the l = mid+1
        while(i<leftArrayLenght && j<rightArrayLength){//we'll go until i and j becomes the length of 2 sorted array
            if(leftArray[i]<rightArray[j]){// check wit the 2 array which is smaller and assign the new array of k with the element which is smaller
                arr[k] = leftArray[i];
                i++;
            }
            else{
                arr[k] = rightArray[j];
                j++;
            }
            k++;
        }
        while(i<leftArrayLenght){//this because we don't want to have any left out items.
            arr[k] = leftArray[i];
            i++;
            k++;
        }
        while(j<rightArrayLength){
            arr[k] = rightArray[j];
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
        //do the function only if start < end
        if(l<r){
            int mid = l+(r-l)/2;
            //now call sort again until the array is divided in 1 1 1... element each.
            sort(arr,l,mid);
            sort(arr,mid+1,r);
            //now merge the element to one array.
            merge(arr,l,mid,r);
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