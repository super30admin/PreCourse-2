//Problem 5: Iterative Quick Sort

//   Time Complexity : I think it has same time complexity as recursive approach with worst time complexity as O(n^2) if the elements are already in sorted order
//                      and it would be O(n log n) n times for partinioning and log n times for recursion.
//   Space Complexity : The space complexity would be O (n + log n) we use n space for the stack.
//   Any problem you faced while coding this : Was not able to achieve swapping without extra variable as difference between two values was throwing zero

import java.util.Stack;

class IterativeQuickSort {
    void swap(int arr[], int i, int j)
    {
        //Try swapping without extra variable

        //TODO: Not able to achieve without extra variable as we encounter zero
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    /* This function is same in both iterative and
       recursive*/
    int partition(int arr[], int l, int h)
    {
        //Compare elements and swap.
        int pivot = arr[h];
        if(l <= h){
            for(int i =l;i<=h;i++){
                if(arr[i] < pivot) {
                    swap(arr, i, l);
                    l++;
                }
            }
            swap(arr,l,h);
        }
        return l;
    }

    // Sorts arr[l..h] using iterative QuickSort
    void QuickSort(int arr[], int l, int h)
    {
        //Try using Stack Data Structure to remove recursion.
        Stack<Integer> s = new Stack<>();
        s.push(l);
        s.push(h);

        while(!s.isEmpty()){
            h = s.pop();
            l = s.pop();

            int pivot = partition(arr,l,h);
            if(pivot-1 > l){
                s.push(l);
                s.push(pivot-1);
            }
            if(pivot+1 < h){
                s.push(pivot+1);
                s.push(h);
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