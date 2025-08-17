// TC: printMiddle() -> O(n)
// SC: O(1) (printMiddle() requires constant memory)
// Explanation in Sample.java
#include<bits/stdc++.h>  
using namespace std;  
   

class LinkedList {
    private:
    // Struct  
    struct Node  
    {  
        int data;  
        struct Node* next;  
    }; 
    Node* head;
    public:
    LinkedList() {
        head = nullptr;
    }
    ~LinkedList() {
        while(head){
            Node* temp = head;
            head = head->next;
            delete temp;
        }
    }
    /* Brute force to find middle of the linked list */
    void printMiddleBruteForce() {
        if(!head){
        // throw exception
            cerr<<"Linked list is empty!"<<endl;
            return;
        }
        if(!head->next){
            cout<<"Middle element: "<<head->data<<endl;
            return;
        }
        Node* temp = head;
        int len = 0;
        while(temp){ // keep going till we hit nullptr
            temp = temp->next;
            len++;
        }
        temp = head;
        for(int i=0; i<len/2; i++) { // iterate till len/2 to end up at the middle of the list 
            temp = temp->next;
        }
        cout<<"Middle element: "<< temp->data<<endl;
    }
    
    /* Function to get the middle of the linked list*/
    void printMiddle()  
    {  
    //YourCode here
    if(!head){
        // throw exception
        cerr<<"Linked list is empty!"<<endl;
        return;
    }
    if(!head->next){
        cout<<"Middle element: "<<head->data<<endl;
        return;
    }
    //Use fast and slow pointer technique
    Node* fast = head;
    Node* slow = head;
    while(fast != nullptr && fast->next != nullptr){
        slow = slow->next;
        fast = fast->next->next;
    }
    cout<<"Middle element: "<< slow->data<<endl;
    }  
  
    // Function to add a new node  
    void push(int new_data)  
    {  
        Node* new_node = new Node;  
        new_node->data = new_data;  
        new_node->next = head;  
        head = new_node;  
    }  

    // A utility function to print a given linked list  
    void printList()  
    {  
        Node* ptr = head;
        while (ptr != NULL)  
        {  
            printf("%d->", ptr->data);  
            ptr = ptr->next;  
        }  
        printf("NULL\n");  
    }  
};


  
// Driver Code 
int main()  
{    /* TEST CASES */
    // LinkedList list; // empty list
    // list.printList();         
    // list.printMiddle();        
    
    LinkedList list; // normal list
    for (int i=15; i>0; i--)  
    {  
        list.push(i);   
    }  
    list.printList();  // moved printList and printMiddle out of the loop to print only when the list is completely created
    list.printMiddle();

    // LinkedList list; // single element
    // list.push(12);             
    // list.printList();         
    // list.printMiddle();

    // LinkedList list; // odd length
    // for (int i=5; i>=1; i--) {
    //    list.push(i); 
    // }   
    // list.printList();         
    // list.printMiddle(); 

    // LinkedList list; // even length
    // for (int i=6; i>=1; i--) {
    //    list.push(i);
    // }
    // list.printList();
    // list.printMiddle();

    // LinkedList list;
    // for (int i=0; i<5; i++) {
    //    list.push(5); 
    // } 
    // list.printList();     
    // list.printMiddle(); 

    return 0;  
}