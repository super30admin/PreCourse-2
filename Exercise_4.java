// Time Complexity : O(NlogN) 
// Space Complexity : O(N) 
// Did this code successfully run on Leetcode : Yes  https://leetcode.com/problems/sort-an-array/description/
// Any problem you faced while coding this:  No
// Your code here along with comments explaining your approach: I have used the sort function twice. First, to sort the elements on the left side and then next time to sort the elements on the right side. Sort is a recursive function that keeps dividing the array until it gets only the last two elements. It then compares them and adds the smaller element in a new List called temp. This process is taken place in the function Merge.  In the end all the elements in the list are added back in the array

import java.util.ArrayList;
import java.util.List;

class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
       int left=l, right=m+1;
       List<Integer> temp=new ArrayList<>();
       while(left<=m && right<=r)
       {
        if(arr[left]<arr[right])
        {
            temp.add(arr[left]);
            left++;
        }
        else
        {
            temp.add(arr[right]);
            right++;
        }
       }

       while (left<=m)
       {
        temp.add(arr[left]);
        left++;
       }

       while (right<=r)
       {
        temp.add(arr[right]);
        right++;
        }

        for(int i=l;i<=r;i++)
        {
            arr[i]=(int) temp.get(i-l);
        }

    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 

        if(l>=r) return ;
        int mid=(l+r)/2;
        //Left side
        sort(arr,l,mid);
        //Right side
        sort(arr,mid+1,r);
        merge(arr,l,mid,r);
    } 
  
    /* A utility function to print array of size n */
    static void printArray(int arr[]) 
    { 
        int n = arr.length; 
        for (int i=0; i<n; ++i) 
            System.out.print(arr[i] + " "); 
        System.out.println(); 
    } 
  
    // Driver method 
    public static void main(String args[]) 
    { 
        int arr[] = {12, 11, 13, 5, 6, 7}; 
  
        System.out.println("Given Array"); 
        printArray(arr); 
  
        MergeSort ob = new MergeSort(); 
        ob.sort(arr, 0, arr.length-1); 
  
        System.out.println("\nSorted array"); 
        printArray(arr); 
    } 
} 