#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(int argc, char *argv[]){


	if(argc!=3){
		fprintf(stderr, "usage: %s EnvironName EnvironValue\n", argv[0]);
		exit(1);
	}
	
	char *ptr;
	char check;
	int result;
	
	if((ptr = getenv(argv[1])) == NULL){ // if ENV not exist
		if((result = (setenv(argv[1], argv[2], 0))) == 0){
			printf("set env OK\n");	
		}
		else{printf("set env fail\n");}
	}else{ // Env exist
		printf("Env Name: %s , Current Env Value : %s\n", argv[1], ptr);
		printf("Are You change of your new Env Value?(Y/N)\n");
		scanf("%c", &check);
	
		if(check == 'Y'){
			if((result = (setenv(argv[1], argv[2], 1))) == 0){
				printf("set env OK\n");
			}else{printf("set env fail\n");}
		}else{ 
			printf("No change\n");
			exit(0);
		}
	}
		
	exit(0);
	return 0;
}
