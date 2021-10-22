# include <stdio.h>
# define SIZE 5

int stack[SIZE];
int top=-1;

int isFull(){

    if(top>=(SIZE-1)){
        printf("stack is full\n");
        return 1;
    }
    else
        return 0;
}

int isEmpty(){

    if (top == -1){
        printf("stack is empty\n");
        return 1;

    }
    else
        return 0;
}

void push(char data){

    if(isFull() == 0){
        top++;
        stack[top] = data;
    }
}

int pop(){

    if(isEmpty() == 0){
        int temp = stack[top];
        top--;
        return temp;

    }
}

int peek(){
    if(!isEmpty()){
        return stack[top];
    }
}


int main(){

    push(1);
    push(2);
    push(3);
    pop();
    push(4);
    push(5);
    push(6);
    pop();
    push(7);
    for(int i=0;i<SIZE;i++){
        printf("%d\n",stack[i]);
    }
}

