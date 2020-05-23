import java.util.Stack;

// Time Complexity : O(nlogn)
// Space Complexity : O(n)  as stack used
// Did this code successfully run on Leetcode : Working on eclipse, problem not on leetcode
// Any problem you faced while coding this : Yes, while swapping for the variables with same values, e.g 3 and 3, the new values becomes 0 and I am unable to figure out why
// Your code here along with comments explaining your approach

class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
    //Try swapping without extra variable 
   if(arr[i]!=arr[j]) // added this as swapping for same values eg. 3 and 3 was giving values 0 for both i and j. I am not able to figure out why
   {
    arr[i] = arr[i]+ arr[j]; // added both values to i
    arr[j] = arr[i] - arr[j]; // subtracted j from sum to give value of i and stored in j
    arr[i] = arr[i] - arr[j]; // subtracted i from sum to give value of j and stored in i
   }
    
    
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
        int pivot = h;  // taking pivot as last element 
        int small = l; // taking the small variable as first element

        for(int i=l; i<=h ;i++)  // looping through the array
        {
             if(arr[i]<arr[pivot]) // if the current element is smaller than the element at pivot
             {
                 swap(arr, i, small); // swap the ith and element at small index to place values smaller than the pivot to the left of pivot
                 small++; // increment small
             }

        }
        swap(arr, pivot, small); // after the loop is completed, place the pivot at its right position by swapping pivot element and element at small index
        return small; // return small i.e index at which the pivot is present now
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
       Stack<Integer> stack = new Stack<>(); // created a stack of Integers

       stack.push(l); // pushing the lower and upper index to stack initially
       stack.push(h);

       while(!stack.isEmpty()) // lopping till stack becomes empty
       {
           h=stack.pop(); // pushing upper and lower to stack each time a partition is made
           l=stack.pop();

           int part = partition(arr,l,h); // calculate the partition for new lower and upper bounds

           if(part-1 > l) // if there are values to the left of the partition
           {
               stack.push(l); // adding the lower and upper bounds for the left elements to the stack
               stack.push(part-1);
           }

           if(part+1 < h) // if there are values to the right of the partition
           {
            stack.push(part+1); // adding the lower and upper bounds for the right elements to the stack
            stack.push(h);
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