{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "a3cf49da",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Sorted array is:\n",
      "1\n",
      "5\n",
      "7\n",
      "8\n",
      "9\n",
      "10\n"
     ]
    }
   ],
   "source": [
    "def partition(arr, low, high):\n",
    "    i = (low-1)         # index of smaller element\n",
    "    pivot = arr[high]     # pivot\n",
    "    \n",
    "    for j in range(low, high):\n",
    " \n",
    "        # If current element is smaller than or\n",
    "        # equal to pivot\n",
    "        if arr[j] <= pivot:\n",
    "            \n",
    "            # increment index of smaller element\n",
    "            i = i+1\n",
    "            arr[i], arr[j] = arr[j], arr[i]\n",
    " \n",
    "    arr[i+1], arr[high] = arr[high], arr[i+1]\n",
    "    return (i+1)\n",
    "\n",
    " \n",
    "def quickSort(arr, low, high):\n",
    "    if len(arr) == 1:\n",
    "        return arr\n",
    "    if low < high:\n",
    "        pi = partition(arr, low, high)\n",
    "        quickSort(arr, low, pi-1)\n",
    "        quickSort(arr, pi+1, high)\n",
    "        \n",
    "        \n",
    "#Driver code to test above\n",
    "arr = [10, 7, 8, 9, 1, 5]\n",
    "n = len(arr)\n",
    "quickSort(arr, 0, n-1)\n",
    "print(\"Sorted array is:\")\n",
    "for i in range(n):\n",
    "    print(\"%d\" % arr[i])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "334970ce",
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
