using System;

namespace Precourse2_xercise5
{
    class Precourse2_exercise5
    {
        void swap(int[] arr,int i,int j)
        {
            if (arr[i] != arr[j])
            {
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
            
            /* arr[i] = arr[i] + arr[j];
            arr[j] = arr[i] - arr[j];
            arr[i] = arr[i] - arr[j];*/
        }
        int partition(int[] arr,int l,int h)
        {
            int temp;
            int pivot = arr[h];
            int i = (l - 1);
            for(int j=l;j<=h;j++)
            {
                if(arr[j]<pivot)
                {
                    i++;
                    swap(arr, i, j);
                }
                
            }

            swap(arr, i + 1, h);
            return i+1;
        }
        void quicksort(int[] arr,int l, int h)
        {
            if(l<h)
            {
                int pi = partition(arr, l, h);
                quicksort(arr, l, pi - 1);
                quicksort(arr, pi + 1, h);
            }
        }

        void printarr(int[] arr,int n)
        {
            for(int i=0;i<n; i++)
            {
                Console.WriteLine("element is {0}", arr[i]);
            }
        }

        static void Main(string[] args)
        {
            Precourse2_exercise5 p = new Precourse2_exercise5();
            int[] arr = { 4, 3, 5, 2, 1, 3, 2, 3 };
            p.quicksort(arr, 0, arr.Length - 1);
            p.printarr(arr, arr.Length);
            Console.WriteLine("Hello World!");
        }
    }
}
