#include<stdio.h>
#include<stdlib.h>
#include<string.h>


typedef struct _stack{
    int data;
    struct stack *link;

} stack;

stack* top;


int isEmpty(){

    if(top == NULL){

        printf("stack is empty\n");
        return 1;
    }
    return 0;
}

void push(int data){


    stack *newnode = malloc(sizeof(stack)); //create struct pointer named 'newnode'

    newnode->data = data; // newnode's data is input data
    newnode->link = top; // newnode's link is top node's address

    top=newnode; // assign top to newnode

}

int pop(){

    if(!isEmpty()){
            stack *temp = top; //create node named 'temp' pointing top node
            int data = temp->data; // return data is temp's data
            top = temp->link; // assign top to temp->link
            free(temp); //free temp
            return data; //return data
       }
}

int peek(){
    if(!isEmpty()){

        return top->data;
    }

}

void printStack(){

    if(!isEmpty()){

        stack *temp = top;

        printf("from top to bottom\n");
        while(temp){

            printf("%d ",temp->data);

            temp = temp->link;

        }
        printf("\n\n");

    }
}

int main(){


    printStack();
    push(1);
    push(2);
    push(3);
    pop();
    push(5);
    printStack();
    push(2);
    push(42);
    printStack();
}

