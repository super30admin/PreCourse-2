
#include<iostream>
#include<cmath>
using namespace std;

int binarySearch(int arr[], int l, int r, int x) {
   int mid;
    if (r >= l) {				//Check if there are elements present in the array or not.

         mid = l + (r - l) / 2;			// Calculating mid point of the array for binary search.


        if (arr[mid]==x) {			// Checking if Element is present at Mid point. 
            return mid;
        }

       else if (arr[mid] > x) {
            return binarySearch(arr, l, mid - 1, x);  // Recursive call to BinarySearch function for left side. Mid will be returned if element is present.
            }

        else
        return binarySearch(arr, mid + 1, r, x);	// Recursive call to Binary Search Function for the right side.

    }

    return -1; // if the element is not present in the array.

    }


int main()
{
    int arr[] = { 2, 3, 4, 10, 40};
    int n = sizeof(arr) / sizeof(arr[0]);
    int x = 10;
    int result = binarySearch(arr, 0, n - 1, x);
    (result == -1) ? cout<<"Element is not present in array"
                   : cout<<"Element is present at index %d "<<result;
    return 0;
}