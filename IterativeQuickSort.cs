using System;
namespace Algorithms
{
    public class IterativeQuickSort
    {
        public void swap(int[] arr, int i, int j)
        {
            //Try swapping without extra variable
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }

        /* This function is same in both iterative and 
           recursive*/
        public int partition(int[] arr, int l, int h)
        {
            //Compare elements and swap.
            int pivot = arr[h];

            int i = (l - 1);
            for (int j = l; j <= h - 1; j++)
            {
                // If current element is smaller
                // than or equal to pivot
                if (arr[j] <= pivot)
                {
                    i++;
                    swap(arr, i, j);

                }
            }

            // swap arr[i+1] and arr[h]
            // (or pivot)
            swap(arr, i + 1, h);

            return i + 1;
        }


        // Sorts arr[l..h] using iterative QuickSort 
        public void QuickSort(int[] arr, int l, int h)
        {
            //Try using Stack Data Structure to remove recursion.
            // Create an auxiliary stack
            int[] stack = new int[h - l + 1];

            // initialize top of stack
            int top = -1;

            // push initial values of l and h to
            // stack
            stack[++top] = l;
            stack[++top] = h;

            // Keep popping from stack while
            // is not empty
            while (top >= 0)
            {
                // Pop h and l
                h = stack[top--];
                l = stack[top--];

                // Set pivot element at its
                // correct position in
                // sorted array
                int p = partition(arr, l, h);
                // If there are elements on
                // left side of pivot, then
                // push left side to stack
                if (p - 1 > l)
                {
                    stack[++top] = l;
                    stack[++top] = p - 1;
                }

                // If there are elements on
                // right side of pivot, then
                // push right side to stack
                if (p + 1 < h)
                {
                    stack[++top] = p + 1;
                    stack[++top] = h;
                }
            }
        }


        // A utility function to print contents of arr 
        public void printArr(int[] arr, int n)
        {
            int i;
            for (i = 0; i < n; ++i)
                Console.WriteLine(arr[i] + " ");
        }


    }
}


