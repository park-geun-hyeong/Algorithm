//adj list using linked list

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

}graphType;


void init(graphType *g){

    int v;
    g->n = 0;

    for(v=0; v< MAX_VERTICES; v++){

        g->adj_list[v] = NULL;
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

    graphNode *node;
    if(u>= g->n || v>= g->n){
        fprintf(stderr, "Vertex error");
        return;
    }

    node = (graphNode*)malloc(sizeof(graphNode));
    node->vertext = v;
    node->link = g->adj_list[u];
    g->adj_list[u] = node;

}

void print_adj_list(graphType *g){

    for(int i=0; i<g->n; i++){
        graphNode *p = g->adj_list[i];
        printf("Adj list of Vertext %d: ",i);
        while(p!=NULL){
            printf("%d -> ", p->vertext);
            p = p->link;
        }
        printf("\n");
    }

}

int main(){

    graphType *g;
    g = (graphType*)malloc(sizeof(graphType));

    init(g);

    for(int i = 0; i<6; i++){
        insert_vertex(g,i);
    }

    insert_edge(g, 0, 1);
	insert_edge(g, 1, 0);
	insert_edge(g, 0, 2);
	insert_edge(g, 2, 0);
	insert_edge(g, 0, 3);
	insert_edge(g, 3, 0);
	insert_edge(g, 0, 5);
	insert_edge(g, 5, 0);
	insert_edge(g, 1, 2);
	insert_edge(g, 2, 1);
	insert_edge(g, 2, 5);
	insert_edge(g, 5, 2);
	insert_edge(g, 3, 4);
	insert_edge(g, 4, 3);
	print_adj_list(g);



    free(g);
    return 0;
}

