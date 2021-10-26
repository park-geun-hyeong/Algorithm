#include<stdio.h>

void printfile(char *file){
	
	char cha;
	FILE* fp = fopen(file, "r");
	
	if(fp == NULL){
		printf("no file\n");
		fclose(fp);
	}
	
	while(feof(fp) == 0){
		fscanf(fp, "%c", &cha);
		printf("%c", cha);
	}		
	fclose(fp);
	
}
