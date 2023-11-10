// Time Complexity : O(nlogn)
// Space Complexity : O(n)
// Any problem you faced while coding this : understanding space complexity
class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
        if(arr[i]==arr[j]){
            return;
        }
        //Swapping elements without using temp variable and using arithmetic operation
        arr[i]=arr[i]+arr[j];
        arr[j]=arr[i]-arr[j];
        arr[i]=arr[i]-arr[j];
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //selecting the end element as the pivot
        int pivot = arr[h];
        int i = l;//left pointer
        int j = h;//right pointer
        //iterate until the left pointer index is lesser than right pointer index indicating that all the elements are traversed
        while(i<j){
            //move the left pointer to the right until the element is greater than pivot
          while(arr[i]<=pivot && i<j){
              i++;
          }
          //move the right pointer to the left until the element is lesser than pivot
          while(arr[j]>=pivot && i<j){
              j--;
          }
          //swap the left pointer element and the right pointer element, thus maintaining the logic that all elements smaller than the pivot is to its left and all element
          //greater than the pivot is to it's right
          swap(arr, i, j);
        }
        //Finally swap the left pointer element with the pivot element, thus pivot element is now in its correct position
        swap(arr, h, i);
        //return the new pivot index
        return i;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        //Create a stack array with size equal to little greater than half the original array
        int[] stack = new int[h-l+1];

        //Set the initial top of the stack
        int top=-1;
        //Push the low and high index value range into the stack
        stack[++top]=l;
        stack[++top]=h;

        //While the stack is not empty
        while(top>=0){
            //Pop the low and high index value, we will use these values to get the partition element for the array between these index range
            h=stack[top--];
            l=stack[top--];
            //Calling the partition function to get the partition element
            int p=partition(arr, l, h);

            //Pushing in lower and upper(mid-1) index for the next subarray
            if(p-1>l){
                stack[++top]=l;
                stack[++top]=p-1;
            }

            //Pushing in lower(mid+1) and upper(mid-1) index for the next subarray
            if(p+1<h){
                stack[++top]=p+1;
                stack[++top]=h;
            }
        }
    } 
  
    // A utility function to print contents of arr 
    void printArr(int arr[], int n) 
    { 
        int i; 
        for (i = 0; i < n; ++i) 
            System.out.print(arr[i] + " "); 
    } 
  
    // Driver code to test above 
    public static void main(String args[]) 
    { 
        IterativeQuickSort ob = new IterativeQuickSort(); 
        int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 }; 
        ob.QuickSort(arr, 0, arr.length - 1); 
        ob.printArr(arr, arr.length); 
    } 
} 