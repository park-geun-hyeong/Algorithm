#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<memory.h>
#define MAX_V 10

typedef struct graphNode{

    int data;
    struct graphNode *link;

}graphNode;

typedef struct graphType{

    int n;
    graphNode *head[MAX_V];
    int visited[MAX_V];

}graphType;

void getGraph(graphType *g){

    int v=0;
    g->n = 0;
    for(v=0; v<MAX_V; v++){

        g->head[v] =NULL;
        g->visited[v] = 0;
    }
}

void add_V(graphType *g, int v){
    if((g->n)+1>MAX_V){
        fprintf(stderr ,"Vertex FULL!\n");
        return;
    }

    g->n++;
}

void add_E(graphType *g, int x, int y){

    graphNode *node;
    if(x >= g->n || y>= g->n){
        fprintf(stderr, "Vertex ERROR\n");
        return;
    }

    node = (graphNode*)malloc(sizeof(graphNode));
    node->data = y;
    node->link = g->head[x];
    g->head[x] = node;
}

typedef struct QueueNode{

    int data;
    struct QueueNode *next;
}QueueNode;

typedef struct Queue{
    struct QueueNode *front, *rear;
}Queue;

Queue *getQ(){
    Queue *Q = (Queue*)malloc(sizeof(Queue));
    Q->front = NULL;
    Q->rear = NULL;

    return Q;
}


int isEmpty(Queue *q){
    if(q->front == NULL){
            return 1;
    }else{return 0;}
}

void push_Queue(int data, Queue *q){

    QueueNode *newnode = (QueueNode*)malloc(sizeof(QueueNode));
    newnode->data = data;
    newnode->next = NULL;

    if(isEmpty(q)){
        q->front = newnode;
        q->rear = newnode;
    }else{
        newnode->next = q->rear->next;
        q->rear = newnode;
    }
}

int pop_Queue(Queue *q){

    if(isEmpty(q)){
        fprintf(stderr, "NULL QUEUE\n");
        return 0;
    }else{

        int data;
        QueueNode *temp;
        temp = q->front;
        data = temp->data;
        q->front = temp->next;
        if(q->front == NULL){
            q->rear = NULL;
        }
        free(temp);
        return data;
    }
}

void BFS(graphType* g, int v){

    graphNode *w;
    Queue *Q;
    Q = getQ();

    g->visited[v] = 1;
    printf("%d ",v);
    push_Queue(v, Q);

    while(!isEmpty(Q)){
        v = pop_Queue(Q);
        for(w = g->head[v]; w; w = w->link){
            if(!g->visited[w->data]){
                g->visited[w->data] = 1;
                printf("%d ",w->data);
                push_Queue(w->data, Q);

            }

        }

    }
}
