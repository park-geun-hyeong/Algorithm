#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;
int graph[21][21] = {0,};
int order[1001] ={0,};
int drow[5] = {0,0,0,-1,1};
int dcol[5] = {0,1,-1,0,0};
int dice[7] = {0,};

void change_dice(int direction){

    int tmp = 0;

    if(direction == 1){
        tmp = dice[3];
        dice[3] = dice[1];
        dice[1] = dice[4];
        dice[4] = dice[6];
        dice[6] = tmp;
    }
    else if(direction == 2){
        tmp = dice[4];
        dice[4] = dice[1];
        dice[1] = dice[3];
        dice[3] = dice[6];
        dice[6] = tmp;
        }

    else if(direction == 3){
        tmp = dice[5];

        dice[5] = dice[1];
        dice[1] = dice[2];
        dice[2] = dice[6];
        dice[6] = tmp;
        }

    else if(direction == 4){
        tmp = dice[2];
        dice[2] = dice[1];
        dice[1] = dice[5];
        dice[5] = dice[6];
        dice[6] = tmp;
    }
}

void solution(int x, int y, int n, int m, int k){

    int row = x;
    int col = y;

