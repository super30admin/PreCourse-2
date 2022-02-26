{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "57e756f0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Given array is\n",
      "12 11 13 5 6 7 \n",
      "Sorted array is: \n",
      "5 6 7 11 12 13 \n"
     ]
    }
   ],
   "source": [
    "def mergeSort(arr):\n",
    "    if len(arr) > 1:\n",
    "        # Finding the mid of the array\n",
    "        mid = len(arr)//2\n",
    "  \n",
    "        # Dividing the array elements\n",
    "        L = arr[:mid]\n",
    "  \n",
    "        # into 2 halves\n",
    "        R = arr[mid:]\n",
    "  \n",
    "        # Sorting the first half\n",
    "        mergeSort(L)\n",
    "  \n",
    "        # Sorting the second half\n",
    "        mergeSort(R)\n",
    "        \n",
    "        \n",
    "        i = j = k = 0 \n",
    "        # Copy data to temp arrays L[] and R[]\n",
    "        \n",
    "        while i < len(L) and j < len(R):\n",
    "            if L[i] < R[j]:\n",
    "                arr[k] = L[i]\n",
    "                i += 1\n",
    "            else:\n",
    "                arr[k] = R[j]\n",
    "                j += 1\n",
    "            k += 1\n",
    "            \n",
    "        # Checking if any element was left\n",
    "        while i < len(L):\n",
    "            arr[k] = L[i]\n",
    "            i += 1\n",
    "            k += 1\n",
    "  \n",
    "        while j < len(R):\n",
    "            arr[k] = R[j]\n",
    "            j += 1\n",
    "            k += 1\n",
    "            \n",
    "            \n",
    "# Code to print the list\n",
    "  \n",
    "def printList(arr):\n",
    "    for i in range(len(arr)):\n",
    "        print(arr[i], end=\" \")\n",
    "    print()\n",
    "    \n",
    "# Driver Code\n",
    "if __name__ == '__main__':\n",
    "    arr = [12, 11, 13, 5, 6, 7]\n",
    "    print(\"Given array is\", end=\"\\n\")\n",
    "    printList(arr)\n",
    "    mergeSort(arr)\n",
    "    print(\"Sorted array is: \", end=\"\\n\")\n",
    "    printList(arr)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9fea2b0e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
