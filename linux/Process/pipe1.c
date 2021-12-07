#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define maxline 100

int main(int argc , char *argv[]){

	if(argc!=2){
		fprintf(stderr, "usage: %s command_shell", argv[0]);
		exit(1);
	}
	
	char line[maxline];
	FILE *fpin;
	
	if((fpin = popen(argv[1], "r")) == NULL){
		perror("popen error");
		return 1;
	}
	
	while(fgets(line, maxline, fpin)){
		fputs(line, stdout);
	}
	pclose(fpin);	
	return 0;
}
