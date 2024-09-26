using System;

namespace Precourse2_exercise2
{
    class Precourse2_exercise2
    {
        void Swap(int[] arr, int i, int j)
        {
            int temp = arr[j];
            arr[j] = arr[i];
            arr[i] = temp;
        }
        int partition(int[] arr,int low, int high)
        {

            int pivot = arr[low];
            while(true)
            {
                while(arr[low] < pivot)
                {
                    low++;
                }
                while(arr[high] > pivot)
                {
                    high--;
                }

                if(low<high)
                {
                    Swap(arr, low, high);
                }
                else
                {
                    return high;
                }
            }
            
        }
        void sort(int[] arr, int low, int high)
        {
            if(low<high)
            {
                int pivot = partition(arr, low, high);
                if(pivot>1)
                {
                    sort(arr, low, pivot - 1);
                }
                else
                {
                    sort(arr, pivot + 1, high);
                }
            }
        }
        static void Print(int[] arr)
        {
            int length = arr.Length;
            for(int i=0;i<arr.Length;i++)
            {
                Console.WriteLine("printing array {0}", arr[i]);
            }
        }
        static void Main(string[] args)
        {
            int[] arr = new int[] { 10,7,8,9,1,5};
            int n = arr.Length;
            Precourse2_exercise2 p = new Precourse2_exercise2();
            p.sort(arr, 0, n - 1);
            Console.WriteLine("sorted array");
            Print(arr);
        }
    }
}
