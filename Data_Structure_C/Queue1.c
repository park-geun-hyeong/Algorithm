#include<stdio.h>
#include<stdlib.h>
#include<string.h>

typedef struct{ // define Node Struct
    int data;
    struct Node *next;
}Node;

typedef struct { //define Queue Struct using Node Struct
    Node *front;
    Node *rear;
    int count; // Queue's number of data
}Queue;

void InitQueue(Queue *queue);
int isEmpty(Queue *queue);
void Enqueue(Queue *queue, int data);
int Dequeue(Queue *queue);

int main(){

    Queue queue;
    InitQueue(&queue);

    for(int i =0; i<=5; i++){
        Enqueue(&queue, i);
    }

    while(!isEmpty(&queue)){
        printf("%d ", Dequeue(&queue));
    }
    printf("\n");
    return 0;


}

void InitQueue(Queue *queue){
    queue->front = queue->rear = NULL;
    queue->count = 0;
}

int isEmpty(Queue *queue){

    if(queue->count == 0){ return 1;}
    else{return 0;}

}

void Enqueue(Queue *queue, int data){

    Node *now = (Node*)malloc(sizeof(Node));
    now -> data = data;
    now -> next = NULL;

    if(isEmpty(queue)){ queue->front = now;}
    else{queue->rear->next = now;}

    queue->rear = now;
    queue->count++;

}

int Dequeue(Queue *queue){

    int re = 0;
    Node *now = (Node*)malloc(sizeof(Node));
    if(isEmpty(queue)){return 0;}

    now = queue->front;
    re = now->data;
    queue->front = now->next;
    free(now);

    queue->count--;
    return re;
}


