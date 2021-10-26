#include<stdio.h>
#include<stdlib.h>
#include "print.c"
#include "wc.c"

// show file's txt & file's line_cnt, word_cnt, char_cnt

int main(int argc, char *argv[]){


	if(argc<1){
		printf("input file name");
		exit(1);
	}
	
	for(int i = 1; i<argc; i++ ){
	
		printfile(argv[i]);
		wc(argv[i]);
	}
	return 0;

}
