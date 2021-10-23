#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>

int main(int argc, char *argv[]){


	char buf[1024];
	int nread;
	
	nread = readlink(argv[1], buf, 1024);
	if(nread>0){
		
		write(1, buf, nread);
		printf("\n");
		exit(0);
	}
	else{
	
		fprintf(stderr, "error: no link\n");
		exit(1);
	
	}  

	return 0;
}
