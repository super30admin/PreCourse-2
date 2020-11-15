using System;

namespace Precourse2_Exercise1
{
    class Precourse2_exercise1
    {
        int BinarySearch(int[] arr,int l,int r, int x)
        {
            if (l > r)
            {
                return -1;
            }
            else
            {
                int mid = (l + r) / 2;
                if (x == arr[mid])
                {
                    return mid;
                }
                else if (x < arr[mid])
                {
                    return BinarySearch(arr, l, mid - 1, x);
                }
                else if (x > arr[mid])
                {
                    return BinarySearch(arr, mid+1,r , x);
                }
                else
                {
                    return -1;
                }
            }
            
        }
        static void Main(string[] args)
        {
            Precourse2_exercise1 p = new Precourse2_exercise1();
            int[] arr = new int[]{ 2,3,4,10,40};
            int n = arr.Length;
            int x = 10;
            int result = p.BinarySearch(arr, 0, n - 1, x);
            if (result == -1)
            {
                Console.WriteLine("element not present");
            }
            else {
                Console.WriteLine("element present at {0}",result);
            }
        }
    }
}
