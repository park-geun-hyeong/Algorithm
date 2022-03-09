#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<map>
#include<deque>

using namespace std;

char matrix[5][5];

void mk_matrix(string key){

    map<char, int> check;
    for(char i= 'A'; i<='Z'; i++){
        check[i] = 1;

    }
    check.erase('J');

    int key_length = key.size();
    int row = 0;
    int col = 0;
    for(int i = 0; i < key_length; i++){
        if(check.find(key[i])!=check.end()){
            matrix[row][col] = key[i];
            col++;
            check.erase(key[i]);

            if(col == 5){
                col = 0;
                row ++;
            }
        }
    }

    if(check.size() != 0){
        for(auto iter = check.begin(); iter!=check.end(); iter++){
            matrix[row][col] = iter->first;
            col++;
            if(col == 5){
                col = 0;
                row ++;
            }
        }
    }
}

vector<string> split_message(string message){

    deque<char> mes;
    vector<string> new_string;
    int message_length = message.size();

    for(int i = 0; i<message_length; i++){
        mes.push_back(message[i]);
    }

    char x;
    string temp;

    temp = "";
    while(mes.size()!= 0){
        x = mes.front();

        if(temp.size() == 0){
            temp = temp+x;
            mes.pop_front();
            continue;
        }

        if(temp.size() == 1){
            if(temp[0] != x){
                temp = temp+x;
                mes.pop_front();
            }else{
                if(temp[0] == 'X'){
                    temp = temp+'Q';
                }else{
                    temp = temp+'X';
                }
            }
        }
        if(temp.size() == 2){
            new_string.push_back(temp);
            temp = "";
        }
    }

    if(temp.size() == 1){
        temp = temp + 'X';
        new_string.push_back(temp);
        }

    return new_string;
}

int main(){

    string message, key;
    getline(cin, message);
    getline(cin, key);

    mk_matrix(key);

    vector<string> split_M;
    split_M = split_message(message);


    string ans = "";
    int first_row, first_col, second_row,second_col;


