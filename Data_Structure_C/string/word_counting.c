
// word count using flag

#include<stdio.h>
#include<ctype.h>

int count_word(char *s);

int main(){

    char ss[40];
    printf("input sentence: ");
    gets(ss);

    int wc = count_word(ss);
    printf("the word cnt of '%s': %d\n", ss, wc);

    return 0;
}

int count_word(char *s){

    int i, wc = 0;
    int waiting = 1;

    for(i =0; s[i]!=NULL; i++){
        if(isalpha(s[i])){
            if(waiting){
                wc++;
                waiting = 0;
            }
        }else{
            waiting = 1;
        }
    }
    return wc;
}

