//DFS using adj_list & stack

#include<stdio.h>
#include<stdlib.h>
#define MAX_VERTICES 50


typedef struct graphNode{

    int vertext;
    struct graphNode *link;

}graphNode;

typedef struct graphType{

    int n;
    graphNode *adj_list[MAX_VERTICES];

    int visited[MAX_VERTICES];
}graphType;


void init(graphType *g){

    int v;
    g->n = 0;

    for(v=0; v< MAX_VERTICES; v++){

        g->adj_list[v] = NULL; // init zero of vertex head
        g->visited[v] = 0;
    }
}

void insert_vertex(graphType *g, int v){


    if((g->n) +1 > MAX_VERTICES){
        fprintf(stderr, "Vertex overflow");
        return;
    }
    g->n++;
}

void insert_edge(graphType *g, int u, int v){

    graphNode *node = (graphNode*)malloc(sizeof(graphNode));
    if(u>= g->n || v>= g->n){ // if vertex of edge over defined vertex num
        fprintf(stderr, "Vertex error");
        return;
    }

    node->vertext = v;
    node->link = g->adj_list[u];
    g->adj_list[u] = node;

}

void print_adj_list(graphType *g){

    for(int i=0; i<g->n; i++){
        graphNode *p = g->adj_list[i];
        printf("Adj list of Vertex %d: ",i);
        while(p!=NULL){
            printf("%d -> ", p->vertext);
            p = p->link;
        }
        printf("\n");
    }

}

typedef struct stackNode{
    int data;
    struct stackNode *next;

}stackNode;

stackNode *top;

int isEmpty(){

    if(top==NULL){
        return 1;
    }else{return 0;}

}

void push_stack(int data){

    stackNode *newnode = (stackNode*)malloc(sizeof(stackNode));

    newnode->data = data;
    newnode->next = top;
    top = newnode;

}

int pop_stack(){

    if(!isEmpty()){
        int data;
        stackNode *temp = top;

        data = temp->data;
        top = temp->next;
        free(temp);

        return data;

    }else{
        printf("empty stack!\n");
        return 0;
        }
}


void DFS(graphType *g, int v){


    graphNode *w;
    top = NULL;
    push_stack(v);

    g->visited[v] = 1;
    printf("%d ", v);

    while(!isEmpty()){
        v = pop_stack();
        w = g->adj_list[v];
        while(w){
            if (g->visited[w->vertext] == 0){
                push_stack(w->vertext);
                g->visited[w->vertext] = 1;
                printf("%d ", w->vertext);
                v = w->vertext;
                w = g->adj_list[v];
            }else{
                w = w->link;
            }

        }

    }
}

