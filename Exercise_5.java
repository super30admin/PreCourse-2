// Time Complexity : Not Sure
// Space Complexity : Not sure
// Did this code successfully run on Leetcode :
// Any problem you faced while coding this : Yes, I was not able to implement it on my own and understand it.
import java.util.*;
class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	if (i != j) {                        //it will not swap if i & j are equal
            arr[i] = arr[i] + arr[j];    //swapping without using 3rd variable
            arr[j] = arr[i] - arr[j];
            arr[i] = arr[i] - arr[j];
        }
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h)         //partitioning and returning the position of the pivot
    { 
        int pivot = arr[h];
        int x=l-1;                                    //x is the pointer which we are maintaining and it will return the correct position of the pivot

        for(int i=l;i<h;i++){                      //the loop will be low to high and then at the end we will swap the pivot
            if(arr[i]<pivot){
                x++;
            swap(arr,x,i);
            }
        }
        x++;
        swap(arr,x,h);
        return x;
    } 
  
     
    void QuickSort(int arr[], int l, int h)                  //I didn't completely understood this part but I understood it recursively. Here we are pushing the range of indexes of left and right of the pivot
    { 
       Stack<Integer> stack = new Stack<>();
        stack.push(l);
        stack.push(h);

        while (!stack.isEmpty()) {
            int high = stack.pop();
            int low = stack.pop();

            if (low < high) {
                int pi = partition(arr, low, high); 

                //left side
                if (pi - 1 > low) {
                    stack.push(low);
                    stack.push(pi - 1);
                }

               //right side
                if (pi + 1 < high) {
                    stack.push(pi + 1);
                    stack.push(high);
                }
            }
        }

        
    } 
  
    
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