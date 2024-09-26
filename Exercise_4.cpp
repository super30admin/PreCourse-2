#include<stdlib.h> 
#include<stdio.h> 
#include<iostream>
#include<math.h>

using namespace std;
  
void printArray(int A[], int size);
// Merges two subarrays of arr[]. 
// First subarray is arr[l..m] 
// Second subarray is arr[m+1..r] 
void merge(int arr[], int l, int m, int r) 
{ 
    int len1 = m-l+1;
    int len2 = r-m;
    int i;

    int s1[len1+1] = {0};
    int s2[len2+1] = {0};

    //Create 2 sub-arrays before merge process
    s1[len1] = INT32_MAX;
    s2[len2] = INT32_MAX;

    for(i = 0; i < len1; i++)
    {
        s1[i] = arr[l+i];
    }

    for(i = 0; i < len2; i++)
    {
        s2[i] = arr[m+1+i];
    }

    int j = 0; int k = 0;

    //Merge the 2 sub-arrays in sorted order
    for(i = 0; i < (len1+len2); i++)
    {
        if(s1[j] < s2[k])
        {
            arr[l+i] = s1[j];
            j++;
        }
        else
        {
            arr[l+i] = s2[k];
            k++;
        }
    }

    return;
} 
  
/* l is for left index and r is right index of the 
   sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r) 
{ 
    int m = floor((l+r)/2);

    if(l == m)
    {
        //Left half is single element
        ;
    }
    else
    {
        mergeSort(arr, l, m);
    }

    if(r == m+1) 
    {
        //Right half is single element
        ;
    }
    else
    {
        mergeSort(arr, m+1, r);
    }

    merge(arr, l, m, r);
    
    return;
} 
  
/* UTILITY FUNCTIONS */
/* Function to print an array */
void printArray(int A[], int size) 
{ 
    int i; 
    for (i=0; i < size; i++) 
        printf("%d ", A[i]); 
    printf("\n"); 
} 
  
/* Driver program to test above functions */
int main() 
{ 
    int arr[] = {12, 11, 13, 5, 6, 7}; 
    int arr_size = sizeof(arr)/sizeof(arr[0]); 
  
    printf("Given array is \n"); 
    printArray(arr, arr_size); 
  
    mergeSort(arr, 0, arr_size - 1); 
  
    printf("\nSorted array is \n"); 
    printArray(arr, arr_size); 
    return 0; 
}

/**
 * @brief Complexity Analysis
 * Time - O(nlogn)
 * Space - Creation of subarrays can take space
 * 
 */