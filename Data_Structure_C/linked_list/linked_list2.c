#include<stdio.h>
#include<stdlib.h>



struct NODE{

    struct NODE *next;
    int data;
};

void addfirst(struct NODE *target, int data){

    // create node next to target node

    struct NODE *newnode = malloc(sizeof(struct NODE));

    newnode->next = target->next; //change link node of new_node first
    newnode->data = data; // input data of new_node
    target->next = newnode; // change link node of target node to new_node's address


}

int main(){


    struct NODE *head = malloc(sizeof(struct NODE));

    head->next = NULL;

    addfirst(head, 30);
    addfirst(head, 20);
    addfirst(head, 10);

    struct NODE *curr = head->next;

    while(curr != NULL){
        printf("%d\n", curr->data);
        curr = curr->next;

    }

    curr =head->next;
    while(curr != NULL){

        struct NODE *next = curr->next;
        free(curr);
        curr = next;

    }

    free(head);

    return 0;
}

