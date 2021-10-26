#include<stdio.h>


void wc(char *file){

	FILE *fd = fopen(file, "r");
	
	if(fd == NULL){
		printf("no file\n");
		fclose(fd);
	}
	
	int c;
	int i;
	int lc =0;
	int wc=0;
	int cc=0;
	int is_word = 0;
	
	c= getc(fd);
	
	while(c != EOF){
	
		cc++;
		if(c>= 33 && c<= 127){
		
			is_word = 1;
		}
		else{
			if(is_word == 1){
				wc ++;
			}
			is_word =0;
			if(c == 10 || c == 13){
				lc ++;
			}
		
		
		}
		c=getc(fd);
		
	
	}
		
	printf("char count: %d word count: %d line count:%d\n",cc,wc,lc);

}
