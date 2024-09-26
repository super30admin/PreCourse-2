// Time Complexity  O(n)
// Space Complexity :O(1)
// Did this code successfully run on Leetcode : N/A
// Any problem you faced while coding this : N/A


// Your code here along with comments explaining your approach

//Finding the middle element in a linked list : Hare and Tortoise algorithm

#include <iostream>

using namespace std;

template<typename T>
struct node_s {
    T data;
    node_s * link;
};




template <typename T>
void list_insert(node_s<T> **monitored_stack_head, T value, int index){
    //create new node_s
    node_s<T> * new_node = new(node_s<T>);
    new_node->data = value;
    new_node->link =NULL;
    
    //edge case
    if (index==1 ){
        if (*monitored_stack_head==NULL){
            *monitored_stack_head = new_node;
        }
        else{
            new_node->link = *monitored_stack_head;
            *monitored_stack_head  = new_node;
        }
        return;
    }
    node_s<T> * temp = *monitored_stack_head;
    while(temp->link!=NULL && index>2){
        temp=temp->link;
        index--;
    }
    //Element is added
    new_node->link = temp->link;
    temp->link = new_node;
}

template <typename T>
int  list_find_mid(node_s<T> **monitored_stack_head){
    int index=1;
    node_s<T> * first_ptr = *monitored_stack_head;
    node_s<T> * second_ptr = *monitored_stack_head;
    
    while(second_ptr->link!=NULL && second_ptr->link->link!=NULL){
        second_ptr = second_ptr->link->link;
        first_ptr  = first_ptr->link;
        index++;
    }
    cout<<"Mid is  : "<<first_ptr->data<<" at "<<index<<"\n";
    return index;
}


template <typename T>
void list_display(node_s<T> **head){
    node_s<T> * temp = *head;
    while(temp!=NULL){
        cout<<temp->data<<"\t";
        temp=temp->link;
    }
}



int main(){

    node_s<int> * head = NULL;
    
    list_insert(&head, 1, 1);
    list_insert(&head, 2, 2);
    list_insert(&head, 3, 3);
    list_insert(&head, 4, 4);
    list_insert(&head, 5, 5);
    list_insert(&head, 6, 6);
    list_insert(&head, 7, 7);
    list_insert(&head, 8, 8);
    list_insert(&head, 9, 9);
    list_insert(&head, 10, 10);
    list_insert(&head, 11, 11);
    list_insert(&head, 12, 12);
    list_insert(&head, 13, 13);
    list_insert(&head, 14, 14);
    list_insert(&head, 15, 15);
    list_insert(&head, 16, 16);
    
    list_display(&head);
    cout<<"\n";
    
    
    list_find_mid(&head);
    
    return 0;
}

