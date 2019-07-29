#include<iostream>
using namespace std;

// Struct
struct Node
{
    int data;
    struct Node* next;
    struct Node * fast,* slow = NULL;   //created slow and fast pointers to get the middle element.

};


void printMiddle(struct Node *head)
{
    struct Node* temp = head;
    struct Node * fast = temp;              //Initialisation of fast and slow pointers to head of the node.
    struct Node * slow = temp;

    cout<<slow->data;
        while (fast->next != NULL && fast!= NULL)
        {                                    // while loop to get to the end of the list.
            fast = fast->next->next;        // fast pointer moves two places while slow
            slow = slow->next;              // pointer moves one place. So when fast pointer reaches NULL or last node
                                            // slow pointer reaches to the mid point of the List.
        }
        cout << "Middle element = " << slow->data;  // print the data present at the mid point.

}

// Function to add a new node
void push(struct Node** head_ref, int new_data)
{
    struct Node* new_node = new Node;    // Create a new node.
    new_node->data = new_data;
    new_node->next = (*head_ref);		// Point the node to Head. If List empty then Head is NULL.
    (*head_ref) = new_node;            
}

// A utility function to print a given linked list
void printList(struct Node *ptr)
{
    while (ptr != NULL)
    {
        printf("%d->", ptr->data);
        ptr = ptr->next;
    }
    printf("NULL\n");
}

// Driver Code
int main()
{
    struct Node* head = NULL;
    for (int i=15; i>0; i--)
    {
        push(&head, i);
        printList(head);
        printMiddle(head);

    }
    return 0;
}