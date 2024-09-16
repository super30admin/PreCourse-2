/*
** Time Complexity - best case - O(nlogn) worst case - O(n^2)
** Space Complexity - O(n)
** Did this code successfully run on Leetcode : Yes
** Any problem you faced while coding this : yes(it took time to figure out how to use stack in sorting)
*/

class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
    //swapping without extra variable
        if(i == j) {
            return;
        }
        System.out.println("before swap : arr[i] = "+ arr[i]+" arr[j] = "+ arr[j]);
        arr[i] = arr[i] * arr[j];
        arr[j] = arr[i] / arr[j];
        arr[i] = arr[i] / arr[j];
        System.out.println("after swap : arr[i] = "+ arr[i]+" arr[j]  "+ arr[j]);
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
         //Pivot - here pivot is the last element of array
        int pivot = arr[h];
        //Index of the smaller element
        int i = (l - 1);
        //if the element is smaller than pivot increment the index and swap the element
        for(int j = l; j <= h-1; j++) {
            if(arr[j] < pivot) {
                i++;
                swap(arr, i, j);
            }
        }
        //swap the pivot
        swap(arr, i+1, h);
        return (i+1);

    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    {
        //creating stack
        int stack[] = new int[h-l+1];

        //initialise top of the stack
        int top = -1;
        //push initial values in to the stack
        stack[++top] = l;
        stack[++top] = h;

        //pop the elements till the stack is empty
        while(top>0){
            h = stack[top--];
            l = stack[top--];

            //partition function call to set the pivot in right position
            int p = partition(arr, l, h);
            //push the remaining left side elements of pivot in to the stack
            if(p-1 > l) {
                stack[++top] = l;
                stack[++top] = p-1;
            }
            //push the remaining right side elements of pivot in to the stack
            if(p+1 < h) {
                stack[++top] = p+1;
                stack[++top] = h;
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