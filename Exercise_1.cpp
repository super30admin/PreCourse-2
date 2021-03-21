#include <iostream> 

using namespace std;
  
// A recursive binary search function. It returns 
// location of x in given array arr[l..r] is present, 
// otherwise -1 
int binarySearch(int arr[], int l, int r, int x) 
{  
    if (l > r) {
        return -1;
    }

    int mid = l + (r - l) / 2;
    if (x == arr[mid]) {
        return mid;
    } else if (x < arr[mid]) {
        return binarySearch(arr, l, mid - 1, x);
    } else {
        return binarySearch(arr, mid + 1, r, x);
    }

    return -1;
} 
  
int main(void) 
{ 
    int arr[] = { 2, 3, 4, 10, 40 }; 
    int n = sizeof(arr) / sizeof(arr[0]); 
    int x = 10; 
    int result = binarySearch(arr, 0, n - 1, x); 
    (result == -1) ? cout << "Element is not present in array" << endl
                   : cout << "Element is present at index " << result
                     << endl; 
    return 0; 
} 
