#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(int argc, char *argv[]){


	char line[255];
	int line_cnt = 0;	

	if(argc<1){
		printf("input file name\n");
		exit(1);
	}
	
			
	FILE *fp = fopen(argv[1],"r");
	if(fp == NULL){
		printf("file open error\n");
		fclose(fp);
	}
	
	while(fgets(line, sizeof(line), fp) != NULL){	
		line_cnt ++;
		}
	fclose(fp);
	
	FILE *fd = fopen(argv[1],"r");
	
	char arr[line_cnt][255];

	int i=0;
	while(fgets(arr[i], sizeof(char)*255 , fd) != NULL){
		i++;	
	}
		
	
	for(int j = line_cnt - 1; j >= 0; j--){
		
		printf("%s", arr[j]);	
	}
	
	fclose(fd);
	return 0;
}
