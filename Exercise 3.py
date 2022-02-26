{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "801c146d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5->NULL\n",
      "The middle element is  5\n",
      "4->5->NULL\n",
      "The middle element is  5\n",
      "3->4->5->NULL\n",
      "The middle element is  4\n",
      "2->3->4->5->NULL\n",
      "The middle element is  4\n",
      "1->2->3->4->5->NULL\n",
      "The middle element is  3\n"
     ]
    }
   ],
   "source": [
    "class Node:\n",
    "   \n",
    "    # Function to initialise the node object\n",
    "    def __init__(self, data):\n",
    "        self.data = data  # Assign data\n",
    "        self.next = None  # Initialize next as null\n",
    "\n",
    "class LinkedList:\n",
    "   # Function to initialize head\n",
    "    def __init__(self):\n",
    "        self.head = None\n",
    "        \n",
    "    # Function to insert a new node at the beginning \n",
    "    def push(self, new_data): \n",
    "        new_node = Node(new_data) \n",
    "        new_node.next = self.head \n",
    "        self.head = new_node\n",
    "        \n",
    "    # Print the linked list\n",
    "    def printList(self):\n",
    "        node = self.head\n",
    "        while node:\n",
    "            print(str(node.data) + \"->\", end=\"\")\n",
    "            node = node.next\n",
    "        print(\"NULL\")\n",
    "        \n",
    "    # Function that returns middle.\n",
    "    def printMiddle(self):\n",
    "        # Initialize two pointers, one will go one step a time (slow), another two at a time (fast)\n",
    "        slow = self.head\n",
    "        fast = self.head\n",
    "        \n",
    "        # Iterate till fast's next is null (fast reaches end)\n",
    "        while fast and fast.next:\n",
    "            slow = slow.next\n",
    "            fast = fast.next.next\n",
    "            \n",
    "        # return the slow's data, which would be the middle element.\n",
    "        print(\"The middle element is \", slow.data)\n",
    "        \n",
    "# Code execution starts here\n",
    "if __name__=='__main__':\n",
    "   \n",
    "    # Start with the empty list\n",
    "    llist = LinkedList()\n",
    "   \n",
    "    for i in range(5, 0, -1):\n",
    "        llist.push(i)\n",
    "        llist.printList()\n",
    "        llist.printMiddle()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "396d568a",
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
