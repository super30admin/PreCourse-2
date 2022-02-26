{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "e67aa441",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Sorted array is:\n",
      "1\n",
      "2\n",
      "2\n",
      "3\n",
      "3\n",
      "3\n",
      "4\n",
      "5\n"
     ]
    }
   ],
   "source": [
    "def partition(arr,l,h):\n",
    "    i = ( l - 1 )\n",
    "    x = arr[h]\n",
    "  \n",
    "    for j in range(l , h):\n",
    "        if arr[j] <= x:\n",
    "            # increment index of smaller element\n",
    "            i = i+1\n",
    "            arr[i],arr[j] = arr[j],arr[i]\n",
    "  \n",
    "    arr[i+1],arr[h] = arr[h],arr[i+1]\n",
    "    return (i+1)\n",
    "\n",
    "\n",
    "def quickSortIterative(arr,l,h):\n",
    "    # Create an auxiliary stack\n",
    "    size = h - l + 1\n",
    "    stack = [0] * (size)\n",
    "  \n",
    "    # initialize top of stack\n",
    "    top = -1\n",
    "  \n",
    "    # push initial values of l and h to stack\n",
    "    top = top + 1\n",
    "    stack[top] = l\n",
    "    top = top + 1\n",
    "    stack[top] = h\n",
    "    \n",
    "    while top >= 0:\n",
    "    # Pop h and l\n",
    "        h = stack[top]\n",
    "        top = top - 1\n",
    "        l = stack[top]\n",
    "        top = top - 1\n",
    "  \n",
    "        # Set pivot element at its correct position in\n",
    "        # sorted array\n",
    "        p = partition( arr, l, h )\n",
    "        \n",
    "        # If there are elements on left side of pivot,\n",
    "        # then push left side to stack\n",
    "        if p-1 > l:\n",
    "            top = top + 1\n",
    "            stack[top] = l\n",
    "            top = top + 1\n",
    "            stack[top] = p - 1\n",
    "            \n",
    "        # If there are elements on right side of pivot,\n",
    "        # then push right side to stack\n",
    "        if p+1 < h:\n",
    "            top = top + 1\n",
    "            stack[top] = p + 1\n",
    "            top = top + 1\n",
    "            stack[top] = h\n",
    "            \n",
    "# Driver code to test above\n",
    "arr = [4, 3, 5, 2, 1, 3, 2, 3]\n",
    "n = len(arr)\n",
    "quickSortIterative(arr, 0, n-1)\n",
    "print (\"Sorted array is:\")\n",
    "for i in range(n):\n",
    "    print (arr[i])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "172d395f",
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
