using System;
namespace Algorithms
{
    /// Time Complexity : O(Log n)
    // Space Complexity :O(1)
    // Did this code successfully run on Leetcode : Tested on VS
    // Any problem you faced while coding this : No
    public class BinarySearch
    {
        
        // Returns index of x if it is present in arr[l.. r], else return -1 
        public int BinarySearchAlg(int[] arr, int l, int r, int x)
        {
            //Write your code here
            if(r >= l)
            {
                //find mid index
                int mid = l + (r - l) / 2;

                //return mid if its equal seaching term
                if (arr[mid] == x)
                {
                    return mid;
                }
                if(x < arr[mid])
                {
                    //search left
                    return BinarySearchAlg(arr, l, mid-l, x);
                }
                else
                {
                    //search right
                    return BinarySearchAlg(arr, mid + l, r, x);
                }
            }
            return -1;
        }
    }
}
