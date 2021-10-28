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

struct LinkedList *createNode(int data){

    struct LinkedList *temp = (struct LinkedList*)malloc(sizeof(struct LinkedList));
    temp ->next= NULL;
    temp->data = data;
    return temp;
};

void LL_insert_node_last(int data, struct LinkedList **head){

    struct LinkedList *newnode = createNode(data);

    if((*head) == NULL){
        (*head) = newnode;
    }
    else{
        struct LinkedList *temp = *head;
        while(temp ->next !=NULL){
            temp = temp->next;
        }
        temp->next = newnode;
    }

    push(data);

}

void LL_display(struct LinkedList *head){

    struct LinkedList *p = head;
    printf("List after insert operations: ");

    while(p->next != NULL){
        printf("%d ", p->data);
        p = p->next;
    }

    printf("\nReversed: ");
    if(isEmpty() == 0){
        stackNode *temp = top;
        while(temp){
            printf("%d ", temp->data);
            temp = temp->link;
        }
    }
}

int main(){

    for(int i=0; i < 10; i++){
       LL_insert_node_last(i, &head);
    }

    LL_display(head);

    return 0;
}

