#include<stdio.h>
#include<stdlib.h>

struct LinkedList{

    int data;
    struct LinkedList *next;
};

typedef struct stackNode{

    int data;
    struct stackNode *link;

} stackNode;

stackNode *top = NULL;
struct LinkedList *head = NULL;

void push(int data){

    stackNode *newnode = (stackNode *)malloc(sizeof(stackNode));

    newnode -> data = data;
    newnode -> link = top;
    top = newnode;
}

int isEmpty(){

    if(top == NULL) return 1;
    else return 0;
}

void pop(){

    int item;
    stackNode *temp = top;

    if(top == NULL) return 0;
    else{
        item = top ->data;
        top = temp->link;
        free(temp);
        return item;
    }
}

void LL_insert_node_last(int data, struct LinkedList **head){

    struct LinkedList *node = malloc(sizeof(struct LinkedList));

    node -> next = *head;
    node -> data = data;
    *head = node;

    push(data);
}

void LL_display(struct LinkedList *head){


    if(head != NULL){
        struct LinkedList *temp = head;
        while(head){
            printf("%d ", head->data);
            head = head-> next;
        }
    }

    printf(" StackNode: ");
    if(isEmpty() == 0){
        stackNode *temp = top;
        while(temp){
            printf("%d ", temp->data);
            temp = temp->link;
        }
    }
}


int main(){

    int i;

    printf("List after insert operations: ");
    for(i=0; i < 10; i++){
        LL_insert_node_last(i, &head);
        printf("%d ", i);
    }

    printf("\nReversed: ");
    LL_display(head);

    return 0;
}

