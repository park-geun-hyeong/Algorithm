#include<stdio.h>
#include<stdlib.h>
#define Max 1001

int adj[Max][Max] = {0, };
int visited[Max] = {0, };


typedef struct Node{

    int data;
    struct Node *next;

}Node;

typedef struct Queue{
    Node *head;
    Node *tail;
    int cnt;
}Queue;

int isEmpty(Queue *q);
void initQueue(Queue *q);
void AddQuue(int data, Queue *q);
int deleteQueue(Queue *q);
void BFS(int start, int v, Queue *q);

int main(){

    Queue *queue;
    initQueue(queue);

    int v,e;
    int x,y;
    int start = 1;

    printf("input VertextNum & EdgeNum\n");
    scanf("%d %d", &v, &e);
    printf("\n");
    printf("input Edge information\n");
    for(int i=1; i<=e; i++){
        scanf("%d %dW", &x, &y);
        adj[x][y] = 1;
        adj[y][x] = 1;
    }

    BFS(start, v, queue);
    return 0;
}


int isEmpty(Queue *q){
    if(q->cnt == 0){
        return 1;
    }else{return 0;}
}

void initQueue(Queue *q){
    q->head = NULL;
    q->tail = NULL;
    q->cnt = 0;
}

void AddQueue(int data, Queue *q){
    Node *now = (Node *)malloc(sizeof(Node));

    now->data = data;
    now->next = NULL;

    if(isEmpty(q)){
        q->head = now;
    }else{
        q->tail->next = now;
    }

    q->tail = now;
    q->cnt++;

}

int deleteQueue(Queue *q){

    int re=0;
    Node *now = (Node *)malloc(sizeof(Node));

    if(isEmpty(q)){return 0;}

    now = q->head;
    re = now->data;
    q->head = now->next;
    free(now);
    q->cnt--;

    return re;
}

void BFS(int start, int v, Queue *q){
    int temp;

    int x;
    visited[start] = 1;

    for(int i = 0; i<=v; i++){
        if(adj[start][i] == 1){
            AddQueue(i, q);
            visited[i] = 1;
        }
    }

    printf("%d ", start);

    while(!isEmpty(q)){

        x = deleteQueue(q);
        printf("%d ", x);

        for(int j=0; j<=v; j++){
            if(adj[x][j] == 1){
                temp = j;
                if(visited[temp] == 0){
                    AddQueue(temp, q);
                    visited[temp] = 1;
                }
            }
        }

    }
}

