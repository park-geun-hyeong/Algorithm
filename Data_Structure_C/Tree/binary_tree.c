#include<stdio.h>
#include<stdlib.h>
#include<string.h>


typedef struct{

    struct tree_node *left;
    int data;
    struct tree_node *right;

}tree_node;

tree_node* insert(tree_node *root, int data);
tree_node* fMin(tree_node *root);
tree_node* Delete(tree_node *root, int data);
//tree_node* initNode(tree_node *root);
void print(tree_node *root);
void preorder(tree_node *root);
void inorder(tree_node *root);
void postorder(tree_node *root);

tree_node *root;

int main(){

    root = insert(root ,5);
    root = insert(root, 1);
    root = insert(root, 3);

    preorder(root);
    printf("\n");
    inorder(root);
    printf("\n");
    postorder(root);


    return 0;
}

tree_node* insert(tree_node* root ,int data){

    if(root == NULL){
            root = (tree_node*)malloc(sizeof(tree_node));
            root->left = root->right = NULL;
            root->data = data;
            return root;
    }

    else{
        if(data < root->data){root->left = insert(root->left, data);}
        else{root->right = insert(root->right, data);}
    }
    return root;

}

tree_node* fMin(tree_node* root){

    tree_node *min = root;
    while(min->left!=NULL){ min = min->left;}
    return min;
}

tree_node* Delete(tree_node *root, int data){

    tree_node *tmp = NULL;

    if(root == NULL){return NULL;}
    if(data < root->data){root->left = Delete(root->left, data);}
    else if(data > root->data){root->right = Delete(root->right, data);}
    else{

        if(root ->left !=NULL && root->right != NULL){

            tmp = fMin(root->right);
            root->data = tmp->data;
            root->right = Delete(root->right, tmp->data);
        }
        else{
            tmp = (root->left ==NULL) ? root->right : root->left;
            free(root);
            return tmp;
        }
    }
    return root;

}

void print(tree_node *root){
    if(root == NULL){return;}
    printf("%d ", root->data);
    print(root -> left);
    print(root -> right);

}

void preorder(tree_node *root){
    if(root == NULL){return;}
    printf("%d ", root->data);
    print(root->left);
    print(root->right);

}

void inorder(tree_node *root){
    if(root == NULL){return;}
    print(root->left);
    printf("%d ", root->data);
    print(root->right);
}

void postorder(tree_node *root){
    if(root == NULL){return;}
    print(root->left);
    print(root->right);
    printf("%d ", root->data);

}

